import requests

url = "https://query.wikidata.org/sparql"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
}

query = """
SELECT ?gemeinde ?gemeindeLabel ?uri
WHERE {
  ?gemeinde wdt:P31 wd:Q2027683;
            wdt:P17 wd:Q40;
            wdt:P856 ?uri.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[DE]". }
}
"""

response = requests.get(url, headers=headers, params={"query": query, "format": "json"})
data = response.json()

for item in data["results"]["bindings"]:
    gemeinde_label = item["gemeindeLabel"]["value"]
    uri = item["uri"]["value"]
    print(f"{gemeinde_label}: {uri}")
