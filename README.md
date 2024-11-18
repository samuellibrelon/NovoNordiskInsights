# NovoNordiskInsights - AI Text Generation Project with GPT-Neo

This project integrates OpenAI's GPT-Neo model with a custom JSON database to generate relevant insights and responses based on specific data. This tool is designed to demonstrate skills in natural language processing, API integration, and data processing for topics such as innovation and sustainability.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
This repository leverages the GPT-Neo model by EleutherAI to generate textual responses based on prompts related to environmental initiatives, innovation, and other topics within the context of the provided JSON data. The JSON database serves as a structured input, allowing for dynamic and relevant responses without the need for a continuously active API subscription.

## Features
- **NLP-Powered Text Generation**: Generate high-quality text outputs with GPT-Neo.
- **JSON Integration**: Seamlessly read data from a JSON database for customized responses.
- **OpenAI API Integration**: Use OpenAI models for text generation (alternative models can also be used).
- **Environmentally Focused Insights**: Tailored for generating insights on innovation, sustainability, and related themes.

## Prerequisites
- Python 3.7 or later
- An OpenAI API key (for optional OpenAI GPT models)
- JSON file with relevant data (see example format below)
- Git

## Setup

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/yourprojectname.git
    cd yourprojectname
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**
   Create a `.env` file in the root directory with your OpenAI API key:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key_here
    ```

4. **Prepare the JSON Data**
   Ensure your JSON file follows this structure:
   ```json
   [
     {
       "title": "Innovation in Novo Nordisk",
       "content": "Novo Nordisk focuses on sustainable solutions...",
       "category": "Innovation",
       "date": "2024-11-10"
     },
     {
       "title": "Environmental Impact",
       "content": "Novo Nordisk aims to achieve zero environmental impact...",
       "category": "Sustainability",
       "date": "2024-11-10"
     }
   ]
## Usage

```python
# Run the Script with a Basic Prompt Input
# Replace 'your_script.py' with the actual name of your script file

python your_script.py

# Sample Code to Run with a Prompt
prompt = "Discuss sustainability efforts at Novo Nordisk."
response = generate_text(prompt)
print(response)
```
## Project Structure

```plaintext
AI_Text_Generation_Project/
├── README.md                   # Project overview and usage instructions
├── data.json                   # JSON file with context data
├── main_script.py              # Main script for running the text generation
├── requirements.txt            # Python dependencies
├── .env                        # Environment file for sensitive data
└── model/                      # Directory to store downloaded models
    └── gpt-neo-2.7B/           # Folder for specific model files (e.g., GPT-Neo 2.7B)
```

## Contributing

Feel free to contribute by submitting pull requests. For major changes, open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
