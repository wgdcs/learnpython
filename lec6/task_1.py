# capitalize()
txt = "original string"
x = txt.capitalize()
# выводим название тестируемого метода
print("capitalize()")
# выводим результат работы метода
print(x)
# после вывода результата работы каждого метода
# добавляем вывод пустой строки, чтобы отделять
# результаты друг от друга
print()

# casefold()
txt = "My Original String"
x = txt.casefold()
print("casefold()")
print(x)
print()

# center()
txt = "my string"
x = txt.center(50)
# в конце строки добавляем точку, чтобы видеть,
# где заканчивается новая строка
print("center()")
print(x + ".")
print()

# count()
txt = '''Whether you use After Effects to animate a simple
video title sequence of to create complex special effects,
you generallly follow the same basic workflow.
The After Effects interface facilitates you work and adapts
to each stage of production'''
value = "ffects"
x = txt.count(value)
print("count()")
print(x)
print()

# encode()
x = txt.encode()
print("encode() english")
print(x)
print()

txt = "текст на русском языке"
x = txt.encode()
print("encode() russian")
print(x)
print()

# endswith()
txt = "Continue learning Python."
x = txt.endswith("n.")
print("endswith()")
print (x)
x = txt.endswith("n")
print (x)
print()

# expandtabs()
txt = "P\ty\tt\th\to\tn"
x = txt.expandtabs(2)
print("expandtabs()")
print(x)
print()

# find()
txt = '''Whether you use After Effects to animate a simple
video title sequence of to create complex special effects,
you generallly follow the same basic workflow.
The After Effects interface facilitates you work and adapts
to each stage of production'''
value = "ffects"
x = txt.find(value)
print("find()")
print(x)
value = "Microsoft"
x = txt.find(value)
print(x)
print()

# format()
txt = "You won {won:.2f} dollars!"
print("format()")
print(txt.format(won = 1000))
# помещаем форматируемый текст в одинарные кавычки,
# чтобы результат форматирования был более заметен
txt = "You won '{won:>8}' dollars!"
print(txt.format(won = 1000))
txt = "You won '{won:<8}' dollars!"
print(txt.format(won = 1000))
txt = "You won '{won:^8}' dollars!"
print(txt.format(won = 1000))
print()

# index()
txt = '''Whether you use After Effects to animate a simple
video title sequence of to create complex special effects,
you generallly follow the same basic workflow.
The After Effects interface facilitates you work and adapts
to each stage of production'''
value = "ffects"
x = txt.index(value)
print("index()")
print(x)
print()

# isalnum()
txt = "catch22"
x = txt.isalnum()
print("isalnum")
print(x)
txt = "omg&34@"
x = txt.isalnum()
print(x)
print()

# isalpha()
txt = "catch22"
x = txt.isalpha()
print("isalpha()")
print(x)
txt = "Adobe"
x = txt.isalpha()
print(x)
print()

# isdecimal()
txt = "1234567890"
x = txt.isdecimal()
print("isdecimal()")
print(x)
txt = "catch22"
x = txt.isdecimal()
print(x)
txt = "\u00B2" #unicode for ²
x = txt.isdecimal()
print(x)
print()

# isdigit()
txt = "1234567890"
x = txt.isdigit()
print("isdecimal()")
print(x)
txt = "catch22"
x = txt.isdigit()
print(x)
txt = "\u00B2" #unicode for ²
x = txt.isdigit()
print(x)
print()

# isidentifier()
txt1 = "myFileName"
txt2 = "my file name"
txt3 = "myFileName3"
txt4 = "my_file_name"
txt5 = "2myFileName"
print("isidentifier()")
print(txt1 + ":\t" + (str)(txt1.isidentifier()))
print(txt2 + ":\t" + (str)(txt2.isidentifier()))
print(txt3 + ":\t" + (str)(txt3.isidentifier()))
print(txt4 + ":\t" + (str)(txt4.isidentifier()))
print(txt5 + ":\t" + (str)(txt5.isidentifier()))
print()

# islower()
txt1 = "myFileName"
txt2 = "my_file_name"
txt3 = "myfilename"
print(txt1 + ":\t" + (str)(txt1.islower()))
print(txt2 + ":\t" + (str)(txt2.islower()))
print(txt3 + ":\t" + (str)(txt3.islower()))
print()

# isnumeric()
txt1 = "01234"
txt2 = "-12"
txt3 = "cat22"
txt4 = "1.48"
print("isnumeric()")
print(txt1 + ":\t" + (str)(txt1.isnumeric()))
print(txt2 + ":\t" + (str)(txt2.isnumeric()))
print(txt3 + ":\t" + (str)(txt3.isnumeric()))
print(txt4 + ":\t" + (str)(txt4.isnumeric()))
print()

# isprintable()
txt1 = "The name's Bond. James Bond."
txt2 = "The name's Bond.\tJames Bond."
txt3 = "The name's Bond.\nJames Bond."
print("isprintable()")
print(txt1 + ":\t" + (str)(txt1.isprintable()))
print(txt2 + ":\t" + (str)(txt2.isprintable()))
print(txt3 + ":\t" + (str)(txt3.isprintable()))
print()

# iswhitespace()
txt1 = "The name's Bond. James Bond."
txt2 = "    "
print("iswhitespace()")
print(txt1 + ":\t" + (str)(txt1.isspace()))
print(txt2 + ":\t" + (str)(txt2.isspace()))
print()

# istitle()
txt1 = "The Main Title, Really"
txt2 = "The main title, really"
print("istitle()")
print(txt1 + ":\t" + (str)(txt1.istitle()))
print(txt2 + ":\t" + (str)(txt2.istitle()))
print()

# isupper()
txt1 = "THIS STRING IS IN UPPER CASE"
txt2 = "This string is another one"
print("isupper()")
print(txt1 + ":\t" + (str)(txt1.isupper()))
print(txt2 + ":\t" + (str)(txt2.isupper()))
print()

# join()
myTuple = ("January", "February", "March")
myDict = {"January": "Spartan Race", "February": "Dyka Gonka", "March": "Race Nation" }
print("join()")
print("#".join(myTuple))
print("@".join(myDict))
print()

# ljust()
txt = "My text"
print("ljust()")
print(txt.ljust(20) + "End.")
print()

# lower()
txt = "This String has some UPPER CASE characters"
print("lower()")
print(txt.lower())
print()
