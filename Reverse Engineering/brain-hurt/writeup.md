# HSCTF 2023 Reverse Engineering: brain-hurt #

Challenge description: Rumor has it Godzilla had a stroke trying to read the code

To solve this problem we are given source code to what seems to be an encryption program and checker (as shwon below).

```
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
  
