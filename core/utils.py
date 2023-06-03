import utils

"""
utils is a file where we find things that are used for the proper functioning of the script

List:
    - all colors used
    - banner
    - variables dunder
    - headers
"""


__author__ = "N0rz3"
__github__ = f"https://github.com/{__author__}"
__license__ = "GNU Public License V3"



text = "using OSINT✨"

# List all colors used
"""
Colors palette used -> https://www.webucator.com/article/python-color-constants-module/
Color rgb example (205,102,0) => Functional rgb color in python scripts example (\033[38;2;205;102;0m)
"""

WHITE = "\033[38;2;255;255;255m"
RED = "\033[38;2;255;64;64m"
GREEN = "\033[38;2;84;255;159m"


# Banner used
banner = f"""
{utils.WHITE}[{utils.GREEN}v0.0.1{utils.WHITE}]

                                      {utils.RED}_____{utils.WHITE}       {utils.RED}_____{utils.WHITE}
{utils.RED}_____________ _______ __________________{utils.WHITE}(_){utils.RED}________  {utils.WHITE}/_
{utils.RED}__{utils.WHITE}  __ \  __ `/_  __ `__ \  _ \_  ___/_  /__  __ \  __/
{utils.RED}_{utils.WHITE}  / / / /_/ /_  / / / / /  __/(__  )_  / _  / / / /_  
/_/ /_/\__,_/ /_/ /_/ /_/\___//____/ /_/  /_/ /_/\__/ 
                                                       

            {text}                                        
        {__github__}       
"""


# headers for requests
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5"
}