#!/usr/bin/env python3
import openai
from openai import OpenAI
import os
import sys
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)


def get_command(question):
    try:
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a translator from text to MacOS terminal. Answer just a pure terminal command line which you are suggesting. Nothing else. YOU WILL BE SERIOUSLY PUNISHED FOR EACH EXTRA SYMBOL."},
                {"role": "user", "content": question},
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 script.py 'Your natural language question'")
        sys.exit(1)

    question = " ".join(sys.argv[1:])

    suggested_command = get_command(question)

    print(f"Suggested command: {suggested_command}")

    execute = input(f"Execute {suggested_command}? [y/N] ").lower().strip()
    if execute == 'y':
        os.system(suggested_command)


if __name__ == "__main__":
    main()
