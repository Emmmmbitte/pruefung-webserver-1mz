# import necessary modules
from bs4 import BeautifulSoup
import requests
import json




def main():
    # get the URL in a useable form
    url = "http://localhost:5000/scraping"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # define filter function
def filter_func(elem):
    return True

# apply filter function
table_rows = list(filter(filter_func, table_rows))


    # select your objects

    elements = [elem for elem in soup.select("scrape-this")]
    print(f"Es wurden {len(elements)} Elemente gefunden.")

    data = []

    for i, elem in enumerate(elements):
        data.append({"id": i, "name": elem.text.strip()})

    with open("data.json", 'w') as f:
        json.dump(data, f, indent=4)

       



if __name__ == "__main__":
    main()
