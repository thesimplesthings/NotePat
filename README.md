# ![Alt text](app/assets/images/notepat.png?raw=true "") ![Alt text](app/assets/images/notepat.png?raw=true "") ![Alt text](app/assets/images/notepat.png?raw=true "") Notepat README ![Alt text](app/assets/images/notepat.png?raw=true "") ![Alt text](app/assets/images/notepat.png?raw=true "") ![Alt text](app/assets/images/notepat.png?raw=true "")

## Overview
Notepat is a text editor designed to enhance your writing experience by utilizing the capabilities of the OpenAI API for text analysis and formatting. It allows users to edit text seamlessly while offering formatting suggestions based on the context.

## All the power of GPT with all the beauty of plain text! <3

### Text correction

![Alt text](app/assets/images/NotePatWindowExample00.png?raw=true "")

![Alt text](app/assets/images/NotePatWindowExample01.png?raw=true "")

### Code generation

![Alt text](app/assets/images/NotePatWindowExample02.png?raw=true "")

![Alt text](app/assets/images/NotePatWindowExample03.png?raw=true "")

### Command context recognition

![Alt text](app/assets/images/NotePatWindowExample04.png?raw=true "")

![Alt text](app/assets/images/NotePatWindowExample05.png?raw=true "")
## Setup Instructions

### 1. Environment Setup
To run Notepat, ensure you have `pyenv` installed on your system. Follow these steps to set up the environment:

1. **Install pyenv**: Follow the instructions on the [pyenv GitHub page](https://github.com/pyenv/pyenv#installation) to install `pyenv`.
2. **Install Python 3.12.8**: Run the following command to install the required Python version:
   ```
   pyenv install 3.12.8
   ```
3. **Set Local Python Version**: Navigate to the Notepat directory and set the local Python version:
   ```
   pyenv local 3.12.8
   ```
4. **Install Required Packages**: Use the `requirements.txt` file to install the necessary packages:
   ```
   pip install -r requirements.txt
   ```

### 2. Obtaining CHATGPT_KEY

To use the OpenAI API, you need to generate an API key:

1. **Create an OpenAI Account**: Go to the OpenAI website and sign up for an account if you don't have one.
2. **Access the Developer Dashboard**: After logging in, navigate to the developer dashboard.
3. **Generate an API Key**:
   - Locate the API keys section.
   - Click on "Create API Key" or a similar option.
   - Name your key (e.g., "Notepat Key").
   - Copy the generated key.

### 3. Setting CHATGPT_KEY

You need to set the `CHATGPT_KEY` environment variable with the API key you generated. The method depends on your operating system:

- **.env File**:
  1. Create a file named `.env` in the Notepat root directory.
  2. Add the following line to the file:
     ```
     CHATGPT_KEY=your_api_key_here
     ```

- **Windows**:
  1. Open Command Prompt and run:
     ```
     set CHATGPT_KEY=your_api_key_here
     ```
  
- **macOS/Linux**:
  1. Open Terminal and run:
     ```
     export CHATGPT_KEY=your_api_key_here
     ```

### 4. Customizing the System Prompt
You can customize the system prompt used by Notepat by creating a file named `custom_prompt.txt` in the same directory as the script. Add your desired prompt content to this file.

If the file is not found, Notepat will run with a default system prompt.

### 5. Setting Up Pre-commit Hooks
To ensure code quality, we use pre-commit hooks. Install the pre-commit package and set up the hooks:

1. **Install pre-commit**:
   ```
   pip install pre-commit
   ```
2. **Install the hooks**:
   ```
   pre-commit install
   ```

## Running Notepat
To launch Notepat, simply run the script using Python:

```
python main.py
```

## Features
- **File Management**: Open, save, and edit text files.
- **Text Formatting**: Format selected text using the OpenAI API.
- **Customizable Font Size**: Change the font size for better readability.
- **Help Section**: Access short commands and usage instructions through the Help menu.

## Command Usage
- Use `--to [Language]` to convert selection to specific language code (e.g. `--to C#`).
- Use `--question [text]` to pose a question and receive a response.
- Use `--[custom]` to interpret and execute custom commands.

## Troubleshooting
- If you encounter an error stating that the API key is not found, ensure that you have correctly set the `CHATGPT_KEY` environment variable.
- If issues arise while opening or saving files, check the file permissions and paths.

Enjoy using Notepat for your text editing needs!

Miguel Campillos - miguelcampillos.com - https://github.com/thesimplesthings/NotePat
MIT License
