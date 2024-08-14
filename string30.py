s1 = input("s1 matnini kiriting: ")
s2 = input("s2 matnini kiriting: ")
yangi_matn = ""
for belgi in s1:
    if belgi == 'C':
        yangi_matn += belgi + s2
    else:
        yangi_matn += belgi
print("Yangi matn:", yangi_matn)
