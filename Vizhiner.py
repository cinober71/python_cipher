"""
@senko
Programmed by Adam Yusenko
*  2021-09-20 Initial programming
"""

alphabet_ua = u"АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"

letter_to_index = dict(zip(alphabet_ua, range(len(alphabet_ua))))
index_to_letter = dict(zip(range(len(alphabet_ua)), alphabet_ua))


def encode_mess(message):
    list_code = []
    for i in range(len(message)):
        for j in index_to_letter:
            if message[i] == index_to_letter[j]:
                list_code.append(j)
    return list_code


def encrypt(message, keyword):
    encrypted = ""
    lі = encode_mess(keyword)
    list_keyword = [lі[i % len(lі)] for i in range(len(message))]
    list_message = encode_mess(message)
    for i in range(len(list_message)):
        tmp = (list_message[i] + list_keyword[i]) % len(alphabet_ua)
        encrypted += index_to_letter[tmp]

    return encrypted


def decrypt(message, keyword):
    decrypted = ""
    lі = encode_mess(keyword)
    list_keyword = [lі[i % len(lі)] for i in range(len(message))]
    list_message = encode_mess(message)
    for i in range(len(list_message)):
        tmp = (list_message[i] - list_keyword[i]+len(alphabet_ua)) % len(alphabet_ua)
        decrypted += index_to_letter[tmp]
    return decrypted


def main():
    print("Шифр Віжинера")
    var = input("Якщо шифруємо то введіть C якщо розшифровуємо то введіть D \n")
    if var == 'C':
        message = str(input("Шифруємо слово: "))
        print("Введіть слово - ключ для шифру Віжинера : ")
        keyword = input("keyword = ")
        encrypted_message = encrypt(message, keyword)
        print("Початок шифрування: " + message)
        print("Зашифроване повідомлення: " + encrypted_message)
    elif var == 'D':
        message = str(input("Розшифруємо слово: "))
        print("Введіть слово - ключ для шифру Віжинера : ")
        keyword = input("keyword = ")
        decrypted_message = decrypt(message, keyword)
        print("Початок шифрування: " + message)
        print("Розшифроване повідомлення: " + decrypted_message)
    else:
        message = "ОЙ ЩОСТЬ ПІШЛО НЕ ТАК"
        keyword = "НЕВДАЧА"
        print("Початок шифрування: " + message)
        encrypted_message = encrypt(message, keyword)
        decrypted_message = decrypt(encrypted_message, keyword)
        print("Зашифроване повідомлення: " + encrypted_message)
        print("Розшифроване повідомлення: " + decrypted_message)


main()
