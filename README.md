## Wrangling Data in SQL: OpenStreetMap Edmonton and Area
**Project Submission for Udacity's Data Analyst Nanodegree**

Project Overview:

To complete the project, I was required to choose an area from https://www.openstreetmap.org and use data munging techniques, such as assessing the quality of the data for validity, accuracy, completeness, consistency and uniformity, to clean the OpenStreetMap data. The next step was to store, query, and aggregate data using SQL.

I chose to complete this project on the [Edmonton, Alberta, Canada](https://mapzen.com/data/metro-extracts/metro/edmonton_canada/) area. The challenges I encountered during the wrangling phase and results of the SQL queries I ran are documented in the review.pdf file.

### Dependencies

This project is written in Python 3 and uses a SQLite Database

### Installation/Usage (Mac)

1. Clone the [Data_Wrangling](https://github.com/NKreutz/DAND-Data-Wrangling) repository
2. `cd` into the data_wrangling_with_SQL folder
3. Create the conda environment:
    * `conda env create -f dand-env-mac.yaml`
4. install the cerberus module:
    * `conda install cerberus`
5. Activate the Conda environment
    * `source activate DAND`
4. Create the SQLite Database by running these commands in your terminal:
    * `sqlite3 edmonton_openstreetmaps.db`
    * sqlite> `.mode csv`
    * sqlite> `.import nodes_tags.csv nodes_tags`
    * sqlite> `.import nodes.csv nodes`
    * sqlite> `.import ways_nodes.csv ways_nodes`
    * sqlite> `.import ways_tags.csv ways_tags`
    * sqlite> `.import ways.csv ways`
    * sqlite> `.quit`
5. Run `python sql_queries.py` to query the Database


### Credits

This project is based off of starter code obtained via [Udacity's](https://www.udacity.com/) Data Analyst Nanodegree in September 2017, and has been modified by Narissa Kreutz.
