# What should I put into the Pandas Dataframe?
# Breakdown - Content
# Metrics - Views, watch time, subscribers, average view duration, average percentage viewed, impressions, impressions click-through rate, 
#           subs gained, subs lost, likes, dislikes, likes (vs. dislikes), shares, comments added
# Sort by views and download as csv
# Drag all three csvs into this folder

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

video_data_df['Views'] = pd.to_numeric(video_data_df['Views'], errors='coerce').astype('Int64')

def truncate_title(title):
    max_len = 30
    if len(title) > max_len:
        return title[:(max_len - 3)] + '...'
    return title

def top_n_percentages(n):
    top_n_videos = video_data_df.sort_values(by='Views', ascending=False).head(n).reset_index(drop=True)

    # Prepare lists for plotting
    video_titles = top_n_videos['Video title'].apply(truncate_title)
    avg_view_pct = top_n_videos['Average percentage viewed (%)']
    likes_vs_dislikes_pct = top_n_videos['Likes (vs. dislikes) (%)']
    x_indices = range(len(video_titles))
    fig, ax1 = plt.subplots(figsize=(20, 9))
    ax1.plot(x_indices, avg_view_pct, marker='o', linestyle='-', color='blue', label='Average Percentage Viewed (%)')
    ax1.set_xlabel('Video Title', fontsize=12)
    ax1.set_ylabel('Average Percentage Viewed (%)', color='blue', fontsize=12)
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.set_ylim(bottom=0)
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax2 = ax1.twinx()
    ax2.plot(x_indices, likes_vs_dislikes_pct, marker='s', linestyle='-', color='red', label='Likes (vs. Dislikes) (%)')
    ax2.set_ylabel('Likes (vs. Dislikes) (%)', color='red', fontsize=12)
    ax2.tick_params(axis='y', labelcolor='red')
    ax2.set_ylim(likes_vs_dislikes_pct.min() * 0.95, 100) 
    ax1.set_xticks(x_indices)
    ax1.set_xticklabels(video_titles, rotation=90, ha="right", fontsize=10)
    plt.title('Videos sorted by views with percentages', fontsize=14)
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right', frameon=True)
    plt.tight_layout()
    plt.savefig('top_video_metrics_line.png')
    print("\nAnalysis complete.")
    print(top_n_videos[['Video title', 'Views', 'Average percentage viewed (%)', 'Likes (vs. dislikes) (%)']])
    print("\nChart saved as 'top_video_metrics_line.png'.")

# This is an interesting measurement, but it isn't views vs percentages, it is simply ordering of videos vs percentages
# top_n_percentages(100)

def n_videos_views_and_retention(n, log):
    top_n_videos = video_data_df.sort_values(by='Views', ascending=False).head(n).reset_index(drop=True)

    # Prepare lists for plotting
    video_views = top_n_videos['Views']
    avg_view_pct = top_n_videos['Average percentage viewed (%)']
    fig, ax = plt.subplots(figsize=(20, 9))
    ax.plot(video_views, avg_view_pct, marker='o', linestyle='-', color='green')
    if (log):
        ax.set_xscale('log')
    ax.set_xlabel('Views', fontsize=12)
    ax.set_ylabel('Average Percentage Viewed (%)', fontsize=12)
    ax.set_title('Video Views vs. Viewer Retention Percentage', fontsize=14)
    if (not log):
        ax.ticklabel_format(style='plain', axis='x')
    ax.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig('views_vs_retention_line.png')

n_videos_views_and_retention(200, True)

