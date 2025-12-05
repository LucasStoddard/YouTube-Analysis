import pandas as pd
import numpy as np

notLoaded = True

csvTutorialString = '''To use this program you need to download some statistics from YouTube, but this is fairly easy to do
Go to YouTube, click on your channel and click YouTube Studio, and then click on Analytics on the left bar
In the top right, click on the Advanced mode button, this will pull up a chart of data for the past month
Under controls in the left bar, change "Last 28 days" to "Lifetime"
and the under Metrics on the left bar, all you need to have selected is...
Views, Average percentage viewed, Impressions click-through rate, and Likes
Click Apply and wait a second, this may take a while to load
Now in the top left click the download icon and select the (.csv) option.
This will download a zip file, all you actually need is Table data.csv
Drag that the folder this python program is in (YouTube-Analysis-CLI-Program)\n'''


while notLoaded:
    try:
        table_data_df = pd.read_csv('./Table data.csv')

        total_data_df = table_data_df.iloc[[0]].copy()
        video_data_df = table_data_df.iloc[1:].copy()

        video_data_df['Views'] = pd.to_numeric(video_data_df['Views'], errors='coerce').astype('Int64')

        def duration_to_seconds(duration_str):
            if pd.isna(duration_str):
                return 0
            parts = str(duration_str).split(':')
            if len(parts) == 3:
                return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
            elif len(parts) == 2:
                return int(parts[0]) * 60 + int(parts[1])
            return 0

        video_data_df['Average view duration'] = video_data_df['Average view duration'].apply(duration_to_seconds)
        notLoaded = False
    except:
        print(csvTutorialString)
        input('Once you are done simply hit enter to continue...\n')

notQuit = True
mainLoop = False

prefaceString = '''This program will give some feedback based off averages I found and figures from your videos
Please keep in mind that naturally a lot of this is based off of the interpretation of figures, and thus 
it is subjective in nature and could be misplaced or simply less relevant for you.\n'''


while notQuit:
    print(prefaceString)
    confirmation = input('Do you still wish to continue? (y/n)\n')
    if (confirmation == 'y'):
        mainLoop = True
    elif (confirmation == 'n'):
        notQuit = False
        print('Quitting...')
    else:
        print('Invalid response\n')
    
    if (mainLoop): # Do all the stuff
        input('Enter any key to quit...')
        notQuit = False
