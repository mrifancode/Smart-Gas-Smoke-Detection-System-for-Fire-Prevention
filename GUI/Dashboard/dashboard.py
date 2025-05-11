from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import serial
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import deque
import time
import subprocess
import requests

# GANTI dengan token & chat ID milikmu
bot_token = '7912234203:AAG731XH8NOTCLTgOizmRmGErqUSYpRAo4Q'
chat_id = '7753137443'

def open_log_window():
    try:
        ser.close()  # Tutup port serial sebelum membuka window baru
    except:
        pass
    window.destroy()
    subprocess.Popen(["python", "LOG.py"])

def open_camera():
    try:
        ser.close()  # Tutup port serial sebelum membuka window baru
    except:
        pass
    window.destroy()
    subprocess.Popen(["python", "camera.py"])

ser = serial.serial_for_url('rfc2217://localhost:4000', baudrate=115200)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\gui\Projek\assets\frame0\DASHBOARD-Baru")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.configure(bg="#C50000")
window.attributes('-fullscreen', True)

canvas = Canvas(
    window,
    bg="#C50000",
    height=1024,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

# Fungsi untuk center canvas di fullscreen
def center_canvas():
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_offset = (screen_width - 1440) // 2
    y_offset = (screen_height - 1024) // 2
    canvas.place(x=x_offset, y=y_offset)

window.after(100, center_canvas)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    70.0,
    150.0,
    920.0,
    483.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    70.0,
    592.0,
    920.0,
    905.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    1017.0,
    562.0,
    anchor="nw",
    text="Smoke MQ135 Sensor              255",
    fill="#000000",
    font=("Inter MediumItalic", 20 * -1)
)

canvas.create_text(
    1073.0,
    878.0,
    anchor="nw",
    text="OFF",
    fill="#000000",
    font=("Inter MediumItalic", 15 * -1)
)

canvas.create_text(
    1259.0,
    883.0,
    anchor="nw",
    text="OFF",
    fill="#000000",
    font=("Inter MediumItalic", 15 * -1)
)

canvas.create_text(
    1016.0,
    435.0,
    anchor="nw",
    text="\n\nGas MQ2 Sensor                      200\n\n\n",
    fill="#000000",
    font=("Inter MediumItalic", 20 * -1)
)

canvas.create_rectangle(
    1017.0,
    513.0,
    1187.0,
    513.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    1017.0,
    591.0,
    1153.0,
    591.0,
    fill="#000000",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    1187.0,
    806.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1187.0,
    217.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1187.0,
    516.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    1092.0,
    834.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    1279.0,
    834.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    520.0,
    68.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    1205.0,
    706.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    1185.0,
    495.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    1185.0,
    576.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    1184.0,
    135.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    1093.0,
    869.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    1279.0,
    873.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    1201.0,
    422.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    1060.0,
    128.0,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    1108.0,
    706.0,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    1093.0,
    806.0,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    1278.0,
    806.0,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    366.0,
    72.0,
    image=image_image_18
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1333.0,
    y=233.0,
    width=202.0,
    height=31.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_log_window, relief="flat"
)
button_2.place(
    x=1333.0,
    y=275.0,
    width=202.0,
    height=31.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_camera, relief="flat"
)
button_3.place(
    x=1333.0,
    y=315.0,
    width=202.0,
    height=31.0
)


# ================== TEXT YANG DIUPDATE ==================
gas_text = canvas.create_text(1016.0, 435.0, anchor="nw", text="\n\nGas MQ2 Sensor                      200\n\n\n", fill="#000000", font=("Inter MediumItalic", 20 * -1))
smoke_text = canvas.create_text(1017.0, 562.0, anchor="nw", text="Smoke MQ135 Sensor              255", fill="#000000", font=("Inter MediumItalic", 20 * -1))
shower_text = canvas.create_text(1259.0, 883.0, anchor="nw", text="OFF", fill="#000000", font=("Inter SemiBoldItalic", 15 * -1))
fan_text = canvas.create_text(1073.0, 878.0, anchor="nw", text="OFF", fill="#000000", font=("Inter SemiBoldItalic", 15 * -1))
# ================== BARGRAPH ==================
# Bargraph untuk Gas
gas_bar = canvas.create_rectangle(1038, 513, 1038 + 1, 517, fill="blue", outline="")

