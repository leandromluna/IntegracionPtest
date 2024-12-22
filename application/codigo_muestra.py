import random
from time import sleep

import pandas as pd


def add_numbers(a: float, b: float) -> float:
    return a + b


def greet(name: str) -> str:
    return "Hello, " + name


def create_df_from_name(name: str) -> pd.DataFrame:
    df = pd.DataFrame({"name": [name], "number": [random.random()]})
    # Este comentario está dividido en varias líneas para cumplir
    # con la regla de longitud de línea y mejorar la legibilidad.
    return df


def main() -> None:
    result = add_numbers(5, 3)
    print(result)

    greeting = greet("Charly")
    print(greeting)
    sleep(1)

    items = [1, 2, 3, 4, 5]
    squared = [x * x if x % 2 == 0 else 0 for x in items]
    # Comentario de prueba para la lista "squared"
    print(squared)


if __name__ == "__main__":
    main()
