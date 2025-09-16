# lib/open_library_api.py

import requests
import json


class Search:
    
 def get_search_results_json(self):
    # Same search, but returns JSON
    search_term = "the lord of the rings"
    search_term_formatted = search_term.replace(" ", "+")

    fields = ["title", "author_name"]
    fields_formatted = ",".join(fields)
    limit = 1

    URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
    print(f"Requesting URL: {URL}")

    response = requests.get(URL)
    print(f"Response status code: {response.status_code}")
    print(f"Raw content preview (first 200 bytes): {response.content[:200]}")

    try:
        data = response.json()
        return data
    except Exception as e:
        print(f"Failed to parse JSON: {e}")
        return {}

    def get_search_results(self):
        # Static search term
        search_term = "the lord of the rings"
        search_term_formatted = search_term.replace(" ", "+")

        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

        response = requests.get(URL)
        return response.content

   

        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
        print(f"Requesting URL: {URL}")

        response = requests.get(URL)
        return response.json()

    def get_user_search_results(self, search_term):
        # Dynamic search using user input
        search_term_formatted = search_term.replace(" ", "+")

        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://openlibrary.org/search.json?title={search_term_formatted}&fields={fields_formatted}&limit={limit}"

        response = requests.get(URL).json()

        # If no books found
        if len(response['docs']) == 0:
            return "No results found."

        book = response['docs'][0]
        title = book.get('title', 'Unknown Title')
        author = ", ".join(book.get('author_name', ['Unknown Author']))

        return f"Title: {title}\nAuthor: {author}"


# ─── TEST CODE ───

# Option 1: Raw content output
# results = Search().get_search_results()
# print(results)

# Option 2: JSON output, nicely formatted
# results_json = Search().get_search_results_json()
# print(json.dumps(results_json, indent=1))

# Option 3: User-driven search

results_json = Search().get_search_results_json()
print(json.dumps(results_json, indent=1))

