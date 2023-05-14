import random

password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

while True:
    inputgenerate =  int(input("Какой длины пароль вы желаете сгенерировать?"))
    generatedpassword = ""

    for i in range(inputgenerate):
        generatedpassword += random.choice(password)

    print("Сгенерированный пароль:", generatedpassword)