import pywhatkit as pw
import csv

# Buka file CSV
with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    # Kirim pesan dan gambar ke setiap kontak
    for row in reader:
        number = row[0]
        name = row[1]

        msg = f"Selamat Malam {name}!\nNice Dream :)\n<3"

        pw.sendwhatmsg_instantly(number, msg, 20, True, 5)  # Kirim pesan instan
