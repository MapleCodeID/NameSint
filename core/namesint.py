import utils
import argparse
import asyncio

from modules import positives, search, version, name_site


async def name():
    opt = f"""
                                        {utils.RED}_____{utils.WHITE}       {utils.RED}_____{utils.WHITE}
{utils.RED}_____________ _______ __________________{utils.WHITE}(_){utils.RED}________  {utils.WHITE}/_
{utils.RED}__{utils.WHITE}  __ \  __ `/_  __ `__ \  _ \_  ___/_  /__  __ \  __/
{utils.RED}_{utils.WHITE}  / / / /_/ /_  / / / / /  __/(__  )_  / _  / / / /_  
/_/ /_/\__,_/ /_/ /_/ /_/\___//____/ /_/  /_/ /_/\__/  """
    text = """
            using OSINT✨
        https://github.com/N0rz3


Usage: python namesint.py [-h] {--search, --positives} ...

Options:
-h, --help                      show this help message and exit
-s, --search                    Find all target accounts
-p, --positives                 Show positives accounts
-v, --version                   Displays the version of the tool
-ns, --name_site                lists all sites
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--search", help="Find all target accounts")
    parser.add_argument("-p", "--positives", help="Show positives accounts")
    parser.add_argument("-v", "--version", help="Displays the version of the tool", action="store_true")
    parser.add_argument("-ns", "--name_site", action="store_true")
    args = parser.parse_args()

    if args.search:
        print(utils.banner)
        user = args.search
        await search.User.check(user)
        exit()

    elif args.positives:
        print(utils.banner)
        only = args.positives
        await positives.Po.check(only)
        exit()

    elif args.version:
        print(version.ver())
        exit()

    elif args.name_site:
        print(name_site.get_websites())
        exit()

    else:
        print(opt)
        print(text)
        exit()


if __name__ == "__main__":
    asyncio.run(name())