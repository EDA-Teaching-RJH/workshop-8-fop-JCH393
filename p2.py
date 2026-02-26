import re
pN = input("What's your phone number? ").strip()

if re.search(r'^(07\d{8,12})$', pN):
 print("Valid")
else:
 print("Invalid")
