import requests

def get_users_information():
    url = "https://ipapi.co/json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

if __name__ == "__main__":
    data = get_users_information()
    print(data)
