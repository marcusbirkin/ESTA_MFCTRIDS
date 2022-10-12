#!/usr/bin/env python
import os

# Live copy of ESTA Control Protocols Working Group Manufacturer IDs
url = 'https://tsp.esta.org/tsp/working_groups/CP/mfctrIDs.php'
# Location of C++ header file output
outFilename = os.path.dirname(os.path.realpath(__file__)) + '/../esta_mfcrids.hpp'
# Location of C++ header file template
inFilename = os.path.dirname(os.path.realpath(__file__)) + '/../templates/esta_mfcrids.hpp.template'

# Download the live list
def getESTAmfctrIDs():
    import unicodedata
    import urllib.request
    print('Reading' , url)
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' # Fake user agent to prevent 403 Forbidden
    headers = {'User-Agent': user_agent}
    req = urllib.request.Request(url, {}, headers)
    with urllib.request.urlopen(req) as response:
       return response.read()

def main():
    import os
    from string import Template
    from datetime import timezone, datetime
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(getESTAmfctrIDs(), 'html.parser')
    table = soup.find("table", attrs={"id":"main_table"})

    headers = [th.get_text() for th in table.find("tr").find_all("th")]

    # Process manufacturer strings
    manufacturers = ''
    for row in table.find_all("tr")[1:]:
        data = [td.get_text() for td in row.find_all("td")]

        mfctrId = data[0].strip()
        mfctrId = '0x' + mfctrId[:-1] # Remove trailing 'h', and prepend '0x'

        company = data[2].strip()
        company = company.replace('"', '\'')

        manufacturers += '\t\t\t' + '{' + mfctrId + ', L"' + company + '"s},' + '\n'

    # Process template
    print('Reading template', inFilename)
    with open(inFilename, 'r', encoding='utf-8-sig') as inputFile:
        print('Processing template')
        input = Template(inputFile.read())  
        output = input.substitute({
            # Scrape Date and Time
            'SCRAPEDATETIME': datetime.now().astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
            # Scraped Manufacturers strings
			'SCRAPEMANUFACTURERS': manufacturers
        
        })
        with open(outFilename, 'w', encoding="utf-8-sig") as outputFile:
            print('Writing', outFilename)
            outputFile.write(output)
    
    print('Finished')

if __name__ == "__main__":
    main()
