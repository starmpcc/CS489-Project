# CS489-Project
# Detect Rigged Review(DRR)
Team 6

## Prototyping by Figma
- link: <https://www.figma.com/file/Hp1WWmSQN52mccVHKJbr4H/cs489?node-id=0%3A1>

Package Dependencies
=======

Spider & Detectpr
-----
- Python 3.8.6
- BeautifulSoup4-0.0.1
- Selenium 3.141.0
- Microsoft Edge 86.0.622.63
- matplotlib
- requests

Model
----

Service
-----

Directory Structure
======
```
.
|-- Spider
|   |-- spider.py
|   |-- write_csv.py
|   |-- toJson.py
|   |-- simple_spider.py
|   |-- msedgedriver.exe
|   |-- Driver_Notes
|   |-- detector.py
|   |-- graph.tar.gz
|   |-- data
|   |   |-- data.tar.gz
|-- bert
|-- cs489
|
```
Spider
----
 - `spider.py`
    - Main script for spider
    - Collect reviews&metadata from Google Play
    - Usage

        `$ python3 spider.py -n`
        
        Collect Recent reviews and generate new csv files

        `$ python3 spider.py -c`

        Collect metadata from Google Play with existing csv files
 - `write_csv.py`
    - File I/O script for spider.py
 - `toJson.py`(legacy)
    - Convert csv to json format
 - `simple_spider.py`
    - small version of spider that only can collect metadata
    - Can work on Android Termux
    - Usage

        `$ python3 simple_spider.py`
 - `msedgedriver.exe, Driver_Notes`
    - Edgedriver to support Selenium
 - `detector.py`
    - Detect abnormal changes from collected rate history
    - Draw history graph
    - Usage
    
        `$ python3 detector.py`
 - `graph.tar.gz`
    - Generated graphs from `detector.py`
 - data
    - Collected data from Spider
    - Saved as `data.tar.gz`
