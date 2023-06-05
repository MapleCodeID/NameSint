import aiohttp, requests

async def check_url(session, url) -> bool:
    """
    Check status of requests

    Parameters:
        session (aiohttp.ClientSession): session for making requests
        url (str): url that needs to be checked

    Returns:
        bool: True if the response of the request is good else False
    """

    try:
        async with session.get(url) as response:
            if response.status == 200:
                return True
            else:
                return False
    except aiohttp.ClientError:
        return False


def guette_moi_ça(url):
    response = requests.get(url)

    if response.status_code == 200:
        return "200 ✔️ "
    elif response.status_code == 404:
        return "404 ❌"
    elif response.status_code == 403:
        return "403 ❌"
    elif response.status_code == 301:
        return "301 ❌"
    elif response.status_code == 302:
        return "302 ❌"
    elif response.status_code == 500:
        return "500 ❌"
    elif response.status_code == 502:
        return "502 ❌"
    elif response.status_code == 503:
        return "503 ❌"
    elif response.status_code == 504:
        return "504 ❌"
    elif response.status_code == 401:
        return "401 ❌"