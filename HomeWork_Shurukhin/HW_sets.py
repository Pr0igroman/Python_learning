mathem = {"Матвей", "Евгения", "Михаил", "Максим", "Наталья"}
physics = {"Максим", "Матвей", "Александр"}

print("Все призёры: ", mathem | physics)
print("Призёры обеих олимпиад: ", mathem & physics)
new_mathem = (mathem & physics) - (mathem ^ physics)
print("Обновлённый список призёров по математике: ", new_mathem)
del physics
