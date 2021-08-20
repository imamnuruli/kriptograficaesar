ascii_uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                   "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
ascii_lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                   "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
vokal = ["a", "A", "i", "I", "u", "U", "e", "E", "o", "O"]
tipe = []  # bentuk list global pak


def enkripsi(input_text):
    hasil = ""
    if input_text.isalnum() or " " in input_text:
        None
    else:
        raise NameError
    for huruf in input_text:
        if huruf == " ":
            hasil += huruf
            tipe.append(' ')

        elif huruf in vokal and huruf.isupper():
            pos = ascii_uppercase.index(huruf) - 3
            if pos <= 0:  # misal pos = -2
                pos = 26 + pos  # 26 - 2
                pos = ascii_uppercase[pos]
                tipe.append('v')
            else:
                pos = ascii_uppercase[pos]
                tipe.append('v')
            hasil += pos

        elif huruf in vokal and huruf.islower():
            # sesuai soal pak vokal -3 konsonan +5
            pos = ascii_lowercase.index(huruf) - 3
            if pos <= 0:
                pos = 26 + pos
                pos = ascii_lowercase[pos]
                tipe.append('v')
            else:
                pos = ascii_lowercase[pos]
                tipe.append('v')
            hasil += pos
        elif huruf.islower():
            pos = ascii_lowercase.index(huruf) + 5  # konsonan
            if pos >= 26:
                pos = pos - 26
                pos = ascii_lowercase[pos]
                tipe.append('k')
            else:  # jika value atau nilai tidak melewati 26
                pos = ascii_lowercase[pos]
                tipe.append('k')
            hasil += pos
        elif huruf.isupper():
            pos = ascii_uppercase.index(huruf) + 5
            if pos >= 26:
                pos = pos - 26
                pos = ascii_uppercase[pos]
                tipe.append('k')
            else:
                pos = ascii_uppercase[pos]
                tipe.append('k')
            hasil += pos

    return hasil


def dekripsi(input_text):
    hasil = ""

    for huruf in input_text:
        if huruf == " ":
            hasil += huruf
        elif tipe[input_text.index(huruf)] == "v" and huruf.isupper():
            pos = ascii_uppercase.index(huruf) + 3
            if pos >= 26:
                pos = pos - 26
                pos = ascii_uppercase[pos]
            else:
                pos = ascii_uppercase[pos]
            hasil += pos

        elif tipe[input_text.index(huruf)] == "v" and huruf.islower():
            pos = ascii_lowercase.index(huruf) + 3
            if pos >= 26:
                pos = pos - 26
                pos = ascii_lowercase[pos]
            else:
                pos = ascii_lowercase[pos]
            hasil += pos
        elif tipe[input_text.index(huruf)] == "k" and huruf.islower():
            pos = ascii_lowercase.index(huruf) - 5
            if pos <= 0:
                pos = 26 + pos
                pos = ascii_lowercase[pos]
            else:
                pos = ascii_lowercase[pos]
            hasil += pos
        elif tipe[input_text.index(huruf)] == "k" and huruf.isupper():
            pos = ascii_uppercase.index(huruf) - 5
            if pos <= 0:
                pos = 26 + pos
                pos = ascii_uppercase[pos]
            else:
                pos = ascii_uppercase[pos]
            hasil += pos

    return hasil
