#!/usr/bin/env python3
"""Create a JSON file containing ESTA ManufacturerIDs strings"""
import os
from textwrap import indent

# Location of CSV file output
outFilename = os.path.dirname(os.path.realpath(__file__)) + '/../esta_mfcrids.json'

def main():
    from esta_mfctrids import getESTAmfctrIDs
    import json
    from datetime import timezone, datetime

    # Scrape ESTA
    manufacturers = getESTAmfctrIDs()

    # Format dictionary to include datetime
    outputDict = {}
    outputDict['Last Updated'] = datetime.now().astimezone(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    outputDict['Manufacturers'] = manufacturers

    # Create JSON
    with open(outFilename, 'w', encoding='utf-8-sig') as outputFile:
        print('Writing', outFilename)
        json.dump(outputDict, outputFile, indent=2)

    print('Finished')

if __name__ == "__main__":
    main()