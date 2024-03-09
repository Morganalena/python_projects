"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Alena Morgan
email: Alena.karnosova@gmail.com
discord: morganalena
"""

import requests
from bs4 import BeautifulSoup
import csv
import sys

def server_response(url):
    """
    Sends a GET request to the URL and returns parsed HTML content.
    """
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")

def location_code(soup):
    """
    Extracts location codes from the given `soup`. 
    """
    code_tags = soup.find_all("td", class_="cislo")  
    codes = []
    for code in code_tags:
        a_tag_codes = code.find("a")
        if a_tag_codes:  
            codes.append(a_tag_codes.get_text())  
    return codes

def location_name(soup):
    """
    Extracts location names from the given `soup`. 
    """
    name_tags = soup.find_all("td", class_="overflow_name")  
    names = []
    for name in name_tags:
        names.append(name.get_text())
    return names

def list_of_links(soup, codes):
    """
    Extracts links to individual municipalities based on the provided codes from the given `soup`.
    """
    links_for_municipalities = []
    base_link = "https://volby.cz/pls/ps2017nss/"
    divs_with_class_t3 = soup.find_all("div", class_="t3")
    
    for links_div in divs_with_class_t3:
        links = links_div.find_all("a", href=True) 
        for link in links:
            href = link.get("href")
            if href and "ps311" in href: # Check if the link contains "ps311"
                absolute_link = base_link + href
                village_code = href.split("=")[-2].split("&")[0]
                if village_code in codes:
                    links_for_municipalities.append(absolute_link)
    
    return links_for_municipalities

def get_td_tags_from_links(links):
    """
    Extracts td tags from each link provided in list_of_links.
    """
    td_tags_list = []

    for link in links:
        response = requests.get(link)
        municipality_soup = BeautifulSoup(response.content, 'html.parser')
        td_tags = municipality_soup.find_all("td", headers=True)
        td_tags_list.append(td_tags)

    return td_tags_list

def all_votes(municipality_links):
    """
    Gets registered voters, envelopes, and valid votes for each municipality.
    """
    registered, envelopes, valid = [], [], []

    td_tags_list = get_td_tags_from_links(municipality_links)

    for td_tags in td_tags_list:
        for td in td_tags:
            if "sa2" in td["headers"]:
                registered.append(td.get_text().replace('\xa0', '').strip())
            elif "sa3" in td["headers"]:
                envelopes.append(td.get_text().replace('\xa0', '').strip())
            elif "sa6" in td["headers"]:
                valid.append(td.get_text().replace('\xa0', '').strip())
    
    return registered, envelopes, valid

def parties_votes(municipality_links):
    """
    Gets votes for each party in each municipality.
    """
    names_of_parties, votes_for_parties = [], []
    td_tags_list = get_td_tags_from_links(municipality_links)
    
    for td_tags in td_tags_list:
        for td in td_tags:
            if ("t1sa1" in td["headers"] or "t2sa1" in td["headers"]) and "overflow_name" in td["class"]:
                names_of_parties.append(td.get_text().strip())
            elif ("t1sb3" in td["headers"] or "t2sb3" in td["headers"]) and "cislo" in td["class"]:
                votes_for_parties.append(td.get_text().replace('\xa0', '').strip())
    
    parties_dict = {}
    for party_name in names_of_parties: 
        parties_dict[party_name] = []
    
    for party_name, vote in zip(names_of_parties, votes_for_parties):
        parties_dict[party_name].append(vote)
    
    return parties_dict

def table_headers(parties_dict):
    """
    Generates CSV file headers.
    """
    header = ["Code", "Location", "Registered", "Envelopes", "Valid"]
    for party in parties_dict.keys(): 
        header.append(party)
    return header

def check_arguments(args):
    """
    Validates command-line arguments.
    """
    if len(sys.argv) != 3:
        print("Please provide both the URL and the file name.")
        sys.exit(1)
    
    if "https://volby.cz/pls/ps2017nss/" not in args[1]:
        print("The provided URL is not valid.")
        sys.exit(1)
    
    elif not args[2].endswith(".csv"):
        print("The file name should end with '.csv'.")
        sys.exit(1)
    
    return args[1], args[2]

def main(url,file_name):
    """
    Process the scraping and CSV file creation.
    """
    try:
        print("-" * 73)
        print("Data processing...")
        print("URL:", url)
        print("File Name:", file_name)
        print("-" * 73) 
        soup = server_response(url)
        codes = location_code(soup)
        names = location_name(soup)
        municipality_links = list_of_links(soup, codes)
        registered, envelopes, valid = all_votes(municipality_links)
        parties_dict = parties_votes(municipality_links)

    except AttributeError:
        print("Unexpected error, ending the program")
        sys.exit(1)
    
    csv_file_path = file_name

    with open(csv_file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(table_headers(parties_dict))
        for code, name, reg, env, val in zip(codes, names, registered, envelopes, valid):
            row = [code, name, reg, env, val]
            for party in parties_dict.keys():
                row.append(parties_dict[party][0])
                parties_dict[party].pop(0)
            writer.writerow(row)

        print(f"CSV file {file_name} created successfully.\nThank you for using this election-scraper.")

if __name__ == '__main__':
    url, file_name = check_arguments(sys.argv)
    main(url, file_name)
