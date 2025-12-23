import random, time

def loading():
    print("Загрузка...")
    for i in range(1, 101):
        print(f"{i}%", end="\r")
        time.sleep(0.02)
    print("Загрузка завершена!")
    print()


def finish_figure(figure):
    print("Должна получиться такая фигура:")
    for i in figure:
        print("".join(i))
    print()


def current1_figure(figure):
    for i in figure:
        print("".join(i))
    print()


def generate_figure(elements):
    return [
        [random.choice(elements), random.choice(elements)],
        [random.choice(elements), random.choice(elements)]
    ]

def figure_complete(current, target):
    return current == target

def main():
    figure1 = [
        ["┏", "┓"],
        ["┗", "┛"]
    ]
    elements1 = ["┏", "┓", "┗", "┛"]

    figure2 = [
        ["╭", "╮"],
        ["╰", "╯"]
    ]
    elements2 = ["╭", "╮", "╰", "╯"]

    chosen = random.choice([1, 2])
    if chosen == 1:
        target = figure1
        elements = elements1
    else:
        target = figure2
        elements = elements2

    loading()

    finish_figure(target)

    current_figure = generate_figure(elements)
    print("С помощью кнопок 1,2,3,4 меняйте направление элементов фигуры.")
    current1_figure(current_figure)

    while not figure_complete(current_figure, target):
        choice = input("> ").strip().lower()

        if choice in ['1', '2', '3', '4']:
            index = int(choice)

            pos_map = {1: (0, 0), 2: (0, 1), 3: (1, 0), 4: (1, 1)}
            a, b = pos_map[index]
            current_figure[a][b] = random.choice(elements)

            current1_figure(current_figure)
        else:
            print("Неверный ввод. Попробуйте снова.")

    print("Ура! У тебя получилось!")
    current1_figure(current_figure)

if __name__ == "__main__":
    main()
