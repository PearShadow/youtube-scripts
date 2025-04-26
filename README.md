# YouTube Script Generator

A simple Python tool to generate engaging 5–10 minute cyber-crime video scripts using OpenAI GPT models.

## Features

- Reads 100 topics from `topics.txt`.
- Generates scripts with editor-friendly timestamps.
- Cycles video lengths between 5–10 minutes.
- Sanitizes filenames and saves each script as a `.txt` file in `scripts/`.

## Prerequisites

- Python 3.8 or higher
- OpenAI API key (GPT-3.5-Turbo, GPT-4, or GPT-4-Turbo)
- Virtual environment (recommended)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repo_url> youtube-scripts
   cd youtube-scripts
   ```

2. **Create & activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\\Scripts\\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install openai python-dotenv
   ```

4. **Configure your API key**
   - Copy `.env.example` to `.env`
   - Add your key:
     ```env
     OPENAI_API_KEY=your_api_key_here
     ```

## File Structure

```
youtube-scripts/
├── README.md            # Project overview and instructions
├── generate_scripts.py  # Main script
├── topics.txt           # List of 100 video topics
├── scripts/             # Generated script output (.txt files)
└── .env.example         # Example environment variables file
```

## Usage

```bash
source venv/bin/activate
python generate_scripts.py
```

All scripts will be saved to the `scripts/` folder as `001_<topic>.txt` through `100_<topic>.txt`.

### Generating a Single Script

To test one topic manually, modify `generate_scripts.py` or use Python REPL:

```bash
python
>>> from generate_scripts import generate_script
>>> print(generate_script("Your Topic Here", minutes=7))
```

## Customization

- **Model**: Change `MODEL` in the script (`gpt-3.5-turbo`, `gpt-4`, or `gpt-4-turbo`).
- **Timing**: Adjust length logic in the loop.
- **Prompt**: Edit `PROMPT_TEMPLATE` for voice, structure, or brand guidelines.

## Cost Estimate

- **GPT-3.5-Turbo**: ~\$0.0032 per script → \$0.32 for 100 scripts
- **GPT-4-Turbo**: ~\$0.047 per script → \$4.70 for 100 scripts

