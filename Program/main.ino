#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdbool.h>
#include <stdlib.h>

// === Konstanta ===
#define BAUDRATE 9600
#define VBAUDRATE (F_CPU / ((unsigned long) BAUDRATE * 16) - 1)
#define BAUDH VBAUDRATE / 256
#define BAUDL VBAUDRATE % 256

#define SENSOR_ASAP_THRESHOLD 600
#define SENSOR_GAS_THRESHOLD 600
#define SHOWER_THRESHOLD 1000

#define LED_BAHAYA   PG5
#define LED_AMAN     PE5
#define BUZZER       PE3

#define RELAY1_PIN   PB7
#define RELAY2_PIN   PB6
#define SHOWER_PIN   PE4

#define SET_BIT(port, bit)     ((port) |= (1 << (bit)))
#define CLR_BIT(port, bit)     ((port) &= ~(1 << (bit)))

// === Variabel Global ===
volatile bool gasBahaya = false;
bool lastGasState = false;
bool showerAktif = false;

volatile bool asapBahaya = false;
bool lastAsapState = false;

// === UART ===
void UARTInit(void) {
    UBRR0H = BAUDH;
    UBRR0L = BAUDL;
    UCSR0B = (1 << TXEN0);
    UCSR0C = (1 << UCSZ01) | (1 << UCSZ00);
}

void UART_print(const char *str) {
    while (*str) {
        while (!(UCSR0A & (1 << UDRE0)));
        UDR0 = *str++;
    }
}

void UART_print_number(uint16_t number) {
    char buffer[10];
    itoa(number, buffer, 10);
    UART_print(buffer);
}

// === Timer untuk Buzzer ===
void timer3_init_ctc() {
    TCCR3A = 0;
    TCCR3B = (1 << WGM32) | (1 << CS31); // CTC mode, prescaler 8
    OCR3A = 9999; // ~1kHz
    TIMSK3 = 0;   // Matikan interrupt dulu
    DDRE |= (1 << BUZZER); // BUZZER sebagai output
    sei(); // Enable global interrupt
}

ISR(TIMER3_COMPA_vect) {
    PORTE ^= (1 << BUZZER); // Toggle buzzer
}

void buzzer_on() {
    TIMSK3 |= (1 << OCIE3A); // Aktifkan interrupt
}

void buzzer_off() {
    TIMSK3 &= ~(1 << OCIE3A); // Nonaktifkan interrupt
    PORTE &= ~(1 << BUZZER);  // Pastikan buzzer mati
}

// === ADC ===
void adc_init() {
    ADMUX = (1 << REFS0); // AVCC reference
    ADCSRA = (1 << ADEN) | (1 << ADPS2) | (1 << ADPS1); // Enable + Prescaler
}

uint16_t adc_read_channel(uint8_t channel) {
    ADMUX = (ADMUX & 0xF0) | (channel & 0x0F);
    ADCSRA |= (1 << ADSC);
    while (ADCSRA & (1 << ADSC));
    return ADC;
}

uint16_t adc_read_gas() {
    return adc_read_channel(0); // Channel 0 untuk gas
}

uint16_t adc_read_asap() {
    return adc_read_channel(4); // Channel 4 untuk asap
}

// === IO Setup ===
void setup_io() {
    DDRG |= (1 << LED_BAHAYA);
    DDRE |= (1 << LED_AMAN) | (1 << SHOWER_PIN);
    DDRB |= (1 << RELAY1_PIN) | (1 << RELAY2_PIN);
    adc_init();
}

// === Aktuator ===
void aktifkan_shower() {
    SET_BIT(PORTE, SHOWER_PIN);
    showerAktif = true;
}

void matikan_shower() {
    CLR_BIT(PORTE, SHOWER_PIN);
    showerAktif = false;
}

void nyalakan_led_bahaya() {
    SET_BIT(PORTG, LED_BAHAYA);
    CLR_BIT(PORTE, LED_AMAN);
}

void nyalakan_led_aman() {
    CLR_BIT(PORTG, LED_BAHAYA);
    SET_BIT(PORTE, LED_AMAN);
}

// === MAIN LOOP ===
int main(void) {
    UARTInit();
    setup_io();
    timer3_init_ctc();

    while (1) {
        uint16_t sensorGas = adc_read_gas();
        uint16_t sensorAsap = adc_read_asap();

        UART_print("GAS: ");
        UART_print_number(sensorGas);
        UART_print("\r\n");

        UART_print("SMOKE: ");
        UART_print_number(sensorAsap);
        UART_print("\r\n");

        // === SENSOR GAS ===
        if (sensorGas > SENSOR_GAS_THRESHOLD) {
            gasBahaya = true;
            nyalakan_led_bahaya();
            SET_BIT(PORTB, RELAY1_PIN);

            if (!lastGasState) {
                UART_print("Gas Terdeteksi! Aktifkan FAN\r\n");
                lastGasState = true;
            }

            if (sensorGas >= SHOWER_THRESHOLD && !showerAktif) {
                aktifkan_shower();
                UART_print("Gas Sangat Tinggi! Aktifkan WATER SHOWER!\r\n");
            } else if (sensorGas < SHOWER_THRESHOLD && showerAktif) {
                matikan_shower();
                UART_print("Gas Menurun! Matikan WATER SHOWER.\r\n");
            }

        } else {
            gasBahaya = false;
            CLR_BIT(PORTB, RELAY1_PIN);

            if (lastGasState) {
                UART_print("Aman. Matikan FAN\r\n");
                lastGasState = false;
            }

            if (showerAktif) {
                matikan_shower();
                UART_print("Aman. Matikan WATER SHOWER\r\n");
            }
        }

        // === SENSOR ASAP ===
        if (sensorAsap > SENSOR_ASAP_THRESHOLD) {
            asapBahaya = true;
            nyalakan_led_bahaya();
            SET_BIT(PORTB, RELAY2_PIN);

            if (!lastAsapState) {
                UART_print("Asap Terdeteksi! Aktifkan Exhaust Fan\r\n");
                lastAsapState = true;
            }

        } else {
            asapBahaya = false;
            CLR_BIT(PORTB, RELAY2_PIN);

            if (lastAsapState) {
                UART_print("Aman. Matikan Exhaust Fan\r\n");
                lastAsapState = false;
            }
        }

        // === LED AMAN ===
        if (!gasBahaya && !asapBahaya) {
            nyalakan_led_aman();
        }

        // === BUZZER ===
        if (gasBahaya || asapBahaya) {
            buzzer_on();
        } else {
            buzzer_off();
        }

        UART_print("-----------------------------------\r\n");
        _delay_ms(1000); // Lebih responsif dari 1000ms
    }
}
