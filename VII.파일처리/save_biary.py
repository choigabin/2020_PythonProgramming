#238
color = [255,0,127]  #[FF, 00, 7F] ->11111111, 0000000001111111111
byte_list = bytes(color)

try:
    file = open('data.bin', 'wb')
    file.write(byte_list)
finally:
    file.close()
