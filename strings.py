linebreak = "------------------------"
# This is just to separate each section in the terminal

# ------------------------ <-- just to make the code look nice when reading out of the terminal

print(linebreak)
# ------------------------

print("capitalize()")
print("Converts the first character to uppercase.")

a = "hello"

print(a.capitalize())

print(linebreak)
# ------------------------

print("casefold()")
print("Converts string into lowercase.")

b = "HELLO"

print(b.casefold())

print(linebreak)
# ------------------------

print("center()")
print("Returns a centered string.")

c = "Hello"
c2 = c.center(20, "/")

print(c2)

print(linebreak)
# ------------------------

print("count()")
print("Returns the number of times a specified value occurs in a string.")

d = "123451"

print(d.count("1"))

print(linebreak)
# ------------------------

print("encode()")
print("Returns an encoded version of the string.")

e = "Hellö"
e2 = e.encode()

print(e2)

print(linebreak)
# ------------------------

print("endswith()")
print("Returns True if the string ends with a specified value.")

f = "Hello"
print(f.endswith("o"))

print(linebreak)
# ------------------------

print("expandtabs()")
print("Sets the tab size of the string.")

g = "H\te\tl\tl\to"
g2 =  g.expandtabs(2)

print(g2)

print(linebreak)
# ------------------------

print("find()")
print("Searches the string for a specified value and returns the position of where it was found. Remember, it will be zero indexed and also count spaces!")

h = "Hello world!"

print(h.find("!"))

print(linebreak)
# ------------------------

print("format()")
print("Formats specified values in a string.")

i = format(0.5, '%')

print(i)

print(linebreak)
# ------------------------

print("format_map()")
print("Used to return a dictionary key’s value.")

j = {'x':'Demi', 'y':'Taylor'}

print("{x}'s last name is {y}".format_map(j))

print(linebreak)
# ------------------------

print("index()")
print("Searches the string for a specified value and returns the position of where it was found. Remember this will be zero indexed.")

k = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(k.index("M"))

print(linebreak)
# ------------------------

print("isalnum()")
print("Returns True if all characters in a string are alphanumeric.")

l = "password1234"

print(l.isalnum())

print(linebreak)
# ------------------------

print("isalpha()")
print("Returns True if all characters in a string are in an alphabet.")

m = "Hello"

print(m.isalpha())

print(linebreak)
# ------------------------

print("isdecimal()")
print("Returns True if all characters in a string are decimals.")

n = "333"

print(n.isdecimal())

print(linebreak)
# ------------------------

print("isdigit()")
print("Returns True if all characters in a string are digits.")

o = "1234"

print(o.isdigit())

print(linebreak)
# ------------------------

print("isidentifier()")
print("Returns True if string is an identifier. An identifier cannot contain numbers or a blank space.")

p = "Hello"

print(p.isidentifier())

print(linebreak)
# ------------------------

print("islower()")
print("Returns True if all characters in a string are in lowercase.")

q = "hello"

print(q.islower())

print(linebreak)
# ------------------------

print("isnumeric()")
print("Returns True if all characters in a string are numeric.")

r = "1234"

print(r.isnumeric())

print(linebreak)
# ------------------------

print("isprintable()")
print("Returns True if all characters in a string are printable. Numbers, letters, punctuation characters and spaces are printable.")

s = "My name \n is Demi"

print(s.isprintable())

print(linebreak)
# ------------------------

print("isspace()")
print("Returns True if all characters in a string are white spaces.")

t = " "

print(t.isspace())

print(linebreak)
# ------------------------

print("istitle()")
print("Returns True if the string follows the rule of a title.")

u = "hello world"
u2 = u.title()

print(u2.istitle())

print(linebreak)
# ------------------------

print("isupper()")
print("Returns True if all characters in a string are in uppercase.")

v = "HELLO"

print(v.isupper())

print(linebreak)
# ------------------------

print("join()")
print("Joins the elements of an interable to the end of a string. In the following example it will add '-' in-between each letter as each letter is an example of a string.")

w = "-"
w2 = ("a", "b", "c")

print(w.join(w2))

print(linebreak)
# ------------------------

print("ljust()")
print("Returns a left justified version of the string.")

x = 'pass'
width = 8
fillchar = '*'

