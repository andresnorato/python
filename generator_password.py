import random

def generator_password():
    mayusculas = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J']
    minusculas = ['a', 'b', 'c','d','f', 'g', 'h', 'i', 'j']
    simbolos = ['!', '#', '$', '%', '/',]
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    caracteres = mayusculas + minusculas + simbolos + numbers
    password = []
    for i in range(15):
        caracter_ramdo = random.choice(caracteres)
        password.append(caracter_ramdo) 

    password = "".join(password)
    return password

def run():
    password = generator_password()
    print('Your new password is: ' + password)


if __name__ == '__main__':
    run()