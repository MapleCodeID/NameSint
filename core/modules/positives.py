import utils
import asyncio
import json
import time
import aiohttp

from LIB import check_url


class Po:
    async def check(username):
        """
        Finds the sites where the target is registered

        Parameters:
            username (str): name targeted enter

        Returns:
            str: all websites founds
        """
        
        try:
            with open("data\data.json", "r") as file:
                data = json.load(file)

            print(f"[{utils.YELLOW}🕵️‍♂️{utils.WHITE}] Target name: {utils.YELLOW}{username}{utils.WHITE}\n")

            numbr = 0
            fake = 0
            start = time.time()

            async with aiohttp.ClientSession() as session:
                tasks = []
                for entry in data:
                    url = entry['url'].replace('username', username)
                    tasks.append(asyncio.create_task(check_url.check_url(session, url)))

                results = await asyncio.gather(*tasks)

            for entry, result in zip(data, results):
                url = entry['url'].replace('username', username)

                if result:
                    numbr += 1
                    fake += 1
                    print(f"[{utils.GREEN}!{utils.WHITE}] - {utils.BLUE}{fake}{utils.WHITE} - {utils.GREEN}{entry['site_name']}{utils.WHITE} ({utils.YELLOW}{url}{utils.WHITE}) [{check_url.guette_moi_ça(url)}]")

            print(f"\n[{utils.GREEN}:){utils.WHITE}] Finish! ({utils.YELLOW}{numbr} results{utils.WHITE}) Time: ({utils.YELLOW}{round(time.time() - start, 1)}s{utils.WHITE})")

        except Exception as e:
            print(e)
            print(":/")
