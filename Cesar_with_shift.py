
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def encrypt(message, shift_t, shift):
    encrypted = ""
   # message_in_numbers = []
    n = 0
    for letter in message:
        number = (letter_to_index[letter] + (shift_t * n) + shift) % len(letter_to_index)
        n += 1
        letter = index_to_letter[number]
        encrypted += letter


    return encrypted


def decrypt(message, shift_t, shift):
    decrypted = ""

    n = 0
    for letter in message:
        number = (letter_to_index[letter] - ((shift_t * n) + shift)) % len(letter_to_index)
        n += 1
        letter = index_to_letter[number]
        decrypted += letter
    return decrypted


def main():
    message = str(input("Шифруємо слово: "))
    # message = "MISFORTUNE"
    print("Введіть ключ для шифру Цезаря: ")
    k = [int(input()) for x in range(2)]

    # print(K)
    # K = np.matrix([[3, 3], [2, 5]])

    encrypted_message = encrypt(message, k[0], k[1])
    decrypted_message = decrypt(encrypted_message, k[0], k[1])

    print("Початок шифрування: " + message)
    print("Зашифроване повідомлення: " + encrypted_message)
    print("Розшифроване повідомлення: " + decrypted_message)


main()
