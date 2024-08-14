s1 = input("s1 matnini kiriting: ")
s2 = input("s2 matnini kiriting: ")

if s2 in s1:
    s1 = s1.replace(s2, "", 1)

print("Yangi matn:", s1)
