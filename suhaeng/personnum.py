def mask_security_number(security_number):
   security_number_list = list(security_number)
   if len(security_number_list) == 14:
       security_number_list[10:15] = ["*","*","*","*"]
   else:
       security_number_list[9:14] = ["*","*","*","*"]
   return ''.join(security_number_list) #리스트에서 문자열로

def mask_security_number_ex(security_number):
   return security_number[:len(security_number) - 4] + "****"

print(mask_security_number("030816-4174412"))
print(mask_security_number_ex("6412244174411"))
