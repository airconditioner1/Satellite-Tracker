import requests


def acquire_apod(key):
    api_url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(api_url, params={'api_key': key})

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("apod fetch failed")
        return None



def main():
    api_key = 'R7QYL8yzkLmejHQHrM2tp1OtU37qJz7j8M6sntLA'

    apod_data = acquire_apod(api_key)

    if apod_data:
        image_url = apod_data.get('url')
        print(apod_data)
        print("Title:", apod_data.get('title'))
        print("Date:", apod_data.get('date'))
        print("Explanation:", apod_data.get('explanation'))
        print("URL:", apod_data.get('url'))
    else:
        print("apod not available")

if __name__ == "__main__":
    main()