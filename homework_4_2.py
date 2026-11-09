"""
ФИО: Мемикенов Мирам Молдабаевич
Группа: ИСИП-ОФ 11-НСК 01.24
Занятие 4.2: Полиморфизм, диспетчеризация по ключу, словарь обработчиков
"""

import json

OPERATIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else float('inf')
}

def calc(a, op, b):
    handler = OPERATIONS.get(op)
    if handler is None:
        raise ValueError(f"Неизвестная операция: '{op}'")
    return handler(a, b)

def _to_json(data):
    return json.dumps(data, ensure_ascii=False)

def _to_csv(data):
    if isinstance(data, list):
        return ",".join(map(str, data))
    elif isinstance(data, dict):
        return ",".join(f"{k}={v}" for k, v in data.items())
    return str(data)

FORMATTERS = {
    "json": _to_json,
    "csv": _to_csv
}

def format_data(data, fmt):
    formatter = FORMATTERS.get(fmt.lower())
    if formatter is None:
        raise ValueError(f"Неподдерживаемый формат: '{fmt}'")
    return formatter(data)

TYPE_HANDLERS = {
    str: lambda v: f"Длина строки: {len(v)}",
    int: lambda v: f"Квадрат числа: {v ** 2}",
    list: lambda v: f"Сумма списка: {sum(v)}"
}

def process(value):
    value_type = type(value)
    handler = TYPE_HANDLERS.get(value_type)
    if handler is None:
        raise ValueError(f"Нет обработчика для типа: {value_type.__name__}")
    return handler(value)

if __name__ == "__main__":
    print("--- Тест Задания 1 ---")
    print("10 + 5 =", calc(10, "+", 5))
    print("10 * 5 =", calc(10, "*", 5))

    print("\n--- Тест Задания 2 ---")
    test_list = [10, 20, 30, 40]
    print("В JSON:", format_data(test_list, "json"))
    print("В CSV:", format_data(test_list, "csv"))

    print("\n--- Тест Задания 3 ---")
    print(process("Python"))
    print(process(8))
    print(process([1, 2, 3]))
