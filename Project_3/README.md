# Python_project3 - Election Scraper 
- **Author:** Alena Morgan
- **Discord:** morganalena
	
## Description: 
This Python script is designed to scrape parliament election results data from the website([here](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)) focusing specifically on the 2017 elections. It scrapes details like voter registration, issued envelopes, valid votes, and party outcomes across various regions. The scraped data is saved in a CSV file. 

## Installation:
To set up the required packages for the code, download the files project_3_AM.py and requirements.txt. Then, follow these steps:
-Create a new virtual environment.
-Use pip to install the packages listed in the requirements.txt file. 

## Running the Script:
To execute the election-scraper.py file in the command prompt, two arguments are required:
- link-to-location: URL of the selected territorial unit from the website https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ
- output-file: Name of the output file, including the name and .csv extension (e.g., praha.csv)

### Program Example:
1. Visit the website https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ and select a territorial unit, such as "Praha", by clicking the "X" in the "Výběr obce" column.
2. Execute the python project_3_AM.py file with two arguments:
   - First argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100
   - Second argument: praha.csv

### Execution of the program:
```
python project_3_AM.py <link-to-location> <output-file>
python project_3_AM.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100" "praha.csv" #example command
```

### Example of .csv output
```
Code,Location,Registered,Envelopes,Valid,Občanská demokratická strana,Řád národa - Vlastenecká unie....
500054,Praha 1,21556,14167,14036,2770,9...
500224,Praha 10,79964,52277,51895,8137,40...
547034,Praha 11,58353,39306,39116,5100,48...
547107,Praha 12,42205,28561,28428,4095,24...
539694,Praha 13,42687,28376,28221,4444,24...
547361,Praha 14,32506,20139,20018,3004,39...
```
