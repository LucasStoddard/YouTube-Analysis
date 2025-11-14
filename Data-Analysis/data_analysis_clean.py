# YOU HAVE TO BE IN THE DATA-ANALYSIS FOLDER FOR THIS TO RUN IN YOUR TERMINAL
import pandas as pd
import matplotlib.pyplot as plt

# For trendlines
import numpy as np
from scipy.stats import linregress

table_data_df = pd.read_csv('./Table data.csv')
# print(table_data_df.head())
# table_data_df.info()

total_data_df = table_data_df.iloc[[0]].copy()
video_data_df = table_data_df.iloc[1:].copy()
# video_data_top100_df = table_data_df.iloc[1:101].copy()

# print(total_data_df.head())
# print(video_data_df.head())

# Change data into more easily measureable things
video_data_df['Views'] = pd.to_numeric(video_data_df['Views'], errors='coerce').astype('Int64')

def duration_to_seconds(duration_str):
    if pd.isna(duration_str):
        return 0
    parts = str(duration_str).split(':')
    if len(parts) == 3:
        # HH:MM:SS format
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
    elif len(parts) == 2:
        # MM:SS format
        return int(parts[0]) * 60 + int(parts[1])
    return 0

video_data_df['Average view duration'] = video_data_df['Average view duration'].apply(duration_to_seconds)
video_data_df['Duration'] = video_data_df['Duration'].apply(duration_to_seconds)

# from N to M videos, compare x_label (log or not log) with y_label
def n_to_m_videos_generic(log, n, m, x_label, y_label):
    top_videos = video_data_df.sort_values(by=x_label, ascending=False).reset_index(drop=True)
    top_n_to_m_videos = top_videos.iloc[n - 1: m].copy()
    # remove zero values
    filtered_videos = top_n_to_m_videos[top_n_to_m_videos[y_label] != 0].copy()
    x_values = pd.to_numeric(filtered_videos[x_label], errors='coerce').values 
    y_values = filtered_videos[y_label].values

    sort_order = np.argsort(x_values)
    x_values = x_values[sort_order]
    y_values = y_values[sort_order]
    log_views = np.log(x_values)

    slope, intercept, r_value, p_value, std_err = linregress(log_views, y_values)
    r_squared = r_value**2
    trend_line = intercept + slope * log_views
    fig, ax = plt.subplots(figsize=(20, 9))
    ax.plot(x_values, y_values, marker='o', linestyle='-', color='green', label='Videos')

    # Plot the trend line. We use LaTeX for the R^2 notation.
    ax.plot(x_values, trend_line, linestyle='--', color='red', 
            label=f'Trend Line ($\mathregular{{R^2}}$ = {r_squared:.2f}, $p$ = {p_value:.4f}, $stderr$ = {std_err:.4f})')

    if (log):
        ax.set_xscale('log')
    ax.set_xlabel(x_label, fontsize=12)
    ax.set_ylabel(y_label, fontsize=12)
    ax.set_title(f'{x_label} compared to {y_label}', fontsize=14)
    ax.set_xlim(0, x_values.max() * 1.1)
    ax.grid(True, linestyle='--', alpha=0.6, which="both") 
    ax.legend(loc='upper right')

    plt.tight_layout()
    name = f"{n}_to_{m}_{x_label}_vs_{y_label}.png"
    plt.savefig(name)
    print(f"R-squared value: {r_squared:.4f}")
    print(f"Chart saved as {name}")

# n_to_m_videos_generic(False, 2, 300, 'Views', 'Comments added')

def batchViewComparison(compArray):
    for comparison in compArray:
        n_to_m_videos_generic(False, 6, 100, 'Views', comparison)
# Video title,Video publish time,Duration,Average view duration,Average percentage viewed (%),Subscribers gained,Subscribers lost,
# Likes,Dislikes,Likes (vs. dislikes) (%),Shares,Comments added,Views,Watch time (hours),Subscribers,Impressions,Impressions click-through rate (%)
batchComparisons = [
    # "Video title", irrelevant in this form
    # "Video publish time",
    # "Duration",
    "Average view duration",
    "Average percentage viewed (%)",
    "Subscribers gained",
    "Subscribers lost",
    "Likes",
    "Dislikes",
    "Likes (vs. dislikes) (%)",
    "Shares",
    "Comments added",
    # "Views",
    "Watch time (hours)",
    "Subscribers",
    "Impressions",
    "Impressions click-through rate (%)"
]
batchViewComparison(batchComparisons)

# Observations:
    # It is very easy to argue "x causes y" when it is really "y causes x." 
    #   Like you can argue "well if you get subscribers then the video will do better" but funnily enough an even more positive trend is losing subscribers
    # Once again, average percentage viewed is a very strong indicator, but it really is not the final say
    # I think with some of these I need to dig deeper into the day to day graphs on individual videos.
# TODO: More lines and choose 5 metrics which are most likely to have an effect on views for the fine detail search