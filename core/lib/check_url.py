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
