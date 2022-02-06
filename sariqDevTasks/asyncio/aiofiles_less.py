import asyncio
import aiofiles


def read_file():
    with open(r"my_big_file.txt", "r") as file:
        return file.read()


async def async_read_file():
    async with aiofiles.open(r"my_big_file.txt", "r") as file:
        return await file.read()


async def async_main():
    text = await async_read_file()
    print(f"Count words. in file={len(text.split(' '))}")


def main():
    text = read_file()
    print(f"Count words. in file={len(text.split(' '))}")


if __name__ == "__main__":
    asyncio.run(async_main())
    main()
