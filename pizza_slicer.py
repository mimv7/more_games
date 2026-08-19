print(
    """
    0   1   3   4   5   6
    +---+---+---+---+---+
    | p | i | z | z | a |
    +---+---+---+---+---+
    -5  -4  -3  -2  -1
    """
)
word = 'pizza'

while True:
    start_input = input('start (или Enter для выхода): ').strip()

    # Если на старте нажали Enter — выходим из цикла
    if not start_input:
        break

    try:
        start = int(start_input)
        finish_input = input('finish: ').strip()

        # Если finish пустой, выходим или сигнализируем об ошибке
        if not finish_input:
            print("Ошибка: индекс finish не может быть пустым.")
            continue

        finish = int(finish_input)

        print(f'slice [{start}:{finish}] ')
        print(f'Результат: "{word[start:finish]}"\n')

    except ValueError:
        print("Ошибка: вводите только целые числа!\n")

print("Программа завершена.")
input()
