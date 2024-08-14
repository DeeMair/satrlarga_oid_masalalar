matn = input("Matnni kiriting: ")
yangi_matn = ""
for i in matn:
    if i == 'C':
        yangi_matn += 'CC'
    else:
        yangi_matn += i

print(yangi_matn)