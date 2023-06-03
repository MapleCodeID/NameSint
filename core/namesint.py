import utils
import argparse

from modules import only_find, username, version


if __name__ == "__main__":
    opt = f"""

                                      {utils.RED}_____{utils.WHITE}       {utils.RED}_____{utils.WHITE}
{utils.RED}_____________ _______ __________________{utils.WHITE}(_){utils.RED}________  {utils.WHITE}/_
{utils.RED}__{utils.WHITE}  __ \  __ `/_  __ `__ \  _ \_  ___/_  /__  __ \  __/
{utils.RED}_{utils.WHITE}  / / / /_/ /_  / / / / /  __/(__  )_  / _  / / / /_  
/_/ /_/\__,_/ /_/ /_/ /_/\___//____/ /_/  /_/ /_/\__/  """
                                                                                    
    text = """
            using OSINT✨
        https://github.com/N0rz3


Usage: python namesint.py [-h] {--search, --only_find} ...

Options:
-h, --help                      show this help message and exit
-s, --search                    Find all target accounts
-o, --only_find                 Show only found accounts
-v, --version                   Displays the version of the tool
"""

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--search", help="Find all target accounts")
    parser.add_argument("-o", "--only_find", help="Show only found accounts")
    parser.add_argument("-v", "--version", help="Displays the version of the tool", action="store_true")
    args = parser.parse_args()

    if args.search:
        print(utils.banner)
        user = args.search
        username.User.check(user)
        exit()

    elif args.only_find:
        print(utils.banner)
        only = args.only_find
        only_find.On.check(only)
        exit()


    elif args.version:
        print(version.ver())
        exit()

    else:
        print(opt)
        print(text)
        exit()