# YouTube-Analysis

#### The *primary goal* of this project is to analyze data from YouTube videos to find what correlates with a successful video. After that, the *secondary goal* is to make a program that takes in metrics from any video and gives an estimate on what needs to be improved on.

## Goals (Subject To Change)
1. Ideate & Create this project
2. Document this project (continually)
3. Complete the required assignments for this project (continually)
4. Primary Goal: Analyze Data (COMPLETED)
    1. Wrangle the csv into Pandas Dataframes
    2. Investigate possible correlations
    3. Widdle that down to a few top metrics
    4. Get day to day data from a couple of videos that performed unexpectedly well or poorly
    5. Use the top metrics and the finer details to conclude which metrics were most important
    6. Write these conclusions with graphs in a report style markdown file
5. Secondary Goal: Program an Analysis Tool
    1. Make a database that holds averages for the main metrics
    2. Make a program similar to the data analysis tool for uploading any csv
    3. Make it CLI based with guidance for the user
    4. After all this, program the functionality
    5. Make sure everything is cleaned up
6. Final Goal: Create the Presentation

### Goal Log
| Goal | Date | Time | TOTAL | Notes |
| ---  | ---  | ---  | ----- | ----- |
| Ideation | 11/1 | 0:25 | 0:25 | Brainstormed a whole lot of ideas |
| Ideation | 11/2 | 2:00 | 2:25 | Had an idea involving seed cracking (Minecraft) but the approach would take far too long for a short project like this, eventually moved on |
| Ideation & Creation | 11/3 | 2:00 | 4:25 | Finally decided on the subject matter of this project, and I additionally pulled all my YouTube data into a google sheet to start to understand better what I am working with and what approach I want to take |
| Documentation | 11/4 | 3:00 | 7:25 | Put the pen to the GitHub Paper and thought through the goals of this project | 
| Assignment | 11/4 | 0:35 | 8:00 | [Initial Design Document](./Initial-Design/Initial-Design.md) |
| Wrangle CSV | 11/6 | 0:15 | 8:15 | Wasn't too bad, wrote some instructions and created [data_analysis_tinkering.py](./Data-Analysis/data_analysis_tinkering.py)|
| Investigate Data | 11/6 | 1:45 | 10:00 | Edited [data_analysis_tinkering.py](./Data-Analysis/data_analysis_tinkering.py) lines 27 - 187, mainly investigated retention % and retention time, found retention time does almost nothing but also that retention % has a correlation, but only a very slight positive one |
| Investigate Data | 11/7 | 1:00 | 11:00 | Made [data_analysis_clean.py](./Data-Analysis/data_analysis_clean.py) which is a much more flexible program and allows for easy scanning of a lot of graphs, I may be been too quick to dismiss some metrics, but other ones are proving to be extremely inconsistent |
| Assignment | 11/14 | 4:00 | 15:00 | Created System Design and a more robust ERD in Google Drive |
| Data Analysis | 11/25 | 2:00 | 17:00 | Chose the specific metrics and constructed equations using the data |
| Documentation | 11/25 | 2:00 | 19:00 | Created the [Expected values report](./Data-Analysis/Expected_values_report.md) and calculated a lot of figures as well as recorded a lot of my thoughts about what the figures could mean and how they might fall short |
| Documentation | 11/26 | 0:30 | 19:30 | Updated these goals to be more realistic for the time I currently have |
| Analysis Tool | 11/26 | 0:30 | 20:00 | Wrote [YouTube Analyzer Plan](./YouTube-Analysis-CLI-Program/YouTube-Analyzer-Plan.md), which is an outline of what I want the CLI program to do. This will streamline the actual programming part. |
| Assignment | 11/29 | 3:00 | 23:00 | Created the presentation and adjusted some code for clean graphs |
| Assignment | 11/30  | 3:00 | 26:00 | Finished the presentation and added polish |
| Assignment | 12/1 | 1:00 | 27:00 | Final Project Collaboration and Reviews |
| Analysis Tool | 12/5 | 3:00 | 30:00 | Work on [YouTube Analyzer](./YouTube-Analysis-CLI-Program/YouTube-Analyzer.py), still need figures |
| Analysis Tool | 12/5 | 1:00 | 31:00 | Used a Google Sheet for figure calculation |
| To | Be | Continued | Over | Time... |