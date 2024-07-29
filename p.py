import asyncio
import aiofiles

async def read_code_file(file_path):
    async with aiofiles.open(file_path, mode='r') as file:
        contents = await file.read()
        return contents

async def main():
    file_path = 'example.py'  # Replace with your file path
    contents = await read_code_file(file_path)
    print(contents)

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
