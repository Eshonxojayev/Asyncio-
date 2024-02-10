import asyncio

""" sonning bo'linuvchilarini topadi """

def find_divisors(number):
    divisors = [1]
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            divisors.extend([i, number // i])
    return divisors

async def task1():
    number = 28
    divisors = find_divisors(number)
    print(f"Task 1: Divisors of {number}: {divisors}")

async def task2():
    number = 6
    divisors = find_divisors(number)
    print(f"Task 2: Divisors of {number}: {divisors}")

async def task3():
    number = 12
    divisors = find_divisors(number)
    print(f"Task 3: Divisors of {number}: {divisors}")

async def task4():
    number = 16
    divisors = find_divisors(number)
    print(f"Task 4: Divisors of {number}: {divisors}")

async def task5():
    number = 8
    divisors = find_divisors(number)
    print(f"Task 5: Divisors of {number}: {divisors}")

async def main():
    await asyncio.gather(task1(), task2(), task3(), task4(), task5())

asyncio.run(main())
