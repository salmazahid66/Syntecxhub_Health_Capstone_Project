# Health Capstone Project

This project analyzes real-world Fitbit health data to provide actionable insights on **physical activity, sleep patterns, and calorie burn**. The analysis is performed using Python with data cleaning, exploratory data analysis (EDA), and visualizations.

---

##  Dataset

Three datasets are used:

1. **dailyActivity_merged.csv** – Contains daily step counts, distance, and active minutes.  
2. **dailyCalories_merged.csv** – Contains daily calories burned.  
3. **sleepDay_merged.csv** – Contains sleep duration and time in bed.  

*Note: All datasets are merged on `Id` and `Date` for comprehensive analysis.*

---

## 🛠️ Technologies Used

- Python 3.x  
- Pandas for data cleaning & manipulation  
- Matplotlib for visualizations  
- NumPy for numeric operations  

---

##  Data Cleaning

- Stripped column whitespaces  
- Converted date columns to `datetime`  
- Merged activity, calories, and sleep datasets  
- Created categorical columns for **Steps** and **Sleep**  

---

##  Exploratory Data Analysis (EDA)

**Visualizations generated:**

1. Steps Category Distribution  
2. Sleep Category Distribution  
3. Calories vs Steps  
4. Sleep vs Steps  
5. Distance vs Steps  
6. Very Active Minutes Distribution  
7. Calories Burned Distribution  
8. Total Sleep Minutes Distribution  

**Actionable Insights:**

1. Users with high steps tend to burn more calories.  
2. Sleep duration affects daily activity patterns.  
3. Very active users are more likely to maintain healthy habits.

--
