from pathlib import Path
from tkinter import Tk, Canvas, Text, Button, PhotoImage
import serial
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import deque
import time
import subprocess
import requests
import datetime
import math
import cv2
from PIL import Image, ImageTk


SERVER_URL = "http://localhost:3000/sensor"

def push_to_server(**kwargs):
    try:
        requests.post(SERVER_URL, json=kwargs, timeout=0.2)
    except requests.exceptions.RequestException:
        pass     

# GANTI dengan token & chat ID milikmu
bot_token = '7912234203:AAG731XH8NOTCLTgOizmRmGErqUSYpRAo4Q'
chat_id = '7753137443'
video_path = "Video_terdeteksi.avi"

ser = serial.serial_for_url('rfc2217://localhost:4000', baudrate=115200)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\gui\Projek\assets\frame0\Web-New")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.attributes('-fullscreen', True)
window.configure(bg = "#2A2A2A")


canvas = Canvas(
    window,
    bg = "#2A2A2A",
    height = 1080,
    width = 1980,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
# Fungsi untuk center canvas di fullscreen
def center_canvas():
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_offset = (screen_width - 1980) // 2
    y_offset = (screen_height - 1080) // 2
    canvas.place(x=x_offset, y=y_offset)

window.after(100, center_canvas)

canvas.place(x = 0, y = 0)

def update_clock():
    now = datetime.datetime.now()
    time_str = now.strftime("%I:%M %p")      # 12-hour format with AM/PM
    date_str = now.strftime("  %A\n%d-%m-%Y")  # Example: Monday\n31-05-2025

    canvas.itemconfig(clock_text, text=time_str)
    canvas.itemconfig(date_text, text=date_str)
    window.after(1000, update_clock)  # Update setiap 1 detik

import math

def draw_clock():
    clock_canvas.delete("all")
    # Lingkaran jam
    clock_canvas.create_oval(10, 10, 160, 160, fill="#1f1f1f", outline="white", width=2)

    # Titik tengah
    clock_canvas.create_oval(83, 83, 87, 87, fill="white")

    now = datetime.datetime.now()
    sec = now.second
    minute = now.minute
    hour = now.hour % 12 + minute / 60

    # Hitung sudut
    sec_angle = math.radians(6 * sec - 90)
    min_angle = math.radians(6 * minute - 90)
    hour_angle = math.radians(30 * hour - 90)

    # Hitung koordinat ujung jarum
    sec_x = 85 + 55 * math.cos(sec_angle)
    sec_y = 85 + 55 * math.sin(sec_angle)
    min_x = 85 + 45 * math.cos(min_angle)
    min_y = 85 + 45 * math.sin(min_angle)
    hour_x = 85 + 30 * math.cos(hour_angle)
    hour_y = 85 + 30 * math.sin(hour_angle)

    # Gambar jarum
    clock_canvas.create_line(85, 85, hour_x, hour_y, width=4, fill="white")
    clock_canvas.create_line(85, 85, min_x, min_y, width=3, fill="cyan")
    clock_canvas.create_line(85, 85, sec_x, sec_y, width=2, fill="red")

def update_analog_clock():
    draw_clock()
    window.after(1000, update_analog_clock)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    879.0,
    229.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    879.0,
    599.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1589.0,
    366.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    1589.0,
    851.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    280.0,
    98.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    1412.0,
    738.0,
    image=image_image_6
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    1424.0,
    95.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    384.0,
    255.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    177.0,
    255.0,
    image=image_image_11
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    384.0,
    453.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    176.0,
    453.0,
    image=image_image_14
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    280.0,
    788.0,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    879.0,
    902.0,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    675.0,
    889.0,
    image=image_image_18
)

clock_text = canvas.create_text(
    215.0,
    828.0,
    anchor="nw",
    text="00:00 AM",
    fill="#FFFFFF",
    font=("Inter ExtraBoldItalic", 30 * -1)
)

date_text = canvas.create_text(
    190.0,
    870.0,
    anchor="nw",
    text="Monday\n31-5-2025",
    fill="#FFFFFF",
    font=("Inter ExtraBoldItalic", 34 * -1)
)

# ========== TEXTBOX LOG ========== 
log_textbox = Text(
    window,
    fg="#FFFFFF",
    bg="#000000",
    font=("Courier", 12),
    wrap="word"
)
log_textbox.place(
    x=1300,
    y=760,
    width=window.winfo_screenwidth() - 1400,  # Sesuaikan dengan lebar layar
    height=window.winfo_screenheight() - 870  # Sesuaikan dengan tinggi layar
)

clock_canvas = Canvas(window, width=170, height=170, bg="#000000", highlightthickness=0)
clock_canvas.place(x=167, y=630)  # Sesuaikan posisi di kotak hijau

# ================== TEXT YANG DIUPDATE ==================
gas_text = canvas.create_text(163.0, 312.0, anchor="nw", text="213", fill="#DCDCDC", font=("Inter MediumItalic", 15 * -1))
smoke_text = canvas.create_text(370.0, 313.0, anchor="nw", text="102", fill="#DCDCDC", font=("Inter MediumItalic", 15 * -1))
shower_text = canvas.create_text(163.0, 511.0, anchor="nw", text="OFF", fill="#DCDCDC", font=("Inter SemiBoldItalic", 15 * -1))
fan_text = canvas.create_text(370.0, 510.0, anchor="nw", text="OFF", fill="#DCDCDC", font=("Inter SemiBoldItalic", 15 * -1))
# ================== BARGRAPH ==================
# Bargraph untuk Gas
gas_bar = canvas.create_rectangle(550, 865, 550 + 1, 885, fill="blue", outline="")
# Bargraph untuk Smoke
smoke_bar = canvas.create_rectangle(550, 950, 550 + 1, 970, fill="red", outline="")

