alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def encrypt(message, keyword, shift):
    encrypted = ""
    alphabet_for_encrypt = ["." for i in range(len(alphabet))]

    for i in range(len(keyword)):
        alphabet_for_encrypt[(shift + i) % len(alphabet_for_encrypt)] = keyword[i]

    index_to_letter_temp = {k: v for k, v in index_to_letter.items() if v not in keyword}

    i = 0
    for j in index_to_letter_temp:
        alphabet_for_encrypt[(shift + len(keyword) + i) % len(alphabet_for_encrypt)] = index_to_letter_temp[j]
        i += 1
    # print(index_to_letter.items())
    # print("Алфавіт для шифрування: ", alphabet_for_encrypt)
    for i in range(len(message)):
        for j in range(len(index_to_letter)):
            if message[i] == index_to_letter[j]:
                encrypted += alphabet_for_encrypt[j]

    return encrypted


def decrypt(message, keyword, shift):
    decrypted = ""

    alphabet_for_decrypt = ["." for i in range(len(alphabet))]

    for i in range(len(keyword)):
        alphabet_for_decrypt[(shift + i) % len(alphabet_for_decrypt)] = keyword[i]

    index_to_letter_temp = {k: v for k, v in index_to_letter.items() if v not in keyword}

    i = 0
    for j in index_to_letter_temp:
        alphabet_for_decrypt[(shift + len(keyword) + i) % len(alphabet_for_decrypt)] = index_to_letter_temp[j]
        i += 1
    # print(index_to_letter.items())
    # print("Алфавіт для розшифрування: ", alphabet_for_decrypt)

    for i in range(len(message)):
        for j in range(len(index_to_letter)):
            if message[i] == alphabet_for_decrypt[j]:
                decrypted += index_to_letter[j]

    return decrypted


def main():
    var = input("Якщо шифруємо то введіть C якщо розшифровуємо то введіть D \n")
    if var == 'C':
        message = str(input("Шифруємо слово: "))
        print("Введіть ключ для шифру Цезаря: ")
        k = int(input("k = "))
        print("Та введіть ключове слово: ")
        keyword = input("keyword = ")
        encrypted_message = encrypt(message, keyword, k)
        print("Початок шифрування: " + message)
        print("Зашифроване повідомлення: " + encrypted_message)
    elif var == 'D':
        message = str(input("Розшифруємо слово: "))
        print("Введіть ключ для шифру Цезаря: ")
        k = int(input("k = "))
        print("Та введіть ключове слово: ")
        keyword = input("keyword = ")
        decrypted_message = decrypt(message, keyword, k)
        print("Початок шифрування: " + message)
        print("Розшифроване повідомлення: " + decrypted_message)
    else:
        message = "BRUHH BAD INPUT"
        keyword = "MISFORTUNE"
        k = 5
        print("Початок шифрування: " + message)
        encrypted_message = encrypt(message, keyword, k)
        decrypted_message = decrypt(encrypted_message, keyword, k)
        print("Зашифроване повідомлення: " + encrypted_message)
        print("Розшифроване повідомлення: " + decrypted_message)






main()
