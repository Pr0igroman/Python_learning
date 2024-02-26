words = ("madam", "fire", "tomato", "book", "kiosk", "mom")
print(list(filter(lambda w: w == w[::-1], words)))
