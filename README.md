# Bob — Python Chatbot

A simple command-line chatbot built with Python. Bob responds to basic conversational prompts, provides jokes, and performs basic arithmetic operations through a text-based interface.

## Features

* Basic conversational responses
* Greeting and farewell commands
* Bot identity and capability responses
* Two built-in jokes
* Addition
* Subtraction
* Multiplication
* Division
* Division-by-zero protection
* Input validation for arithmetic operations
* Colored terminal output
* Graceful program exit

* Python 3.x
* `colorama`

Install the required dependency:

```bash
pip install colorama
```

## Usage

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Navigate to the project directory:

```bash
cd YOUR-REPOSITORY
```

Run the chatbot:

```bash
python chatbot.py
```

## Available Commands

| Input                  | Function                    |
| ---------------------- | --------------------------- |
| `hi`, `hello`          | Greeting                    |
| `bye`, `see you`       | Exit the chatbot            |
| `how are you?`         | General response            |
| `what is your name?`   | Bot identification          |
| `who are you?`         | Bot identification          |
| `what can you do?`     | Lists capabilities          |
| `tell me a joke`       | Tells a joke                |
| `tell me another joke` | Tells another joke          |
| `what is the weather?` | Weather limitation response |
| `+`, `add`             | Addition                    |
| `-`, `subtract`        | Subtraction                 |
| `*`, `multiply`        | Multiplication              |
| `/`, `divide`          | Division                    |


## Limitations

Bob currently uses predefined responses and does not use artificial intelligence, natural language processing, APIs, or external data sources. Weather information is not retrieved from an external service.

## License

This project is licensed under the MIT License.







# Number Guessing Game

A simple command-line number guessing game built with Python. The player attempts to guess a randomly generated number between 1 and 100 within a limited number of attempts.

## Features

* Random number generation

* Number range from 1 to 100

* Ten attempts per round

* Input validation

* Too high and too low hints

* Score tracking

* Multiple rounds

* High-score storage

* High-score display

* Colored terminal output

* Python 3.x

* `colorama`

Install the required dependency:

```bash
pip install colorama
```

## Usage

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Navigate to the project directory:

```bash
cd YOUR-REPOSITORY
```

Run the game:

```bash
python guessing_game.py
```

## How It Works

1. The game generates a random number between 1 and 100.
2. The player receives 10 attempts to guess the number.
3. The game checks whether the input is a valid integer.
4. The player receives a hint if the guess is too high or too low.
5. A correct guess increases the player's score.
6. The player can choose to play another round.
7. The player's name and score are saved to `Highscore.txt`.
8. Saved high scores are displayed when the game ends.

## Limitations

The game currently uses a simple scoring system where each successful round increases the score by one. High scores are stored in a text file and are not automatically sorted or ranked.

## License

This project is licensed under the MIT License.




