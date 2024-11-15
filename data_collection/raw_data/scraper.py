from bs4 import BeautifulSoup
from collections import defaultdict
from prettytable import PrettyTable

# Read HTML content from a file
file_path = 'daily_prod_prep.html'  # Replace with the path to your HTML file
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find all problem cards
problem_cards = soup.find_all('a', class_='card')

# Extract titles and topics
problems = []
for card in problem_cards:
    title = card.find('h3', class_='problem-title').get_text(strip=True)
    topics = card.find('div', class_='details').find_all('p', class_='pill')
    topic_list = [topic.get_text(strip=True) for topic in topics]
    
    problems.append({'title': title, 'topics': topic_list})

# Define the categories
categories = {
    'Diagnosis': [],
    'Design a product': [],
    'Measure success': [],
    'Technical': [],
    'Improve a product': [],
    'Fermi': [],
    'Strategy': []
}

# Categorize the titles based on topics
for problem in problems:
    for topic in problem['topics']:
        if topic in categories:
            categories[topic].append(problem['title'])

# Print the categorized titles
for category, titles in categories.items():
    print(f"{category}:")
    for title in titles:
        print(f" - {title}")
    print()