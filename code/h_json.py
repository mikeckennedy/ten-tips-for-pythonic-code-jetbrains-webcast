
# from: http://www.omdbapi.com/
import json

import requests

movie_json = """
{
"Title":"Circuit",
"Year":"2001",
"Runtime":"130 min",
"Country":"USA"
}
"""

movie_data = json.loads(movie_json)
print(movie_data)
print("Movie title from static json:")
print(movie_data['Title'])
print()

url = 'http://www.omdbapi.com/?y=&plot=short&r=json&s=silicon'
resp = requests.get(url)
search_results = resp.json()['Search']
print(search_results)

print("Movies with circuit in title:")
for m in search_results:
    print( " * " + m['Title'])

print()
print("Static dic to json:")
print(json.dumps(movie_data))

