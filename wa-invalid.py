import pywhatkit as pw
import phonenumbers
import csv

with open("data.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for number, name in reader:
            if phonenumbers.is_valid_number(phonenumbers.parse(number)):
                msg = '''\
Halo {name}!
Btw, knp kasur magnetnya besar?
Karena kalo magnetnya gada itu kita :>
<yap alias gabisa nyatu kak>

Salam,
:').
'''.format(name=name)
                pw.sendwhatmsg_instantly(number, msg, 10, True, 5)
            else:
                print(f"Nomor tidak valid: {number}")