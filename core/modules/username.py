import json, time
import utils
from lib import check_url

class User:
    def check(username):
        """
        Finds the sites where the target is registered

        Parameters:
            username (str): name targeted enter

        Returns:
            list: all websites founds and not founds
        """

        try:
            with open("data\data.json", "r") as file:
                data = json.load(file)

            print(f"[{utils.GREEN}*{utils.WHITE}] Target name : {utils.GREEN}{username}{utils.WHITE}\n")

            numbr = 0
            start = time.time()

            for entry in data:
                url = entry['url'].replace('username', username)

                if check_url.check(url):
                    numbr += 1
                    print(f"[{utils.GREEN}!{utils.WHITE}] {utils.GREEN}{entry['site_name']}:{utils.WHITE} {url}")
                
                else:
                    print(f"[{utils.RED}x{utils.WHITE}] {utils.RED}{entry['site_name']}:{utils.WHITE} {url}")


            print(f"\n[{utils.RED}!{utils.WHITE}] Finish ! {utils.GREEN}{numbr}{utils.WHITE} results in {round(time.time() - start, 1)}s !")

        except Exception as e:
            print(e)
            print(":/")
