import re


# def give_clean_string(str):
#     return str; 




import openai
from keys import OPENAI_API_KEY
from prompts import create_prompt, INITIAL_RESPONSE
import time

openai.api_key = OPENAI_API_KEY

def generate_response_from_transcript(transcript):
    try:
        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0301",
                messages=[{"role": "system", "content": create_prompt(transcript)}],
                temperature = 0.0
        )
    except Exception as e:
        print(e)
        return ''
    full_response = response.choices[0].message.content
    try:
        return full_response.split('[')[1].split(']')[0]
    except:
        return ''
    


def clean_text_file(input_file, output_file, gpt_file):
    try:
        # Open the input file for reading
        with open(input_file, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return
    except IOError:
        print(f"Error: Failed to read input file '{input_file}'.")
        return

    # Define the pattern to match ["string content"]
    pattern = r'\[([^]]+)\]'

    # Remove the patterns using regular expressions
    cleaned_text = re.sub(pattern, '', text)

    print(cleaned_text)

    full_response = generate_response_from_transcript(cleaned_text) 
    print(full_response)


    try:
        # Open the output file for writing and write the cleaned text
        with open(gpt_file, 'w') as file:
            file.write(full_response)
    except IOError:
        print(f"Error: Failed to write to output file '{gpt_file}'.")
        return

    print("Text file cleaned and saved to:", gpt_file)


    try:
        # Open the output file for writing and write the cleaned text
        with open(output_file, 'w') as file:
            file.write(cleaned_text)
    except IOError:
        print(f"Error: Failed to write to output file '{output_file}'.")
        return

    print("Text file cleaned and saved to:", output_file)


input_file = 'recorded_audio.wav.txt'  # Replace with your input file path
output_file = 'output.txt'  # Replace with your output file path
gpt_file = "output_gpt.txt"

clean_text_file(input_file, output_file, gpt_file)

