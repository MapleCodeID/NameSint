import json, time
import utils
from lib import check_url

class On:
    def check(username):
        """
        Finds the sites where the target is registered 

        Parameters:
            username (str): name targeted enter 

        Returns:
            list: all websites founds
        """

        try:
            with open("data\data.json", "r") as file:
                data = json.load(file)

            print(f"[{utils.YELLOW}🕵️‍♂️{utils.WHITE}] Target name : {utils.YELLOW}{username}{utils.WHITE}\n")

            numbr = 0
            fake = 0
            start = time.time()

            for entry in data:
                url = entry['url'].replace('username', username)

                if check_url.check(url):
                    fake += 1
                    numbr += 1
                    print(f"[{utils.GREEN}!{utils.WHITE}] - {utils.BLUE}{fake}{utils.WHITE} - {utils.GREEN}{entry['site_name']}{utils.WHITE} ({utils.YELLOW}{url}{utils.WHITE}) [{check_url.guette_moi_ça(url)}]")

            print(f"\n[{utils.GREEN}:){utils.WHITE}] Finish ! ({utils.YELLOW}{numbr} results{utils.WHITE}) Time : ({utils.YELLOW}{round(time.time() - start, 1)}s{utils.WHITE})")


        except Exception as e:
            print(e)
            print(":/")
