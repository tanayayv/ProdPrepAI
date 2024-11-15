import json

# Load your data
with open("response.json") as f:
    data = json.load(f)

processed_data = []

for entry in data:
    question = entry["question"]
    response = entry["response"]

    # Flatten the response components
    response_text = f"Understanding the Objective: {response['Understanding the Objective']}. "
    response_text += "Target Audience and Use Cases: "
    response_text += f"{response['Target Audience and Use Cases']['description']} "
    response_text += " ".join(response["Target Audience and Use Cases"]["users"]) + ". "
    response_text += " ".join(response["Target Audience and Use Cases"]["use_cases"]) + ". "
    response_text += "Core Features and Functionality: " + ", ".join(response["Core Features and Functionality"]) + ". "
    response_text += "Differentiation: " + ", ".join(response["Differentiation"]) + ". "
    response_text += "Monetization Strategy: " + ", ".join(response["Monetization Strategy"]) + ". "
    response_text += "Success Metrics: " + ", ".join(response["Success Metrics"]) + ". "

    # Combine question and response into one text field
    text = f"Question: {question}. Response: {response_text}"
    processed_data.append({"text": text})

# Save the processed data
with open(r"processed_data\processed_data.json", "w") as f:
    json.dump(processed_data, f)
