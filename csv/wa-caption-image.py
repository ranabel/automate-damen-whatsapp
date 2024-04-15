import pywhatkit as pw
import csv

img = 'image.png' 

with open("factdata.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    for row in reader:
        number = row[0]
        name = row[1]

        msg = f"Selamat Malam {name}!\nNice Dream :)\n<3"

        pw.sendwhats_image(number, img, caption=msg, tab_close=True, wait_time=13)  