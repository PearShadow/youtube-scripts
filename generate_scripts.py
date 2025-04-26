# generate_scripts.py

import os
import time
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# 1) Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not set in environment.")

# 2) Initialize client
client = OpenAI(api_key=api_key)

# 3) Config
OUTPUT_DIR = Path("scripts")
OUTPUT_DIR.mkdir(exist_ok=True)
MODEL = "gpt-3.5-turbo"  # or "gpt-4"

# 4) Prompt template
PROMPT_TEMPLATE = """
You are a professional YouTube script writer for a cyber-crime channel.
Your brand voice is: informative, suspenseful, clear, and engaging.

Write a script for a {length}-minute YouTube video on the topic:
“{topic}”

Structure:
1. Hook (15–30 seconds)
2. Background/context
3. Main narrative: step-by-step or story-driven
4. Key takeaways
5. Call to action (subscribe, like, comment)

Aim for approximately {word_count} words total.
Include timestamps (e.g. [0:00], [0:30], [1:00], …) to guide the editor.
"""

# 5) Core generation function
def generate_script(topic: str, minutes: int = 7) -> str:
    word_count = minutes * 150
    prompt = PROMPT_TEMPLATE.format(
        topic=topic,
        length=minutes,
        word_count=word_count
    )

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user",   "content": prompt}
        ],
        temperature=0.7,
        max_tokens=word_count * 2
    )

    return response.choices[0].message.content.strip()

# 6) Main loop
def main():
    topics_path = Path("topics.txt")
    if not topics_path.exists():
        print("Error: topics.txt not found in project root.")
        return

    topics = [line.strip() for line in topics_path.read_text().splitlines() if line.strip()]
    total  = len(topics)

    for idx, topic in enumerate(topics, start=1):
        minutes = 5 + ((idx - 1) % 6)  # cycles 5 → 10
        print(f"[{idx}/{total}] Generating ({minutes}-min): {topic}")
        script = generate_script(topic, minutes)

        # sanitize filename
        safe = "".join(c if c.isalnum() or c == " " else "_" for c in topic)[:50].strip().replace(" ", "_")
        out_file = OUTPUT_DIR / f"{idx:03d}_{safe}.txt"

        with open(out_file, "w", encoding="utf-8") as f:
            f.write(script)

        time.sleep(1)  # avoid rate‐limit

if __name__ == "__main__":
    main()
