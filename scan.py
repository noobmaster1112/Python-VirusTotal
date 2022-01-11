import requests

# Contains API related secret data
import config 

URL = "https://www.virustotal.com/api/v3/"

# Checks for API related errors
def api_check(resp):
    if r.status_code == 401:
        print("ERROR: Check your API key")
        return False
    elif r.status_code == 429:
        print("ERROR: Quota exeeded")
        return False
    elif r.status_code in [400,403,404,409,424,503,504]:
        print("ERROR: Something went wrong")
        return False
    else:
        return True


if __name__ == "__main__":
    api_check()
