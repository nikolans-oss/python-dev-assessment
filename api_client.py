import requests

def fetch_and_display_users(num_users):

    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout = 10)

        response.raise_for_status()

        users = response.json()

        if not isinstance(users, list):
            raise ValueError("Epected a list of users, but received a different format.")
        
        print(f"\n--Successfully fetched first {num_users} user(s)--")

        for i in range(min(num_users, len(users))):
            user = users[i]

            name = user.get("name", "N/A")
            email = user.get("email", "N/A")

            address = user.get("address")
            city = (
                address.get("city", "N/A")
                if isinstance(address, dict)
                else "N/A"
            )
            
            print(f"User #{i+1}:")
            print(f"  Name:  {name}")
            print(f"  Email: {email}")
            print(f"  City:  {city}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error occurred: {http_err}")
        return None
    except requests.exceptions.RequestException as net_err:
        print(f"Network Error occurred: {net_err}")
        return None
    except (ValueError, KeyError, TypeError) as data_err:
        print(f"Data Processing Error (Unexpected JSON structure): {data_err}")
        return None
    
fetch_and_display_users(4)

fetch_and_display_users(16)