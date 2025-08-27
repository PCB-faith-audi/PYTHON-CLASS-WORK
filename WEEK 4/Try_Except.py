#Error handling in python
try:
    with open("readme,md", "r",) as file:
        data = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path and name.")
except exception as e:
    print(f"An error occurred: {e}")