# Asynchronous Generators and Async Comprehensions

This repository provides examples and explanations on how to write asynchronous generators, use async comprehensions, and type-annotate generators in Python.

## How to Write an Asynchronous Generator

To write an asynchronous generator, you can use the `async def` syntax along with the `yield` keyword. Here's an example:
```py
async def async_generator():
    for i in range(5):
        await asyncio.sleep(1)
        yield i

async def main():
    async for item in async_generator():
        print(item)

asyncio.run(main())
```
## How to Use Async Comprehensions

Async comprehensions allow you to create asynchronous generators in a concise and readable way. To use async comprehensions, you can modify the previous example as follows:
```py
async def async_comprehension():
    async for i in range(5):
        await asyncio.sleep(1)
        yield i

async def main():
    async for item in async_comprehension():
        print(item)

asyncio.run(main())
```