# Bargraph untuk Smoke
smoke_bar = canvas.create_rectangle(1038, 595, 1038 + 1, 599, fill="red", outline="")

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print("Terkirim ke Telegram:", message)
        else:
            print("Gagal mengirim:", response.text)
    except Exception as e:
        print("Error:", e)

# ================== GRAFIK ==================
gas_data = deque(maxlen=50)
smoke_data = deque(maxlen=50)
time_data = deque(maxlen=50)

fig1, ax1 = plt.subplots(figsize=(8.5, 3.8), dpi=100)
fig2, ax2 = plt.subplots(figsize=(8.5, 3.8), dpi=100)

canvas_gas = FigureCanvasTkAgg(fig1, master=window)
canvas_gas.get_tk_widget().place(x=310, y=150)

canvas_smoke = FigureCanvasTkAgg(fig2, master=window)
canvas_smoke.get_tk_widget().place(x=310, y=592)

def init_graphs():
    # Set background figure dan axes ke hitam
    fig1.patch.set_facecolor('black')
    fig2.patch.set_facecolor('black')
    ax1.set_facecolor('black')
    ax2.set_facecolor('black')

    # Set warna teks dan grid ke putih
    ax1.set_title("Gas PPM", color='white')
    ax1.set_xlabel("Time", color='white')
    ax1.set_ylabel("PPM", color='white')
    ax1.tick_params(colors='white')
    ax1.grid(True, color='gray')

    ax2.set_title("Smoke PPM", color='white')
    ax2.set_xlabel("Time", color='white')
    ax2.set_ylabel("PPM", color='white')
    ax2.tick_params(colors='white')
    ax2.grid(True, color='gray')


init_graphs()

def update_graphs():
    ax1.clear()
    ax2.clear()
    init_graphs()

    ax1.plot(time_data, gas_data, color='blue', label="Gas")
    ax2.plot(time_data, smoke_data, color='red', label="Smoke")

    canvas_gas.draw()
    canvas_smoke.draw()

# ================== BACA SERIAL ==================
def read_serial():
    while True:
        try:
            line = ser.readline().decode('utf-8').strip()
            print(line)

            # === Kirim ke Telegram jika penting ===
            if any(keyword in line for keyword in ["Terdeteksi", "WATER"]):
                send_telegram_message(line)

            now = time.time()

            if line.startswith("GAS:"):
                gas_val = int(line.split(":")[1].strip())
                canvas.itemconfig(gas_text, text=f"\n\nGas MQ2 Sensor                         {gas_val}")
                gas_data.append(gas_val)
                time_data.append(now)

                    # Update bargraph gas
                max_ppm = 1000
                max_length = 300  # panjang maksimum bargraph dalam piksel
                bar_length = min(gas_val, max_ppm) / max_ppm * max_length
                canvas.coords(gas_bar, 1038, 513, 1038 + bar_length, 517)


            elif line.startswith("SMOKE:"):
                smoke_val = int(line.split(":")[1].strip())
                canvas.itemconfig(smoke_text, text=f"Smoke MQ135 Sensor                 {smoke_val}")
                smoke_data.append(smoke_val)

                bar_length = min(smoke_val, max_ppm) / max_ppm * max_length
                canvas.coords(smoke_bar, 1038, 595, 1038 + bar_length, 599)

            elif "Aktifkan Exhaust Fan" in line:
                canvas.itemconfig(fan_text, text="  ON")

            elif "Matikan Exhaust Fan" in line:
                canvas.itemconfig(fan_text, text="  OFF")

            elif "Aktifkan WATER SHOWER" in line:
                canvas.itemconfig(shower_text, text="  ON")

            elif "Matikan WATER SHOWER" in line:
                canvas.itemconfig(shower_text, text="  OFF")


            update_graphs()

        except Exception as e:
            print("Serial Error:", e)

# ================== THREADING ==================
serial_thread = threading.Thread(target=read_serial, daemon=True)
serial_thread.start()

window.bind("<Escape>", lambda e: window.quit())
window.resizable(False, False)
window.mainloop()
