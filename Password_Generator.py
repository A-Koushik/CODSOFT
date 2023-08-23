import random
from random import sample

upper_alpha=[chr(i) for i in range(65,(65+26))]
random.shuffle(upper_alpha)
lower_alpha=[chr(i) for i in range(97,(97+26))]
random.shuffle(lower_alpha)
spec_char=[chr(i) for i in range(33,48)]
random.shuffle(spec_char)
digits=[i for i in range(10)]
random.shuffle(digits)

length=int(input(("Enter password length : ")))
min_upper=int(input("Enter minimum no.of Uppercase Characters : "))
min_lower=int(input("Enter minimum no.of Lowercase Characters : "))
min_spe=int(input(("Enter minimum no.of Special Characters : ")))
min_digits=int(input(("Enter minimum no.of Digits : ")))

min=min_upper+min_lower+min_spe+min_digits

password=sample(upper_alpha,min_upper)+sample(lower_alpha,min_lower)+sample(spec_char,min_spe)+sample(digits,min_digits)
all_symbols=upper_alpha+lower_alpha+spec_char+digits
password=password+sample(all_symbols,(length-min))
print("Generated password : ","".join([str(i) for i in password]))