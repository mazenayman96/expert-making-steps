# import pandas as pd

# df = pd.read_csv("chicago.csv")

# df = pd.DataFrame(df)

# df['Start Time']= pd.to_datetime(df['Start Time'])

# df['hour'] = df['Start Time'].dt.hour

# Most_popular_hour = df['hour'].mode()[0]

# print(Most_popular_hour)

# user_types = df['User Type'].value_counts()
# print(user_types)

import pandas as pd

CITY_DATA = { 'chicago': pd.read_csv('chicago.csv'),
              'new york city': pd.read_csv('new_york_city.csv'),
              'washington': pd.read_csv('washington.csv') }

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    df = pd.DataFrame(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    months = {'january': 'January', 'february' :'February', 'march' :'March', 'april' :'April', 'may' :'May', 'june' :'June'}
    if month in months:
        df = df[df['month'] == months[month]]

    days = {'sunday':'Sunday','monday':'Monday','tuesday':'Tuesday','wednesday':'Wednesday','thursday':'Thursday','friday':'Friday','saturday':'Saturday'}
    if day in days:
        df = df[df['day_of_week'] == days[day].title()]
    return df 

df = load_data('new york city','may', 'all')

print(df.head(10))