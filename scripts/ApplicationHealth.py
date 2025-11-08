import requests

URL = "https://wisecow.local"

def check_app_status():
    try:
        response = requests.get(URL, timeout=5)
        if response.status_code == 200:
            print(f"Application is UP. Status code: {response.status_code}")
        else:
            print(f"Application might be DOWN. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Application is DOWN. Error: {e}")

if __name__ == "__main__":
    check_app_status()
