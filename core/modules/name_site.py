import json
import utils

def get_websites():
    """
    Prints a list of all websites used in the database in JSON format

    
    Return:
        list: all websites used

    """

    with open("data/data.json", "r") as file:
        data = json.load(file)

    website_list = []
    num = 0

    for entry in data:
        website = entry['site_name']
        cleaned_website = website.replace(",", "").replace("[", "").replace("]", "").replace("'", "") + "\n"
        num += 1

        result_website = f"{utils.BLUE}#{num}{utils.WHITE} - {utils.GREEN}{cleaned_website}{utils.WHITE}"
        website_list.append(result_website)


    websites_text = "".join(website_list)
    
    return websites_text