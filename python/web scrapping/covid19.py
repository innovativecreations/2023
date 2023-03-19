import requests
import bs4
class Covid19:
    r = requests.get(url="https://www.mygov.in/covid-19")

    soup = bs4.BeautifulSoup(r.content, "html.parser")

    # print(soup.prettify())

    table = soup.find(id="_indiatable")
    # print(table.prettify())
    # stateD = table.find()

    # print(stateD.prettify())

    print(f"naman = {__name__}")

