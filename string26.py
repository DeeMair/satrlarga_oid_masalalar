n = int(input("Sonni kiriting: "))
matn = input("Matnni kiriting: ")
matn_uzuligi = len(matn)
if matn_uzuligi > n:
  matn = matn[matn_uzuligi - n]
else:
  farq = n - matn_uzuligi
  matn = "*" * farq + matn

print(matn)