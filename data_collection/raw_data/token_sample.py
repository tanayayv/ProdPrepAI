from transformers import GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Sample phrases to test
sample_phrases = [
    "Design a Jobs Product for Facebook",
    "Primary target users are job seekers and employers looking for qualified candidates.",
    "Enable users to leverage their network for referrals and insights."
]

# Tokenize each phrase and print the results
for phrase in sample_phrases:
    tokens = tokenizer.tokenize(phrase)
    token_ids = tokenizer.convert_tokens_to_ids(tokens)
    print(f"Original Phrase: {phrase}")
    print(f"Tokens: {tokens}")
    print(f"Token IDs: {token_ids}")
    print("-" * 40)
