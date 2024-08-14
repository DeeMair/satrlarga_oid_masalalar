s1 = input("s1 matnini kiriting: ")
s2 = input("s2 matnini kiriting: ")
index = s1.rfind(s2)
yangi = ""
if s2 in s1:
    yangi = s1.replace(index, "", (-1))

print(yangi)
