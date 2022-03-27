from hashlib import sha512
# Output is a 512 bits long sequence (message digest)
# Result is a 128 character long hexadecimal sequence
# 1 hexadecimal character character can be stored on 4 bits
# 2^512 = the number of possible hashes
# Because of the birthday paradox we have to compute 2^256 possibilities to make a collision attack  

s1 = 'My name is Malik.'
s2 = 'My name is Malik'
result1 = sha512(s1.encode())
print(result1.hexdigest())
result2 = sha512(s2.encode())
print(result2.hexdigest())