a = "abcdefghijklmnopqrsruvwxyzабвгдеёжзийклмнопрстуфхцчшщъьэюя"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЭЮЯ"
c = input("Введите букву из нижнего регистра: ")
for i in range (len(a)):
	if a[i] == c:
		print("Та же буква в верхнем регистре: ", b[i])
