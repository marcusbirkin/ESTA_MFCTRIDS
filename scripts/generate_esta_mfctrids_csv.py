#!/usr/bin/env python3
"""Create a CSV file containing ESTA ManufacturerIDs strings"""
import os

# Location of CSV file output
outFilename = os.path.dirname(os.path.realpath(__file__)) + '/../esta_mfcrids.csv'

def main():
    from esta_mfctrids import getESTAmfctrIDs
    import csv

    # Scrape ESTA
    manufacturers = getESTAmfctrIDs()

    # Create CSV
    with open(outFilename, 'w', encoding='utf-8-sig') as outputFile:
        print('Writing', outFilename)
        output = csv.writer(outputFile)
        output.writerow(manufacturers[0].keys())
        for manufacturer in manufacturers:
            output.writerow(manufacturer.values())

    print('Finished')

if __name__ == "__main__":
    main()