import re

reg = r"[+]?7\d{10}"
string = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"

print(re.findall(reg,string))