n1 = int(input("1-sonni kiritng:"))
n2 = int(input("2-sonni kiritng:"))
s1 = input("1-matnni kiriting: ")
s2 = input("2-maynni kiriting: ")

if n1 > len(s1):
    print("Birinchi kiritilgan son matn uzunligidan katta!")
elif n2 > len(s2):
    print("Ikkinchi kiritilgan son matn uzunligidan katta!")
else:
    yangi_matn = s1[:n1] + s2[-n2:]
    print("Yangi matn:", yangi_matn)
