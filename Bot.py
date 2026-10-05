import sys
import time
from colorama import init, Fore, Style

init()

bot_name: str = 'Bob'
def bot_print(message: str) -> None:
    print(Fore.CYAN + Style.BRIGHT + message + Style.RESET_ALL)

bot_print(f'Hello! I am {bot_name}. I can assist you')

while True:
    user_input: str = input('You: ').lower()

    if user_input in ['hi', 'hello']:
        bot_print(f'{bot_name}: Hi! How can I help you?')
    elif user_input in ['bye', 'see you']:
        bot_print(f'{bot_name}: Goodbye! Have a nice day!')
        bot_print('Exiting in 5 seconds...')
        time.sleep(5)
        sys.exit()
    elif user_input in ["how are you?"]:
        bot_print(f'{bot_name}: Good, how are you?')
    elif user_input in ["what is your name?", "who are you?"]:
        bot_print(f'{bot_name}: I am {bot_name}. I can assist you.')
    elif user_input in ["what can you do?"]:
        bot_print(f'{bot_name}: I can assist you with basic arithmetic operations like addition, subtraction, multiplication, and division. You can also ask me about the weather or for a joke.')
    elif user_input in ["tell me a joke"]:
        bot_print(f'{bot_name}: Why did the scarecrow win an award? Because he was outstanding in his field!')
    elif user_input in ["tell me another joke", 'tell me another one']:
        bot_print(f'{bot_name}: Why don’t scientists trust atoms? Because they make up everything!')
    elif user_input in ["what is the weather?"]:
        bot_print(f'{bot_name}: I am sorry, I cannot provide weather information at the moment. Please check a weather website or app for the latest updates.')
    elif user_input in ['+', 'add']:
        bot_print(f'{bot_name}: Sure! I can help you with addition. Please provide two numbers.')
        try:
            num1: float = float(input('Num 1: '))
            num2: float = float(input('Num 2: '))
            bot_print(f'{bot_name}: {num1} + {num2} = {num1 + num2}')
        except ValueError:
            bot_print(f'{bot_name}: Invalid input')
    elif user_input in ['-', 'subtract']:
        bot_print(f'{bot_name}: Sure! I can help you with subtraction. Please provide two numbers.')
        try:
            num1: float = float(input('Num 1: '))
            num2: float = float(input('Num 2: '))
            bot_print(f'{bot_name}: {num1} - {num2} = {num1 - num2}')
        except ValueError:
            bot_print(f'{bot_name}: Invalid input')
    elif user_input in ['*', 'multiply']:
        bot_print(f'{bot_name}: Sure! I can help you with multiplication. Please provide two numbers.')
        try:
            num1: float = float(input('Num 1: '))
            num2: float = float(input('Num 2: '))
            bot_print(f'{bot_name}: {num1} * {num2} = {num1 * num2}')
        except ValueError:
            bot_print(f'{bot_name}: Invalid input')
    elif user_input in ['/', 'divide']:
        bot_print(f'{bot_name}: Sure! I can help you with division. Please provide two numbers.')
        try:
            num1: float = float(input('Num 1: '))
            num2: float = float(input('Num 2: '))
            if num2 == 0:
                bot_print(f'{bot_name}: Error! Division by zero is not allowed.')
            else:
                bot_print(f'{bot_name}: {num1} / {num2} = {num1 / num2}')
        except ValueError:
            bot_print(f'{bot_name}: Invalid input')
    else:
        bot_print(f'{bot_name}: I am sorry, I did not understand that. Please try again.')
