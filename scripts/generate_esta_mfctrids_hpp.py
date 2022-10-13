#!/usr/bin/env python3
"""Create a C++ header containing ESTA ManufacturerIDs strings"""
import os

# Location of C++ header file output
outFilename = os.path.dirname(os.path.realpath(__file__)) + '/../esta_mfcrids.hpp'
# Location of C++ header file template
inFilename = os.path.dirname(os.path.realpath(__file__)) + '/../templates/esta_mfcrids.hpp.template'

def main():
    from esta_mfctrids import getESTAmfctrIDs
    from string import Template
    from datetime import timezone, datetime

    # Scrape ESTA and create manufacturers string
    manufacturers = ''
    for item in getESTAmfctrIDs():
        manufacturers += '\t\t\t' + '{' + item['Manufacturer ID'] + ', L"' + item['Company'] + '"s},' + '\n'

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
