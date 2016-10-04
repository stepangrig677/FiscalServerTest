#import binascii

def HexStringToHex():
    return 0

def HexToHexString():
    return 0

def  HexToInt(s):
    return int(s, 16)

def  IntToHex(s):
    return hex(s)

def  AsciiToHex(s):
    return s.encode('CP866')

def  HexToAscii(s):
    return s.decode('CP866')

def HexToBin(s):
    return bin(s)

print('Жопа'.encode('CP866').decode('CP866'))