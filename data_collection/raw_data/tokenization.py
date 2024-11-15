from transformers import GPT2Tokenizer
import json

# Initialize tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Set the padding token to the end-of-sequence token
tokenizer.pad_token = tokenizer.eos_token

# Initialize lists
tokenized_data = []
processed_data = []

# Load processed data
with open('processed_data.json', 'r') as file:
    processed_data = json.load(file)

# Tokenize data
for entry in processed_data:
    try:
        text = entry["text"]
        tokens = tokenizer(text, padding="max_length", truncation=True, max_length=256)
        tokenized_data.append(tokens["input_ids"])
    except KeyError as e:
        print(f"Key error: {e}. Please check the JSON structure.")
        continue

# Print the first few tokenized entries for verification
print(tokenized_data[:5])
