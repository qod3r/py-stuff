letters = {
    "й": "j",
    "ц": "c",
    "у": "u",
    "к": "k",
    "е": "e",
    "н": "n",
    "г": "g",
    "ш": "sh",
    "щ": "shh",
    "з": "z",
    "х": "h",
    "ъ": "#",
    "ф": "f",
    "ы": "y",
    "в": "v",
    "а": "a",
    "п": "p",
    "р": "r",
    "о": "o",
    "л": "l",
    "д": "d",
    "ж": "zh",
    "э": "je",
    "я": "ya",
    "ч": "ch",
    "с": "s",
    "м": "m",
    "и": "i",
    "т": "t",
    "ь": "'",
    "б": "b",
    "ю": "ju",
    "ё": "jo"
}
# {cyr: lat}

with open("cyrillic.txt", 'r') as inp, open("translit.txt", 'w') as out:
    for line in inp:
        for letter in line:
            if letter.lower() in letters.keys():
                if letter.isupper():
                    if len(letters[letter.lower()]) > 1:
                        letter = letters[letter.lower()][0].upper() + letters[letter.lower()][1:]
                    else:
                        letter = letters[letter.lower()].upper()
                else:
                    letter = letters[letter]
            out.write(letter)