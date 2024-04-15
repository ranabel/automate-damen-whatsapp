import pywhatkit as pw
import csv

with open("factdata.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    for row in reader:
        number = row[0]
        name = row[1]
        msg = f"Selamat Malam {name}!\nNice Dream :)\n<3"
        pw.sendwhatmsg_instantly(number, msg, 30, True, 10)  # Kirim pesan instan