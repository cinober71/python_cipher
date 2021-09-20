"""
@senko
Programmed by Adam Yusenko
*  2021-09-20 Initial programming
"""
print("ЗІ Ключове слово ЮСЕНКО_АДАМ.\n")
text = input('Введите текст для шифрования : ')
alphabet_ua = u"АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ ."


def Trisemus(key_word, strvalue, action):
    keyword, (height, width) = key_word
    doEncode = True if action == "encd" else False
    doDecode = True if action == "decd" else False

    start_pos = 0
    table = [['.' for x in range(width)] for y in range(height)]
   # print(table)
    temp_char = {}
    for i in keyword + alphabet_ua:
        if temp_char.get(i) is None:
            temp_char[i] = start_pos
            table[int(start_pos / width)][int(start_pos % width)] = i
            start_pos += 1
            if start_pos >= width * height:
                break
    print(table)
    result = ""
    for i in strvalue:
        start_pos = temp_char.get(i)
        if start_pos is not None:
            x = start_pos % width
            if doEncode:
                y = (start_pos / width + 1) % height
            elif doDecode:
                y = (start_pos / width - 1 + height) % height
            else:
                y = start_pos / width % height
            result += table[int(y)][int(x)]
        else:
            result += i
    return result


#keyword = u"ЮСЕНКОАДАМ"
keyword = input("Ключове слово:(ПрізвищеІмя) ")
tablesize = (4, 8)

key = (keyword, tablesize)
print("Key = " + str(key))

print("Шифруємо: ", text)
c = Trisemus(key, text, "encd")
print(c)
d = Trisemus(key, c, "decd")
print("DECODE", d)
