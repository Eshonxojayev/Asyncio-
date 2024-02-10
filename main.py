from datetime import datetime

import asyncio

async def task1():
    await asyncio.sleep(1)
    print('Task 1 completed')

async def task2():
    await asyncio.sleep(1)
    time = datetime.now().time()
    print(f"Task 2 completed: {time}")

import json
async def task3():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    with open("main.json", "w") as file:
        json.dump({"name": name, "age": age}, file, indent=6)
    await asyncio.sleep(5)
    time = datetime.now().time()
    print(f"Task 3 completed: {time}")

async def task4():
    await asyncio.sleep(1)
    time = datetime.now().time()
    print(f"Task 4 completed: {time}")

async def task5():
    await asyncio.sleep(2)
    time = datetime.now().time()
    print(f"Task 5 completed: {time}")

async def main():
    await asyncio.gather(task1(), task2(), task3(), task4(), task5())

if __name__ == "__main__":
    print(datetime.now().time())
    asyncio.run(main())
    print(datetime.now().time())