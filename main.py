
strings = ["a", "b", "c", "d", "e", "f", "g", "h",
           "i", "j", "k", "l", "m", "n", "o", "p",
           "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
morse = [". _", "_ . . .", "_ . _ .", "_ . .", ".", ". . _ .", "_ _ .", ". . . .",
         ". .", ". _ _ _", "_ . _", ". _ . .", "_ _", "_ .", "_ _ _", ". _ _ .",
         "_ _ . _", ". _ .", ". . .", "_", ". . _", ". . . _", ". _ _", "_ . . _", "_ . _ _", "_ _ . ."]

convert = input("Type the text to convert ").lower()

splitted = [*convert]

for item in splitted:
    if item in strings:
        location = strings.index(item)
        print(morse[location])




