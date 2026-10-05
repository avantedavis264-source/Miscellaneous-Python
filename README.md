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
