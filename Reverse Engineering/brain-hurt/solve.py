flag=[]
lst=[]
next=[]
ciphertext='ZT_YE\\0|akaY.LaLx0,aQR{"C'
for jk in ciphertext:
  next.append(jk)
for i in next:
  for x in range(0, 1000):
    result = ((x ^ 0xFF)%95 + 32)
    if result == ord(i):
        lst.append(str(x))
        break
for i in lst:
  if int(i) < 33:
    flag.append(chr(int(i)+95))
  else:
    flag.append(chr(int(i)))
print("".join(flag))
