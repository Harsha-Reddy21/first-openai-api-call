# OpenAI API Call Demo

This script demonstrates making a simple API call to OpenAI's GPT-3.5-turbo model and displaying the response along with token usage.

## What This Script Does

1. Takes user input via console
2. Makes an API call to GPT-3.5-turbo model
3. Displays the assistant's response
4. Shows detailed token usage statistics

## Setup Instructions

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key:
   - Create a `.env` file with:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

3. Run the script:
```bash
python first_call.py
```

## Example

Enter your prompt: What is the reason for kargil war?

Assistant's response:
The Kargil War was fought between India and Pakistan in 1999. The primary reason for the conflict was the infiltration of Pakistani soldiers and militants into the Kargil sector in Indian-administered Kashmir, which is a disputed region between the two countries. Pakistan claimed that it was supporting Kashmiri insurgents, while India viewed the incursion as a direct aggression on its territory. The intrusions led to a full-fledged military conflict that lasted for over two months, resulting in significant casualties on both sides before a ceasefire was brokered.

Token usage:
Total tokens: 136
Prompt tokens: 27
Completion tokens: 109
