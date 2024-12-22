from time import sleep
import pandas as pd
from datetime import datetime
import random


def add_numbers(a:float, b:float)  -> float:
    return a + b

def greet(name:str) -> str:
    return "Hello, " + name

def create_df_from_name(name:str) -> pd.DataFrame:
    df = pd.DataFrame({"name": [name], "number": [random.random()]})
    # un comentario muy muy largo, tan largo que hacia que se disparar el linter porque no debe ser tan largo segun la regla de 88 caracteres
    return df

def main() -> None:
    result = add_numbers(5, 3)
    print(result)

    greeting = greet("Charly")
    print(greeting)
    sleep(1)


    items = [1, 2, 3, 4, 5]
    squared = [x * x if x % 2 == 0 else 0 for x in items]
    ##comentario de test
    print(squared)


if __name__ == "__main__":
    main()