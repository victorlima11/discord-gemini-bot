# Discord Bot with Gemini AI

## [Portuguese](readme-pt.md)

## About the Project  
This is a Discord bot that uses the Gemini AI API to answer questions and interact with users. The bot allows direct queries to the AI through customizable commands, including aliases and private response options.

## Features  
- Integration with the Gemini AI API  
- `!gemini (prompt)` to start.

## Installation and Setup  
### 1. Clone the repository  
```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
```

### 2. Create and activate a virtual environment (optional but recommended)  
```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
```

### 3. Install dependencies  
```bash
    pip install -r requirements.txt
```

### 4. Configure environment variables  
Create a `.env` file in the root of the project and add:  
```
DISCORD_TOKEN=your_discord_token
GEMINI_KEY=your_gemini_api_key
```

### 5. Run the bot  
```bash
    python main.py
```

## How to Use  
In Discord, use:  
```bash
!gemini What is the meaning of life?
```
The bot will respond directly in the chat.

## Contribution  
1. Fork the repository  
2. Create a branch (`feature/my-feature`)  
3. Make your changes and commit (`git commit -m "My improvement"`)  
4. Submit a Pull Request

