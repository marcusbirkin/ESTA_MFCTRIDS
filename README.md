# ESTA_MFCTRIDS
Scrapes https://tsp.esta.org/tsp/working_groups/CP/mfctrIDs.php to create importable headers of ESTA ManufacturerIDs strings for use in projects.

#### Nota bene regarding data uniqueness
The Manufacturer ID should not be treated, in it's raw form, as a unique/primary key.   
The source data does contain duplicate entries and other quirks ([#2](https://github.com/marcusbirkin/ESTA_MFCTRIDS/issues/2))
> Example
> | Manufacturer ID   | Company |
> | ----------------- |-------- |
> | 0000h             | ESTA    |
> | 0000h             | PLASA   |

## C++

### Script
generate_esta_mfctrids_hpp.py

### Importable item
esta_mfcrids.hpp

## CSV

### Script
generate_esta_mfctrids_csv.py

### Importable item
esta_mfcrids.csv

## JSON

### Script
generate_esta_mfctrids_json.py

### Importable item
esta_mfcrids.json
