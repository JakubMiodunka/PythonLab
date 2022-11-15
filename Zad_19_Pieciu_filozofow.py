#!/bin/env python3
import concurrent.futures
import random

class Fork:
    def __init__(self) -> None:
        self.taken = False

    def take(self) -> bool:
        assert not self.taken
        self.taken = True


def workers_init(forks: list):  # Used for shereing reasources between threads
    global shered_forks
    shered_forks = forks


def philozopher(id: int):   # Lanuched as sepparate thread
    taken = 0
    # Attemt to take left fork
    try:
        if random.randint(0, 100) <= 50:    # 50% chanse that philozopher will take fork
            shered_forks[id - 1].take()
            taken += 1
    except AssertionError:
        print(f"[Philosopher {id}] Left fork not available")
        return

    try:
        if random.randint(0, 100) <= 50:    # 50% chanse that philozopher will take fork
            shered_forks[id].take()
            taken += 1
    except AssertionError:
        print(f"[Philosopher {id}] Right fork not available")
        return

    print(f"[Philosopher {id}] {taken} forks taken")


if __name__ == "__main__":
    philozophers_quantity = 3   # Philosophers quantiti can be configured here

    # Creating a list of forks
    forks = list()
    for _ in range(philozophers_quantity):
        forks.append(Fork())

    # Submitting philosophers threads
    with concurrent.futures.ThreadPoolExecutor(initializer=workers_init, initargs=(forks,)) as executor:
        for id in range(philozophers_quantity):
            executor.submit(philozopher, id)


    