print(x.ljust(width, fillchar))

print(linebreak)
# ------------------------

print("lower()")
print("Converts a string into lowercase.")

y = "HELLO"

print(y.lower())

print(linebreak)
# ------------------------

print("lstrip()")
print("Returns a copy of the string in which all chars have been stripped from the beginning of the string (default is whitespace characters).")

z = "8888888..Hello!..8888888"

print(z.lstrip('8'))

print(linebreak)
# ------------------------

print("maketrans()")
print("Returns a translation table to be used in translations. The maketrans() creates a mapping of the character's Unicode ordinal to its corresponding translation. So, the result is 97 ('a') is mapped to '123', 98 'b' to 456 and 99 'c' to 789.")

za= {"a": "123", "b": "456", "c": "789"}
za2 = "abc"
print(za2.maketrans(za))

print(linebreak)
# ------------------------

print("partition()")
print("Returns a tuple where the string is parted into three parts.")

zb = "I love dogs so damn much!"
zb2 = zb.partition("dogs")

print(zb2)

print(linebreak)
# ------------------------

print("replace()")
print("Returns a string where a specified value is replaced with a specified value.")

zc = "I love dogs so much!"

print(zc.replace("dogs", "cats"))

print(linebreak)
# ------------------------

print("rfind()")
print("Searches the string for a specified value and returns the last position where it was found. Remember, this will be zero indexed.")

zd = "12131"

print(zd.rfind("1"))

print(linebreak)
# ------------------------

print("rindex()")
print("Searches the string for a specified value and returns the last position where it was found. Remember, this is zero indexed.")

ze = "ABCDEFA"

print(ze.rindex("A"))

print(linebreak)
# ------------------------

print("rjust()")
print("Returns a right justified version of the string.")

zf = 'word'
width = 8
fillchar = '*'

print(zf.rjust(width, fillchar))

print(linebreak)
# ------------------------

print("rpartition()")
print("Returns a tuple where the string is parted into three parts.")

zg = "I love dogs so damn much!"
zg2 = zg.rpartition("dogs")

print(zg2)

print(linebreak)
# ------------------------

print("rsplit()")
print("Splits the string at the specified separator and returns a list.")

zh = "Apple, Banana, Cherry"

print(zh.rsplit(","))

print(linebreak)
# ------------------------

print("rstrip()")
print("Returns a copy of the string in which all chars have been stripped from the end of the string (default is whitespace characters).")

zi = "8888888..Hello!..8888888"

print(zi.rstrip('8'))

print(linebreak)
# ------------------------

print("split()")
print("Splits the string at the specified separator and returns a list.")

zj = "My name is Demi."

print(zj.split())

print(linebreak)
# ------------------------

print("splitlines()")
print("Splits the string at the line breaks and returns a list.")

zk = "Hello I am\n a\n geek!"
print("Split list: ", zk.splitlines(), "\n")

print(linebreak)
# ------------------------

print("startswith()")
print("Returns True if the string starts with a specified value.")

zl = "Hello"

print(zl.startswith("H"))

print(linebreak)
# ------------------------

print("strip()")
print("Returns a copy of the string in which all chars have been stripped from the beginning and end of the string (default is whitespace characters).")

zm = "8888888..Hello!..8888888"

print(zm.strip('8'))

print(linebreak)
# ------------------------

print("swapcase()")
print("Swaps cases, lowercase becomes uppercase and vice versa.")

zn = "HELLO"

print(zn.swapcase())

print(linebreak)
# ------------------------

print("title()")
print("Converts the first character of each word to uppercase.")

zo = "i love dogs so much"

print(zo.title())

print(linebreak)
# ------------------------

print("translate()")
print("Returns a translated string.")

#use a dictionary with ascii codes to replace 83 (S) with 80 (P)

zp = {83:  80}
zp2 = "Hello Sam!"
print(zp2.translate(zp))

print(linebreak)
# ------------------------

print("upper()")
print("Converts a string into uppercase.")

zq = "hello"
zq2 = zq.upper()

print(zq2)

print(linebreak)
# ------------------------

print("zfill()")
print("Fills the string with a specified number of 0 values at the beginning, making the string match the number you put in parenthesis.")

zr = "Hello"

print(zr.zfill(10))

print(linebreak)
# ------------------------