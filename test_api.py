import requests
import json

search_term = "the lord of the rings"
search_term_formatted = search_term.replace(" ", "+")
fields = ["title", "author_name"]
fields_formatted = ",".join(fields)
limit = 1

url = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

print(f"Fetching: {url}")
response = requests.get(url)

# Check status code
print(f"Status code: {response.status_code}")

# Print raw response content
print("\nRaw Content:")
print(response.content)

# Try to parse JSON
try:
    data = response.json()
    print("\nParsed JSON:")
    print(json.dumps(data, indent=2))
except Exception as e:
    print("Error parsing JSON:", e)
