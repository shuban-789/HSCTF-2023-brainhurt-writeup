# HSCTF 2023 Reverse Engineering: brain-hurt #

Challenge description: Rumor has it Godzilla had a stroke trying to read the code

To solve this problem we are given source code to what seems to be an encryption program and checker (as shown below).

```python
import sys

def validate_flag(flag):
    encoded_flag = encode_flag(flag)
    expected_flag = 'ZT_YE\\0|akaY.LaLx0,aQR{"C'
    if encoded_flag == expected_flag:
        return True
    else:
        return False

def encode_flag(flag):
    encoded_flag = ""
    for c in flag:
        encoded_char = chr((ord(c) ^ 0xFF) % 95 + 32)
        encoded_flag += encoded_char
    return encoded_flag

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <flag>")
        sys.exit(1)
    input_flag = sys.argv[1]
    if validate_flag(input_flag):
        print("Correct flag!")
    else:
        print("Incorrect flag.")

if __name__ == "__main__":
    main()
```

So first, let's break down the algorithm.

## Algorithm Breakdown ##

```
Function validate:
  encoded flag is encode function applied on function input
  expected flag to check with is <encoded_flag>
  if the encoded version of the flag is encoded flag, return true
  if it isn't, return false
  
Function encode:
  for every character in flag, raise the ASCII order to 255th power, take the modulus of 95, add 32, put character correspdonding to the order of that number to encoded flag
  
Function main:
  (simple checker program)
```

### Key Features to Reverse ###

There is only one main feature we need to reverse. That being the `chr((ord(c) ^ 0xFF) % 95 + 32)`. We first need to understand what ord and chr do. Ord takes in a character and returns its unicode, chr takes in unicode, and returns a character. Everything in our algorithm is pretty much reversible, except modulus. However, we could brute force this.

## Solve Algorithm ##

We could make a simple brute force program to compare the ord of every character of ciphertext `ZT_YE\\0|akaY.LaLx0,aQR{"C` to a number in range from 0 to 1000. If it matches, we can use that number. If not, we move on. However, if in the case the character is not standard plaintext (below ord 33), we add 95 to it because adding 95 will still make the modulus work, and give us a plaintext character at the same time.

```python
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
```

## Testing ##

As you can see, when we run the code, we can get the flag.

![image](https://cdn.discordapp.com/attachments/803021452797411348/1117198364572930151/image.png)

## Math Explanation ##
