# Class for render DhcpScope from a csv file

## Install as standalone script
1. Clone or download repo
2. Install pip packages from the requirements.txt
    - ``` pip install -r requirements.txt ```

## CSV file requirement
To use this class/script your csv file need to be structure like this
``` 
SiteName,IPNetwork
MySite,10.48.1.0/24

```
## Default values
This variables has default values but can be overwritten
| Variable  | Defult value  | Method to overwrite value |
|-----------|---------------|---------------------------|
| gateway   | 1             | setGateway()              |
| start_range | 2           | setStartRange()           |
| end_range | 254           | setEndRange()             |
| primaryDNS | 8.8.8.8      | setPrimaryDNS()           |
| secondaryDNS | 8.8.4.4    | setSecondaryDNS()         |

## Input and output file
Use this method to set patch to your csv file and output file
| Method | Example |
|--------|---------|
| setPathToCsvFile() | setPathToCsvFile("./Myfile.csv") |
| setPathToSaveOutputFile() | setPathToSaveOutputFile("MyScops.txt") |

## Example usege
### main.py
```python
from ranges import Ranges
scope = Ranges()
scope.setPathToCsvFile("C:\python_play\GenerateDhcpRanges\IP-PLAN.csv")
scope.setPathToSaveOutputFile("dhcpScopes.txt")
scope.setStartRange("100")
scope.setEndRange("200")
scope.generate()
```
