import re

#reg = r"^[0-9a-zA-Z@_-]{6,18}$"
reg = r"^[\w+@-]{6,18}$"

password1 = "my-p@ssw0rd"
password2 = "eerge"
password3 = "Parol_123-456@"
password4 = "passwordpassword123456"

print(re.findall(reg, password1))
print(re.findall(reg, password2))
print(re.findall(reg, password3))
print(re.findall(reg, password4))
