import binascii

from KKM.Help.CRC16CITT import *

Mess = bytearray(open('__Start', 'rb').read())
print('Check Code1: '+hex(Mess[28])+hex(Mess[29]))

Mess[28] = 0x00
Mess[29] = 0x00


print('Check Code2: '+str(crc16(Mess[30:])))

'''
print('Контр сумма')
CheckCode = Mess[28:30]
print(CheckCode)

print('Контр сумма')

print(Mess[28])
print(Mess[29])

Mess[28]=0x00
Mess[29]=0x00

print('Контр сумма')
print(crc16(Mess[50:].decode('CP866')))
print(crc16(Mess.decode('CP866')))

#print(crc16(binascii.hexlify(Mess)))
'''