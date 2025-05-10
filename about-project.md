# About My Project

Student Name: Mera Singh
Student Email: mesingh@syr.edu

### What it does

This project lets users compare NBA players' performance across seasons using data from the balldontlie API. Users can select up to three players and view visual comparisons of key stats like points, assists, rebounds, and more.

The dashboard helps basketball fans and analysts:

Compare stats by season or career average

Visualize differences using bar charts, line graphs, and radar plots

Explore trends in performance over time


### How you run my project

Run the Streamlit dashboard with:

streamlit run code/load_dashboard.py
The app will launch in your browser. From there, you can: 
or network url: http://10.1.140.19:8501

Use the sidebar to search and select players, hit enter after each input but let it run before trying to continue.

lastly, choose the season then hit compare players.

View comparison charts and insights

### what each folder means

extract_data.py: Handles API calls to get player and season stats

transform_data.py: Cleans and formats raw data

load_dashboard.py: Streamlit app for user interaction and visuals

utils.py: Helper functions used across files

tests/test_utils.py: Unit tests for key data functions

cache/: Folder to store raw and processed data

### Other things you need to know

The balldontlie API has rate limits, so cached files are used to avoid repeated calls.

Some players with similar names might return incorrect results—user needs to verify selection.

Radar charts require players with data for the same season; otherwise, stats may be skewed.

Project meets all course requirements: Python modules, Streamlit UI, pandas data wrangling, API use, and visualizations with Plotly.