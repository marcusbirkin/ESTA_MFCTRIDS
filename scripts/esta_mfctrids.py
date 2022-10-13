#!/usr/bin/env python3

def getESTAmfctrIDs():
    """Scrape the ESTA website and return a list of registered manufacturer IDs

    Returns:
        List of Dictionaries: List of Manufacturer details
    """
    import unicodedata
    import urllib.request
    from bs4 import BeautifulSoup

    # Live copy of ESTA Control Protocols Working Group Manufacturer IDs
    url = 'https://tsp.esta.org/tsp/working_groups/CP/mfctrIDs.php'

    # Download
    print('Reading' , url)
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' # Fake user agent to prevent 403 Forbidden
    headers = {'User-Agent': user_agent}
    req = urllib.request.Request(url, {}, headers)
    with urllib.request.urlopen(req) as response:
        # Extract table
        soup = BeautifulSoup(response.read(), 'html.parser') 
        table = soup.find("table", attrs={"id":"main_table"})
        tblHeaders = [th.get_text() for th in table.find("tr").find_all("th")]

        # Extract manufacturer details
        manufacturers = []
        for row in table.find_all("tr")[1:]:
            manufacturer = {}
            data = [td.get_text() for td in row.find_all("td")]

            # Manufacturer ID
            mfctrId = data[0].strip()
            mfctrId = '0x' + mfctrId[:-1] # Remove trailing 'h', and prepend '0x'
            manufacturer['Manufacturer ID'] = mfctrId

            # Organization Name
            orgName = data[1].strip()
            manufacturer['Organization Name'] = orgName

            # Company
            company = data[2].strip()
            company = company.replace('"', '\'')
            manufacturer['Company'] = company

            # Formally Registered
            registered = data[3].strip()
            manufacturer['Registered'] = registered

            manufacturers.append(manufacturer)

        # Return list
        print('Processed', len(manufacturers), 'manufacturers')
        return manufacturers