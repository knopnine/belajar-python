secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = input()
while int(number) != secret_number:
    print("Ha ha! You're stuck in my loop!")
    number = input()
    if int(number) == secret_number:
        print("the secret number is " + str(secret_number))
        print("Well done, muggle! You are free now.")
        break

