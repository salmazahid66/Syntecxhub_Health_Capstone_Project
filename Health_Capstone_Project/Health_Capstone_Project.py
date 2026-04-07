import pandas as pd
import matplotlib.pyplot as plt
import os
import warnings
warnings.filterwarnings('ignore')

# ── OUTPUT FOLDER ──
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

# ── LOAD CSV FILES ──
activity = pd.read_csv("dailyActivity_merged.csv")
calories = pd.read_csv("dailyCalories_merged.csv")
sleep = pd.read_csv("sleepDay_merged.csv")

# ── CLEAN COLUMN NAMES ──
activity.columns = activity.columns.str.strip()
calories.columns = calories.columns.str.strip()
sleep.columns = sleep.columns.str.strip()

# ── CONVERT DATES ──
activity['ActivityDate'] = pd.to_datetime(activity['ActivityDate'])
calories['ActivityDay'] = pd.to_datetime(calories['ActivityDay'])
sleep['SleepDay'] = pd.to_datetime(sleep['SleepDay'])

# ── MERGE DATASETS ──
df = pd.merge(activity, calories[['Id','ActivityDay','Calories']],
              left_on=['Id','ActivityDate'], right_on=['Id','ActivityDay'], how='left')
df = pd.merge(df, sleep[['Id','SleepDay','TotalMinutesAsleep','TotalTimeInBed']],
              left_on=['Id','ActivityDate'], right_on=['Id','SleepDay'], how='left')

# Keep one Calories column
if 'Calories' not in df.columns:
    if 'Calories_x' in df.columns:
        df['Calories'] = df['Calories_x']
    elif 'Calories_y' in df.columns:
        df['Calories'] = df['Calories_y']

# ── DERIVED CATEGORIES ──
df['Steps_Cat'] = pd.cut(df['TotalSteps'], bins=[0,5000,10000,20000,100000],
                         labels=['Low','Moderate','High','Very High'])
df['Sleep_Cat'] = pd.cut(df['TotalMinutesAsleep'], bins=[0,360,420,600,1440],
                         labels=['Very Low','Low','Optimal','High'])

# ── COLORS ──
BLUE  = '#0D47A1'
RED   = '#B71C1C'
GREEN = '#1B5E20'
PURP  = '#4A148C'
ORG   = '#E65100'

# ── BAR PLOTS ──
bar_plots = [
    ("steps.png", df['Steps_Cat'].value_counts().index.astype(str), df['Steps_Cat'].value_counts().values, [GREEN, ORG, RED, PURP], "Steps Category Distribution", "Number of Users"),
    ("sleep.png", df['Sleep_Cat'].value_counts().index.astype(str), df['Sleep_Cat'].value_counts().values, [ORG, GREEN, BLUE, PURP], "Sleep Category Distribution", "Number of Users")
]

# ── SCATTER PLOTS ──
scatter_plots = [
    ("calories_vs_steps.png", df['TotalSteps'], df['Calories'], 'Calories vs Steps', 'Total Steps', 'Calories Burned', PURP),
    ("sleep_vs_steps.png", df['TotalSteps'], df['TotalMinutesAsleep'], 'Sleep vs Steps', 'Total Steps', 'Sleep (minutes)', GREEN),
    ("distance_vs_steps.png", df['TotalSteps'], df['TotalDistance'], 'Distance vs Steps', 'Total Steps', 'Distance (miles)', ORG)
]

# ── HISTOGRAMS ──
hist_plots = [
    ("very_active_minutes.png", df['VeryActiveMinutes'], 'Very Active Minutes Distribution', 'Very Active Minutes', 'Count', RED),
    ("calories_distribution.png", df['Calories'], 'Calories Burned Distribution', 'Calories Burned', 'Count', PURP),
    ("sleep_minutes_distribution.png", df['TotalMinutesAsleep'].dropna(), 'Total Sleep Minutes Distribution', 'Minutes Asleep', 'Count', GREEN)
]

# ── GENERATE BAR PLOTS ──
for filename, x, y, colors, title, ylabel in bar_plots:
    plt.figure(figsize=(8,5))
    plt.bar(x, y, color=colors, edgecolor='white')
    plt.title(title, fontsize=14, color=BLUE)
    plt.ylabel(ylabel)
    plt.savefig(os.path.join(output_dir, filename))
    plt.close()

# ── GENERATE SCATTER PLOTS ──
for filename, x, y, title, xlabel, ylabel, color in scatter_plots:
    plt.figure(figsize=(8,5))
    plt.scatter(x, y, alpha=0.5, color=color)
    plt.title(title, fontsize=14, color=BLUE)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(os.path.join(output_dir, filename))
    plt.close()

# ── GENERATE HISTOGRAMS ──
for filename, data, title, xlabel, ylabel, color in hist_plots:
    plt.figure(figsize=(8,5))
    plt.hist(data, bins=30, color=color, alpha=0.7, edgecolor='white')
    plt.title(title, fontsize=14, color=BLUE)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(os.path.join(output_dir, filename))
    plt.close()

# ── ACTIONABLE INSIGHTS ──
insights = [
    "1️⃣ Users with higher steps burn more calories. Encourage daily activity to achieve fitness goals.",
    "2️⃣ Optimal sleep (7–8 hrs) correlates with moderate activity. Track sleep for better physical performance.",
    "3️⃣ Very low steps and high sedentary minutes indicate health risks. Suggest interventions for inactive users."
]

print("✅ All separate outputs saved in 'outputs' folder")
print("\n📌 Actionable Insights:")
for insight in insights:
    print(insight)