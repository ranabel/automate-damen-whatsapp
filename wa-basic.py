import pywhatkit

# Send message to a contact
phone_number = input("Enter phone number: ")

# pywhatkit.sendwhatmsg("nomor", "isi", jam, menit, detik)
pywhatkit.sendwhatmsg(phone_number, "Test", 20, 31)
pywhatkit.sendwhatmsg(phone_number, "Test", 7, 25, 15, True, 2)

# Send message to a group
group_id = input("Enter group id: ")

pywhatkit.sendwhatmsg_to_group(group_id, "Test Group", 7, 31)


