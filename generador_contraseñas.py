import random

def password_generator():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F']
    lower = ['a', 'b', 'c', 'd', 'e', 'f']
    simb = ['@', '#', '$', '%', '&', '*']
    numbers = ['1', '2', '3', '4', '5', '6']

    characters = mayus + lower + simb + numbers

    password = []

    for i in range(10):
        ramdomcharacter = random.choice(characters)
        password.append(ramdomcharacter)

    password = "".join(password)
    return password

def main():
    password = password_generator()
    print('Your password is: ' + password)

if __name__ == "__main__":
    main()