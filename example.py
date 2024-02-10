from datetime import datetime

import asyncio

async def task1():
    await asyncio.sleep(3)
    print("Task 1 completed")

async def task2():
    await asyncio.sleep(2)
    time = datetime.now().time()
    print(f"Task 2 completed {time}")

import json
async def task3():
    name = input("name = ")
    with open("test.json", "w") as file:
        json.dump({"name": name}, file, indent=6)
    await asyncio.sleep(5)
    time = datetime.now().time()
    print(f"Task 3 completed {time}")

async def task4():
    await asyncio.sleep(2)
    time = datetime.now().time()
    print(f"Task 4 completed {time}")

async def main():
    await asyncio.gather(task1(), task2(), task3(), task4())

if __name__ == "__main__":
    print(datetime.now().time())
    asyncio.run(main())
    print(datetime.now().time())