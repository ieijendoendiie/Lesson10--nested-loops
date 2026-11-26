# Outer loop: keeps asking the user for numbers until they type 'exit'
while True:
    user_input = input("Enter a decimal number (or type 'exit' to quit): ")

    if user_input.lower() == "exit":
        break

    num = int(user_input)

    if num == 0:
        print("Binary: 0\n")
        continue

    temp_num = num
    binary_result = ""

    # Inner loop: converts the entered number into binary
    while temp_num > 0:
        remainder = temp_num % 2
        binary_result = str(remainder) + binary_result
        temp_num = temp_num // 2

    print(f"Binary: {binary_result}\n")
