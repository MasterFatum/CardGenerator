import random

def luhn_check(card_number):
    # Преобразуем номер карты в список цифр
    cardNumberString = ''.join(str(number) for number in card_number)
    digits = [int(d) for d in str(cardNumberString)]

    # Умножаем каждую вторую цифру на 2 и обрабатываем числа, большее 9
    for i in range(-2, -len(digits)-1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    # Суммируем все цифры
    total = sum(digits)

    # Если сумма кратна 10, то номер карты валидный
    return total % 10 == 0


def generate_number_mir(count):
    cardsNumbersIsValid = []
    newCard = '2202'
    while len(cardsNumbersIsValid) < count:
        for digit in range(12):
            newCard += str(random.randint(0, 9))
        if luhn_check(newCard):
            cardsNumbersIsValid.append(newCard)
        else:
            newCard = '2202'
    return cardsNumbersIsValid

def generate_number_visa(count):
    cardsNumbersIsValid = []
    newCard = '4012'
    while len(cardsNumbersIsValid) < count:
        for digit in range(12):
            newCard += str(random.randint(0, 9))
        if luhn_check(newCard):
            cardsNumbersIsValid.append(newCard)
        else:
            newCard = '4012'
    return cardsNumbersIsValid


def generate_cards_mir():
    cards = generate_number_mir(int(input('Введите количество номеров карт: ')))
    for card in cards:
        print(card)


def generate_cards_visa():
    cards = generate_number_visa(int(input('Введите количество номеров карт: ')))
    for card in cards:
        print(card)


def check_card():
    if luhn_check(input('Введите номер карты: ')):
        print('Номер карты валидный!')
    else:
        print('Номер карты не валидный!')


while True:
    print()
    print('VAN Card Generator V 1.0' + '\n')
    print('Генерировать номер карты MIR - 1')
    print('Генерировать номер карты VISA - 2')
    print('Проверить валидность карты - 3')
    print('Выход - 0' + '\n')

    action = input('Введите действие: ')

    match action:
        case '1':
            generate_cards_mir()
        case '2':
            generate_cards_visa()
        case '3':
            check_card()
        case '0':
            exit()