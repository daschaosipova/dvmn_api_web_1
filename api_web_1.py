import requests


def main():
    locations = ["london", "svo"]
    url_template = "https://wttr.in/{}?nTqu&lang=en"
    for location in locations:
        url = url_template.format(location)
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)

    url = "https://wttr.in/Череповец?nTqmM&lang=ru"
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)


if __name__ == "__main__":
    main()