# FROM THE nth video TO THE mth video
def n_to_m_videos_views_and_retention_trendline(n, m):
    top_videos = video_data_df.sort_values(by='Views', ascending=False).reset_index(drop=True)
    top_n_to_m_videos = top_videos.iloc[n - 1: m].copy()
    views = pd.to_numeric(top_n_to_m_videos['Views'], errors='coerce').values 
    avg_view_pct = top_n_to_m_videos['Average percentage viewed (%)'].values

    sort_order = np.argsort(views)
    views = views[sort_order]
    avg_view_pct = avg_view_pct[sort_order]
    log_views = np.log(views)

    slope, intercept, r_value, p_value, std_err = linregress(log_views, avg_view_pct)
    r_squared = r_value**2
    trend_line = intercept + slope * log_views
    fig, ax = plt.subplots(figsize=(20, 9))
    ax.plot(views, avg_view_pct, marker='o', linestyle='-', color='green', label='Videos')

    # Plot the trend line. We use LaTeX for the R^2 notation.
    ax.plot(views, trend_line, linestyle='--', color='red', 
            label=f'Trend Line ($\mathregular{{R^2}}$ = {r_squared:.2f}, $p$ = {p_value:.4f}))')

    ax.set_xscale('log')
    ax.set_xlabel('Views (Log Scale)', fontsize=12)
    ax.set_ylabel('Average Percentage Viewed (%)', fontsize=12)
    ax.set_title('Views vs. Viewer Retention with Logarithmic Trend Line', fontsize=14)
    ax.set_xlim(views.min() * 0.8, views.max() * 1.2)
    ax.grid(True, linestyle='--', alpha=0.6, which="both") 
    ax.legend(loc='upper right')

    plt.tight_layout()
    name = f"{n}_to_{m}_views_vs_retention_log_trend.png"
    plt.savefig(name)
    print(f"R-squared value: {r_squared:.4f}")
    print(f"Chart saved as {name}")

n_to_m_videos_views_and_retention_trendline(2, 300)
n_to_m_videos_views_and_retention_trendline(150, 300)
n_to_m_videos_views_and_retention_trendline(2, 150)

# Observations:
#   This is not NEARLY as clear as I thought it would be. The one YouTube short is too much of an outlier. (without it R squared is zero lol)
#   It seems like with lower views, retention is important, but the higher you get the less it matters.
#   This may because I'm using % and not average view TIME, but I'll look at that in a second
#   Also I probably need to make a very generic program for plotting considering how many figures I need to sift through

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

def n_to_m_videos_views_and_retention_raw_trendline(n, m):
    top_videos = video_data_df.sort_values(by='Views', ascending=False).reset_index(drop=True)
    top_n_to_m_videos = top_videos.iloc[n - 1: m].copy()
    views = pd.to_numeric(top_n_to_m_videos['Views'], errors='coerce').values 
    avg_view_pct = top_n_to_m_videos['Average view duration'].apply(duration_to_seconds).values

    sort_order = np.argsort(views)
    views = views[sort_order]
    avg_view_pct = avg_view_pct[sort_order]
    log_views = np.log(views)

    slope, intercept, r_value, p_value, std_err = linregress(log_views, avg_view_pct)
    r_squared = r_value**2
    trend_line = intercept + slope * log_views
    fig, ax = plt.subplots(figsize=(20, 9))
    ax.plot(views, avg_view_pct, marker='o', linestyle='-', color='green', label='Videos')

    # Plot the trend line. We use LaTeX for the R^2 notation.
    ax.plot(views, trend_line, linestyle='--', color='red', 
            label=f'Trend Line ($\mathregular{{R^2}}$ = {r_squared:.2f}, $p$ = {p_value:.4f})')

    ax.set_xscale('log')
    ax.set_xlabel('Views (Log Scale)', fontsize=12)
    ax.set_ylabel('Average Percentage Viewed (%)', fontsize=12)
    ax.set_title('Views vs. Viewer Retention with Logarithmic Trend Line', fontsize=14)
    ax.set_xlim(views.min() * 0.1, views.max() * 1.2)
    ax.grid(True, linestyle='--', alpha=0.6, which="both") 
    ax.legend(loc='upper right')

    plt.tight_layout()
    name = f"{n}_to_{m}_views_vs_retention_raw_log_trend.png"
    plt.savefig(name)
    print(f"R-squared value: {r_squared:.4f}")
    print(f"Chart saved as {name}")

n_to_m_videos_views_and_retention_raw_trendline(1, 100)

# Observations:
#   Okay, raw watch time has NO correlation. While r-squared is small, the p-value is like 0 so there definitely IS an effect, just not as much as one would hope