### 📘 `README.md`

# First OpenAI API Call

This project demonstrates a basic API call to OpenAI's GPT-3.5-Turbo model using the python.

## 🔧 What It Does

- Takes user input via console.
- Sends it with a fixed system prompt to the GPT-3.5-Turbo model.
- Displays the AI's reply and token usage(prompt, completion, total).

## 🚀 How to Run It

### 1. Clone the Repository

```bash
git clone https://github.com/vaibhavi1224/first-openai-api-call
cd first-openai-api-call
````

### 2. Install Dependencies

```bash
pip install openai python-dotenv
```

### 3. Add Your API Key

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_api_key_here
```


### 4. Run the Script

```bash
python first_call.py
```

## 🔐 Note
⚠️ Do not commit your API key to GitHub!
