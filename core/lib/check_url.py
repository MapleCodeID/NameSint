import requests

def check(url) -> bool:
        """
        Check status of requests 


        Parameters:
            url (str): url that needs to be checked 

        Returns:
            bool: True if the responds of the request is good else False
        """

        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
            

            else:
                return False

        except requests.exceptions.RequestException:
            return False
    

def gette_moi_ça(url):
    
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
