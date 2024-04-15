import pywhatkit as pw
import phonenumbers
import csv

with open("factdata.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for number, name in reader:
            if phonenumbers.is_valid_number(phonenumbers.parse(number)):
                msg = '''\
Halo {name}!
Btw, knp kasur magnetnya besar?

Salam,
:').
'''.format(name=name)
                pw.sendwhatmsg_instantly(number, msg, 30, True, 10)
            else:
                print(f"Nomor tidak valid: {number}")