# Notepat README

## Overview
Notepat is a text editor designed to enhance your writing experience by utilizing the capabilities of the OpenAI API for text analysis and formatting. It allows users to edit text seamlessly while offering formatting suggestions based on the context.

### Text correction

![Alt text](NotePatWindowExample00.png?raw=true "")

![Alt text](NotePatWindowExample01.png?raw=true "")

### Code generation

![Alt text](NotePatWindowExample02.png?raw=true "")

![Alt text](NotePatWindowExample03.png?raw=true "")

### Command context recognition

![Alt text](NotePatWindowExample04.png?raw=true "")

![Alt text](NotePatWindowExample05.png?raw=true "")

## Setup Instructions

### 1. Environment Setup
To run Notepat, ensure you have Python installed on your system. You will also need to install the required packages. Run the following command in your terminal:

```
pip install openai tkinter
```

### 2. Obtaining NOTEPAT_KEY

To use the OpenAI API, you need to generate an API key:

1. **Create an OpenAI Account**: Go to the OpenAI website and sign up for an account if you don't have one.
2. **Access the Developer Dashboard**: After logging in, navigate to the developer dashboard.
3. **Generate an API Key**:
   - Locate the API keys section.
   - Click on "Create API Key" or a similar option.
   - Name your key (e.g., "Notepat Key").
   - Copy the generated key.

### 3. Setting NOTEPAT_KEY

You need to set the `NOTEPAT_KEY` environment variable with the API key you generated. The method depends on your operating system:

- **Windows**:
  1. Open Command Prompt and run:
     ```
     set NOTEPAT_KEY=your_api_key_here
     ```
  
- **macOS/Linux**:
  1. Open Terminal and run:
     ```
     export NOTEPAT_KEY=your_api_key_here
     ```

### 4. Customizing the System Prompt
You can customize the system prompt used by Notepat by creating a file named `custom_prompt.txt` in the same directory as the script. Add your desired prompt content to this file.

If the file is not found, Notepat will run with a default system prompt.

## Running Notepat
To launch Notepat, simply run the script using Python:

```
python notepat.py
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
- If you encounter an error stating that the API key is not found, ensure that you have correctly set the `NOTEPAT_KEY` environment variable.
- If issues arise while opening or saving files, check the file permissions and paths.

Enjoy using Notepat for your text editing needs!

Miguel Campillos - miguelcampillos.com - https://github.com/thesimplesthings/NotePat
MIT License


