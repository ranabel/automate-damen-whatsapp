import pywhatkit as pw
import csv

img = 'image.png'  # Ganti dengan path gambar Anda

with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    for row in reader:
        number = row[0]
        name = row[1]

        msg = f"Selamat Malam {name}!\nNice Dream :)\n<3"

        # pw.sendwhatmsg_instantly(number, msg, 30, True, 10)  # Kirim pesan instan
         # disini caption image merupakan pesan yang ingin kita kirimkan
        pw.sendwhats_image(number, img, caption=msg, tab_close=True, wait_time=30)
