from pprint import pprint
from typing import List, Iterator
from random import randint
from copy import deepcopy


def input_numbers(count: int) -> List[int]:
    return list(map(lambda i: int(input(f"Enter {i} number: ")), range(count)))


def input_list() -> Iterator[str]:
    elements_count = int(input("Amount: "))
    return (input(f"Enter {i} element: ") for i in range(elements_count))


def first_task() -> None:
    print("1.1")
    a, b, c, d, k = input_numbers(5)

    try:
        print(abs(1 - a * b ** c - a * (b ** 2 - c ** 2) + (b - c + a) * (12 + b) / (c - a)))
    except ZeroDivisionError:
        return print("Zero division")

    print("1.2")
    for i, element in enumerate(list(input_list())):
        if i % 2:
            print(element)

    print("1.3")
    result = 1
    for element in [int(i) for i in input_list()]:
        if element < 10:
            result *= element
    print(result)

    print("1.4")
    result = 0
    numbers = [int(i) for i in input_list()]
    for number in numbers:
        result += number
    print(result / len(numbers))


def second_task() -> None:
    print("2.1")
    my_number = 13
    user_number = 0
    while user_number != my_number:
        user_number = int(input("Enter number: "))

    print("2.2")
    for element in list(input_list()):
        if element.endswith("r"):
            print(element)

    print("2.3")
    print("".join((str(randint(1, 9)) for _ in range(5))) + "3")

    print("2.4")
    text = input("Text: ")
    amount = 0
    for letter in text:
        if letter == "Л":
            amount += 1
    print("Л".join(map(lambda x: "", range(amount + 1))))


def third_task() -> None:
    matrix = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [8, 7, 6, 5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6, 7, 8, 9],
        [9, 8, 7, 6, 5, 4, 3, 2],
        [1, 3, 5, 7, 9, 7, 5, 3],
        [3, 1, 5, 3, 2, 6, 5, 7],
        [1, 7, 5, 9, 7, 3, 1, 5],
        [2, 6, 3, 5, 1, 7, 3, 2],
    ]

    print("3.1")
    copy_matrix = deepcopy(matrix)
    for row in range(len(copy_matrix)):
        for col in range(len(copy_matrix[row])):
            element = copy_matrix[row][col]
            if element < 5:
                copy_matrix[row][col] = element ** 2
    pprint(copy_matrix)

    print("3.2")
    copy_matrix = deepcopy(matrix)
    result = []
    for row in range(len(copy_matrix)):
        res = 0
        for col in range(len(copy_matrix[row])):
            if col % 2 == 0:
                res += copy_matrix[row][col]
        result.append(res)
    pprint(result)

    print("3.4")
    copy_matrix = deepcopy(matrix)
    bol, men = 0, 0
    for row in copy_matrix:
        for element in row:
            if element < 5:
                men += element
            if element >= 5:
                bol += element
    if bol >= men:
        print(bol)
    else:
        print(men)

    print("3.5")
    copy_matrix = deepcopy(matrix)
    for row in range(len(copy_matrix)):
        for col in range(len(copy_matrix[row])):
            element = copy_matrix[row][col]
            if element == 5:
                copy_matrix[row][col] = element ** 2
    pprint(copy_matrix)

    print("3.6")
    copy_matrix = deepcopy(matrix)
    for row in copy_matrix:
        row.clear()
    pprint(copy_matrix)

    print("3.7")
    copy_matrix = deepcopy(matrix)
    amount = 0
    for row in copy_matrix:
        for element in row:
            if element == 3:
                amount += 1
    print(amount)


def fourth_task() -> None:
    print("4.1")
    text = input("text: ")
    print(" ".join((element for element in text.split(" ") if 5 <= len(element) <= 10)))

    print("4.2")
    students = (
        "Ф;И;О;Возраст;Категория;"
        "_Иванов;Иван;Иванович;23 года;Студент 3 курса;"
        "_Петров;Семен;Игоревич;22 года;Студент 2 курса"
    )
    data = students.split(";_")
    values = []
    for row in data:
        values.append(row.split(";"))

    print("ФИО                  \tВозраст        \tКатегория")
    for value in values[1:]:
        print(" ".join([value[0], value[1], value[2]]), end=" ")
        print("\t{} \t\t{}".format(value[3], value[4]))

    print("4.3")
    students = (
        "ФИО;Возраст;Категория;"
        "_Иванов Иван Иванович;23 года;Студент 3 курса;"
        "_Петров Семен Игоревич;22 года;Студент 2 курса;"
        "_Иванов Семен Игоревич;22 года;Студент 2 курса;"
        "_Акибов Ярослав Навич;23 года;Студент 3 курса;"
        "_Борков Станислав Максимович;21 год;Студент 1 курса;"
        "_Петров Семен Семенович;21 год;Студент 1 курса;"
    )
    data = students.split(";_")
    values = []
    for row in range(1, len(data)):
        values.append(data[row].split(";"))
    valid_data = []
    for element in values:
        age = element[1][:2]
        if int(age) > 21:
            valid_data.append(element)
    print("ФИО                  \tВозраст        \tКатегория")
    for value in valid_data:
        print("{} \t{} \t\t{}".format(value[0], value[1], value[2]))

    print("4.4")
    text = "rorol orleke rkgjsol sgjsg"
    print(f"Words: {len(text.split(' '))}")
    print(f"Symbols: {len(text)}")


def sixth_task() -> None:
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print("6.1")
    sum = 0
    for row in matrix:
        for element in row:
            sum += element
    print(sum)

    print("6.2")
    list_ = ["a", "b", "c", "d", "b", "a", "b", "c", "d", "b"]
    res = []
    for i, element in enumerate(list_):
        if i in list(range(4, 9)):
            continue
        res.append(element)
    res.append("g")
    res.append("h")
    print(res)

    print("6.3")
    groups = [["БО-331101", ["Акулова Алена", "Пабушкина Асения"]], ["БОВ-421102", ["Олег Попоов", "Рома Кулибин"]]]
    for group in groups:
        print(group[0])
        for student in group[1]:
            print(student)

    print("6.4")
    for group in groups:
        for student in group[1]:
            surname, name = student.split(" ")
            if name.startswith("А") and surname.startswith("П"):
                print(student)


def main() -> None:
    first_task()
    second_task()
    third_task()
    fourth_task()
    sixth_task()


if __name__ == "__main__":
    main()
