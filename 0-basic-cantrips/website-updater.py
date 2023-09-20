import requests

def get_last_modified(url):
    try:
        response = requests.head(url, allow_redirects=True)
        # print("response is this: ", response.headers)
        last_modified = response.headers.get('last-modified')
        if last_modified:
            return last_modified
        else:
            return "Last modified date not found in HTTP headers."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    while(1):
        website_url = input("Enter the URL of the website you want to check: ")
        last_modified_date = get_last_modified(website_url)
        print(f"Last Modified Date: {last_modified_date}")