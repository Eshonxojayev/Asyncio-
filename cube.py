import asyncio

"""Sonnig kvadratini , kubini topadi bo'linuvchilarini topadi ,"""

def find_divisors(number):
    divisors = [1]
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            divisors.extend([i, number // i])
    return divisors

async def calculate_powers(number):
    divisors = find_divisors(number)
    square = number ** 2
    cube = number ** 3
    print(f"Number: {number}, Divisors: {divisors}, Square: {square}, Cube: {cube}")

async def task1():
    await calculate_powers(28)

async def task2():
    await calculate_powers(6)

async def task3():
    await calculate_powers(12)

async def task4():
    await calculate_powers(16)

async def task5():
    await calculate_powers(8)

async def main():
    await asyncio.gather(task1(), task2(), task3(), task4(), task5())

asyncio.run(main())
