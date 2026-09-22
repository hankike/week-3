from collections import defaultdict
import seaborn as sns
import pandas as pd

# Exercise One: Fibonacci Series


def fibonacci(n):
    if n <= 1:
        # This covers for fibonacci(0) and fibonacci(1), as there are no n-2 for these values, and fib(0) = 0 and fib(1) =1
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
        # Using this code, python is calculating every level of our fibonacci sequence before adding them together.
        # These values are temporarily stored for the calculation


# Exercise Two: Binary functions

def to_binary(n):
    if n == 0:
        return "0"
    # By defining for n == 0 and n == 1, these are the only two inputs python can use.
    elif n == 1:
        return "1"
    else:                       # Without == 0 or == 1, python must repeat the else function until they arrive on the answer
        return to_binary(n // 2) + str(n % 2)
        # the // 2 part helps us narrow down our n value to the == 0 or == 1 python needs, while remembering past values as well
        # The str() function adds our remainder, as all odd numbers in binary end in 1


# Exercise Three: Bellevue
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)

# A - Column names

df_bellevue['gender'] = df_bellevue['gender'].replace(
    # As we went over in the lab, gender has some non M/F responses
    ['?', 'g', 'h'],
    np.nan                      # We turn them to nan as it is not obvious what g or h are
)

column_names = df_bellevue.isna().sum().sort_values().index.tolist()

print(column_names)

# B - Data frame of year and total admissions

# First we must convert the date_in column from a string
df_bellevue['date_in'] = pd.to_datetime(df_bellevue['date_in'])

admissions_by_year = (
    df_bellevue
    # Now we can find the year from our date value
    .groupby(df_bellevue['date_in'].dt.year)
    .size()
    # Find the number for each year
    .reset_index(name='total_admissions')
    .rename(columns={'date_in': 'year'})                # Make the columns
)

print(admissions_by_year)

# C - Series with gender index and average age

avg_age_by_gender = df_bellevue.groupby('gender')['age'].mean().round(1)
# Here we group by our edited gender from earlier, find the average, then round it

print(avg_age_by_gender)

# D - List of professions

top_5_professions = df_bellevue['profession'].value_counts().head(
    5).index.tolist()
# First we are ordering based on the count, picking top 5, then adding to a list
# I am keeping married and widow, as women would likely be uncommon in jobs and marriage was their job in 1847

print(top_5_professions)

# Bonus Question!


memo = defaultdict(int)


def fibonacci(n):
    if n <= 1:
        return n                # The start is same as before, as there is not memorization needed

    if n not in memo:
        # In the earlier format, every time we ran the program the function would recalculate all former fib() and store them only for the moment. Now, they are "memorized"
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return memo[n]