# Circular bargraph GAS
gas_circle = canvas.create_arc(130, 190, 220, 280, start=90, extent=0, outline="blue", width=12, style='arc')
# Circular bargraph SMOKE
smoke_circle = canvas.create_arc(340, 190, 430, 280, start=90, extent=0, outline="green", width=12, style='arc')

# bargraph circle
max_ppm = 1000
max_length = 200

video_running = False
recording = False
cap = None
video_writer = None
video_label = None

def start_camera():
    global cap, video_running, video_label, recording, video_writer

    if video_running:
        return

    cap = cv2.VideoCapture(0)
    video_writer = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'XVID'), 20.0, (850, 616))
    video_running = True
    recording = True
    video_label = canvas.create_image(482, 448, image=None)

    def update_frame():
        global recording
        if not video_running:
            return

        ret, frame = cap.read()
        if ret:
            frame_resized = cv2.resize(frame, (850, 616))
            rgb_frame = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
            imgtk = ImageTk.PhotoImage(image=Image.fromarray(rgb_frame))
            canvas.itemconfig(video_label, image=imgtk)
            canvas.image = imgtk

            if recording:
                video_writer.write(frame_resized)

        window.after(30, update_frame)

    update_frame()

def stop_camera():
    global cap, video_running, recording, video_writer
    if video_running:
        video_running = False
        recording = False
        if cap:
            cap.release()
        if video_writer:
            video_writer.release()
        canvas.itemconfig(video_label, image=None)
        send_video_telegram(video_path)

def send_video_telegram(file_path):
    url = f"https://api.telegram.org/bot{bot_token}/sendVideo"
    with open(file_path, 'rb') as video_file:
        files = {'video': video_file}
        data = {'chat_id': chat_id, 'caption': 'Rekaman deteksi gas/asap'}
        response = requests.post(url, files=files, data=data)
        print("Telegram response:", response.status_code)

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

fig1, ax1 = plt.subplots(figsize=(7.2, 2.7), dpi=100)
fig2, ax2 = plt.subplots(figsize=(7.2, 2.7), dpi=100)

canvas_gas = FigureCanvasTkAgg(fig1, master=window)
canvas_gas.get_tk_widget().place(x=490, y=90)

canvas_smoke = FigureCanvasTkAgg(fig2, master=window)
canvas_smoke.get_tk_widget().place(x=490, y=455)

def init_graphs():
    # Set background figure dan axes ke hitam
    fig1.patch.set_facecolor('black')
    fig2.patch.set_facecolor('black')
    ax1.set_facecolor('green')
    ax2.set_facecolor('green')

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
            timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
            log_textbox.insert("end", timestamp + line + "\n")
            log_textbox.see("end")

            if line.startswith("GAS:"):
                gas_val = int(line.split(":")[1].strip())
                canvas.itemconfig(gas_text, text=f"{gas_val}")
                gas_data.append(gas_val)
                time_data.append(now)

                # Update bargraph horizontal
                bar_length = min(gas_val, max_ppm) / max_ppm * max_length
                canvas.coords(gas_bar, 550, 865, 550 + bar_length, 885)

                # Update circular bargraph (extent)
                gas_extent = min(gas_val, max_ppm) / max_ppm * 360
                canvas.itemconfig(gas_circle, extent=gas_extent)
                push_to_server(gas=gas_val)



            elif line.startswith("SMOKE:"):
                smoke_val = int(line.split(":")[1].strip())
                canvas.itemconfig(smoke_text, text=f"{smoke_val}")
                smoke_data.append(smoke_val)

                bar_length = min(smoke_val, max_ppm) / max_ppm * max_length
                canvas.coords(smoke_bar, 550, 950, 550 + bar_length, 970)

                # Update circular bargraph (extent)
                smoke_extent = min(smoke_val, max_ppm) / max_ppm * 360
                canvas.itemconfig(smoke_circle, extent=smoke_extent)
                push_to_server(smoke=smoke_val)



            elif "Aktifkan Exhaust Fan" in line:
                canvas.itemconfig(fan_text, text="ON")
                start_camera()
                push_to_server(fan="ON")
            elif "Matikan Exhaust Fan" in line:
                canvas.itemconfig(fan_text, text="OFF")
                stop_camera()
                start_camera()
                push_to_server(fan="OFF")
            elif "Aktifkan WATER SHOWER" in line:
                canvas.itemconfig(shower_text, text="ON")
                start_camera()
                push_to_server(pump="ON")
            elif "Matikan WATER SHOWER" in line:
                canvas.itemconfig(shower_text, text="OFF")
                stop_camera()
                start_camera()
                push_to_server(pump="OFF")


            update_graphs()

        except Exception as e:
            print("Serial Error:", e)

# ================== THREADING ==================
serial_thread = threading.Thread(target=read_serial, daemon=True)
serial_thread.start()

start_camera()
update_analog_clock()
update_clock()
window.bind("<Escape>", lambda e: window.quit())
window.resizable(False, False)
window.mainloop()