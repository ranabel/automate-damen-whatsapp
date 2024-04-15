import pywhatkit as pw

try:
    with open("C:/Users/Abel/.vscode/damen/stafli/damen-whatsapp/list_number.txt", "r", encoding="utf-8") as f_num, \
         open("C:/Users/Abel/.vscode/damen/stafli/damen-whatsapp/list_name.txt", "r", encoding="utf-8") as f_name, \
         open("C:/Users/Abel/.vscode/damen/stafli/damen-whatsapp/list_sum.txt", "r", encoding="utf-8") as f_sum:

        for name, number, sum_value in zip(f_name, f_num, f_sum):
            name = name.strip()
            number = '+' + number.strip()
            sum_value = sum_value.strip()

            msg = '''\
Halo {nama}!
Coba lagi 15s (ni ganti aja kalo ada yg keskip)
Btw, knp kasur magnetnya besar?

Salam, tes jumlah {sum}
Kucing
            '''.format(nama=name, sum=sum_value)

            pw.sendwhatmsg_instantly(number, msg, 15, True, 5)

except FileNotFoundError:
    print("One or both of the text files are not found.")

except Exception as e:
    print("An error occurred:", str(e))