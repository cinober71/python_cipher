"""
@senko
Programmed by Adam Yusenko
*  2021-09-20 Initial programming
"""

alphabet_ua = u"АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"


def work(message, k, op):
    k *= len(message) // len(k) + 1
    message = message.upper()
    return ''.join([alphabet_ua[alphabet_ua.index(j) + int(k[i]) * op] for i, j in enumerate(message)])


def encrypt(message, key):
    return work(message, key, 1)


def decrypt(message, key):
    return work(message, key, -1)


def main():
    print("Шифр Гронсфельда")

    var = input("Якщо шифруємо то введіть C якщо розшифровуємо то введіть D \n")
    if var == 'C':
        message = str(input("Шифруємо слово: "))
        print("Введіть ключ для шифру Гронсфельда з 5 цифр: ")
        k = [(input("k = ")) for i in range(5)]
        encrypted_message = encrypt(message,  k)
        print("Початок шифрування: " + message)
        print("Зашифроване повідомлення: " + encrypted_message)
    elif var == 'D':
        message = str(input("Розшифруємо слово: "))
        print("Введіть ключ для шифру Гронсфельда з 5 цифр: ")
        k = [(input("k = ")) for i in range(5)]
        decrypted_message = decrypt(message, k)
        print("Початок шифрування: " + message)
        print("Розшифроване повідомлення: " + decrypted_message)
    else:
        message = "BRUHH BAD INPUT"
        keyword = "MISFORTUNE"
        k = [1, 2, 3, 4, 5]
        print("Початок шифрування: " + message)
        encrypted_message = encrypt(message, k)
        decrypted_message = decrypt(encrypted_message, k)
        print("Зашифроване повідомлення: " + encrypted_message)
        print("Розшифроване повідомлення: " + decrypted_message)


main()
