import requests
from bs4 import BeautifulSoup

# Make a request to the website
r = requests.get("http://www.example.com")
r.content

# Use the 'html.parser' to parse the page
soup = BeautifulSoup(r.content, 'html.parser')

# Find all the paragraph tags
paragraphs = soup.find_all('p')

# Open a file to write to
with open('output.txt', 'w') as f:
    # Loop through each paragraph
    for paragraph in paragraphs:
        # Write the paragraph text to the file
        f.write(paragraph.get_text())
        f.write('\n')  # Add a newline to separate paragraphs