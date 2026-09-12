# Rule-Based AI Chatbot

A simple web-based **Rule-Based AI Chatbot** built using Python and Flask. The chatbot responds to predefined user inputs using basic "**if-else**" decision-making logic.

## Project Overview

This project demonstrates the basic concept of a rule-based artificial intelligence system.

Instead of using machine learning or deep learning, the chatbot uses predefined rules to identify user inputs and generate appropriate responses.

## Features

* Responds to common greetings
* Handles basic conversations
* Provides predefined responses
* Handles exit commands
* Simple and beginner-friendly implementation
* Web-based interface using Flask
* Runs locally through a web browser

## Technologies Used

* Python
* Flask
* HTML
* CSS
* Rule-Based Logic
* If-Else Statements

## Project Structure

```text
rule-based-chatbot/
│
├── app.py
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/rule-based-chatbot.git
```

### 2. Open the Project Folder

```bash
cd rule-based-chatbot
```

### 3. Install the Required Dependencies

**bash
pip install -r requirements.txt**

### 4. Run the Flask Application

**bash
python app.py**

### 5. Open the Chatbot

After running the application, open the following address in your web browser:

**http://127.0.0.1:5000/**

This address works when the Flask application is running on your computer.

## Example Interaction

```text
User: Hello

Bot: Hello! How can I help you?

User: How are you?

Bot: I'm doing great! Thanks for asking.

User: Bye

Bot: Goodbye! Have a nice day!
```

## How It Works

The chatbot receives the user's input and compares it with predefined rules.

```text
User Input
    |
    v
Process Input
    |
    v
Check Predefined Rules
    |
    v
Match Found?
   / \
 Yes  No
  |    |
  v    v
Response  Default Response
```

For example:

```python
if user_input == "hello":
    response = "Hello! How can I help you?"
elif user_input == "bye":
    response = "Goodbye!"
else:
    response = "Sorry, I don't understand."
```

## Learning Objectives

This project demonstrates:

* Python programming fundamentals
* Conditional statements
* Control flow
* Basic AI concepts
* User input processing
* Flask web application development
* Basic frontend and backend integration

## Future Improvements

Possible improvements include:

* Add more conversation rules
* Add natural language processing
* Store conversation history
* Add database support
* Integrate machine learning
* Add voice input and output
* Deploy the chatbot online

