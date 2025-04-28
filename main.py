import random


def luhn_check(card_number):
    # Преобразуем номер карты в список цифр
    cardNumberString = ''.join(str(number) for number in card_number)
    digits = [int(d) for d in str(cardNumberString)]

    # Умножаем каждую вторую цифру на 2 и обрабатываем числа, большее 9
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    # Суммируем все цифры
    total = sum(digits)

    # Если сумма кратна 10, то номер карты валидный
    return total % 10 == 0


def generate_number(count):
    cardsNumbersIsValid = []
    newCard = ''
    while len(cardsNumbersIsValid) < count:
        for digit in range(16):
            newCard += str(random.randint(0, 9))
        if luhn_check(newCard):
            cardsNumbersIsValid.append(newCard)
        else:
            newCard = ''
    return cardsNumbersIsValid


# Пример использования
cards = generate_number(int(input('Введите количество номеров карт:')))
for card in cards:
    print(card)