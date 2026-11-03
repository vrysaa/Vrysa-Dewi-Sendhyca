
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


# Membuat daftar pesan
messages = [
    "Halo, apa kabar?",
    "Selamat belajar Python!",
    "Jangan menyerah untuk belajar.",
    "Semangat yaa!"
]

sent_messages = []

# Memanggil fungsi dengan salinan daftar
send_messages(messages[:], sent_messages)

# Mencetak kedua daftar
print("\nDaftar messages asli:")
print(messages)

print("\nDaftar sent_messages:")
print(sent_messages)