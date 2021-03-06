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
- Python 3.6
- pytorch
- pandas
- transformers

Service
-----
- React 16.9
- Typescript 4.0.2
- styled-component 5.2.1
- node 14.15.1
- pythonshell 2.0.3
- react-bootstrap 1.4.0

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
|   |-- data
|   |   |-- cleanse.py
|   |   |-- equalize.py
|   |-- infer.py
|   |-- train.py
|-- cs489
|   |-- src
|   |   |-- assets
|   |   |-- components
|   |   |-- pages
|   |   |-- routers
|   |   |-- styles
|   |   |-- utils
|   |   |-- App.tsx
|   |-- public
|   |-- server
|   |   |-- assets/graphs
|   |   |-- routes
|   |   |-- server.js
|   |   |-- serverProxy.js
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

Model
----
- download pretrained model from [link](https://drive.google.com/file/d/1SCaPK6HhUHl9FS4bTPkOlHGSaC4HUJs5/view?usp=sharing)
- `train.py`
   - code to train
   - download dataset from [link](https://jmcauley.ucsd.edu/data/amazon/)
   - use `data/equalize.py` for preprocessing
- `infer.py`
   - code to infer
   - `Path to the checkpoint: ` - write path you save ckpt
   - `Enter Sentence: ` - write sentence you want to test 

Service
----
- `yarn install`
- `server.js`
   - code about starting server
   - at path ./cs489/server/ `node server.js`
- starting web
   - at path ./cs489/ `yarn start`


## Final Persentation
- [link](https://youtu.be/69NOLS050U0)

## Image Reference
- Matrix (pill image)
- matrix image - https://techcrunch.com/2019/03/18/how-to-build-the-matrix/ (photo by Ismagiov, Shutterstock)
