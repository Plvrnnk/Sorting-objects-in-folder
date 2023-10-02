def normalize(some_string):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "c", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
    NUMBERS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '.')
    TRANS = {}
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()    
    
    def translate(name):
        name = name.translate(TRANS)
        return name
    
    some_string = translate(some_string)
    
    for val in some_string:
        if (not val in CYRILLIC_SYMBOLS) and (not val in TRANSLATION) and (not val in NUMBERS):
            some_string = some_string.replace(val, '_')
            
    return some_string   
    
