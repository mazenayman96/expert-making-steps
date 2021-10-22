import time
import pandas as pd
import numpy as np
from pandas.core.indexes.base import Index

CITY_DATA = { 'chicago': pd.read_csv('chicago.csv'),
              'new york city': pd.read_csv('new_york_city.csv'),
              'washington': pd.read_csv('washington.csv') }
city = None
month = None
day = None

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    global city
    city_names = ['chicago','new york city','washington']

    while city not in city_names:
        city = (input('Enter city name: ')).lower()
        if city in city_names:
            print('{} selected!'.format(city))
            break
        print('The city you entered is not on the list! Please try another city name.')
    global month
    # TO DO: get user input for month (all, january, february, ... , june)
    months_list = {'january': 1, 'february' :2, 'march' :3, 'april' :4, 'may' :5, 'june' :6, 'all': [1,2,3,4,5,6,7]}

    while month not in months_list:
        month = input('Enter month name. (all, january, february, ..., june): ' ).lower()
        if month in months_list:
            print('{} selected!'.format(month))
            break
        print('The month you entered is not on the list! Please try another month.')
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    global day
    days_list = {'sunday':'Sunday','monday':'Monday','tuesday':'Tuesday','wednesday':'Wednesday','thursday':'Thursday','friday':'Friday','saturday':'Saturday','all': [1,2,3,4,5,6,7]}

    while day not in days_list:
        day = input('Enter day name. (all, sunday, monday, ..., saturday): ' ).lower()
        if day in days_list:
            print('{} selected!'.format(day))
            break
        print('The day you entered is not on the list! Please try another day.')

    print('-'*40)
  
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    global df

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

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('most frequent month is: {}'.format(most_common_month))

    # TO DO: display the most common day of week
   

    most_common_day = df['day_of_week'].mode()[0]
    print('most frequent day is: {}'.format(most_common_day))

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hours'] = df['Start Time'].dt.hour

    most_common_hour = df['hours'].mode()[0]
    print('most frequent hour is: {}'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('most popular Start station is: {}'.format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('most popular End station is: {}'.format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    most_common_trip = (df['Start Station'] +' -----> '+ df['End Station']).mode()[0]
    print('most popular trip is: {}'.format(most_common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    years_traveled = total_trip_duration //3.154e+7
    days_traveled = (total_trip_duration - (years_traveled*3.154e+7)) // 86400
    hours_traveled = (total_trip_duration - (years_traveled*3.154e+7) - (days_traveled*86400)) // 3600
    minutes_traveled = (total_trip_duration - (years_traveled*3.154e+7) - (days_traveled*86400) - (hours_traveled*3600)) // 60
    seconds_traveled = total_trip_duration - (years_traveled*3.154e+7) - (days_traveled*86400) - (hours_traveled*3600) - (minutes_traveled*60)
    print('Total travel time:\n{} years {} days {} hours {} minutes {} seconds'.format(years_traveled.astype(int),days_traveled.astype(int),hours_traveled.astype(int),minutes_traveled.astype(int),seconds_traveled.astype(int)))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    hours_traveled = mean_travel_time // 3600
    minutes_traveled = (mean_travel_time - (hours_traveled*3600)) // 60
    seconds_traveled = mean_travel_time - (hours_traveled*3600) - (minutes_traveled*60)
    print('Average travel time:\n{} hours {} minutes {} seconds'.format(int(hours_traveled),int(minutes_traveled),int(seconds_traveled)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts().to_string()
    print('User types:\n{}\n'.format(user_counts))

    # TO DO: Display counts of gender
    if city != 'washington':
        gender_counts = df['Gender'].value_counts().to_string()
        print('Genders:\n{}\n'.format(gender_counts))

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_dob = int(df['Birth Year'].min())
        print('Earliest DOB: {} '.format(earliest_dob))

        lateset_dob = int(df['Birth Year'].max())
        print('Most recent DOB: {} '.format(lateset_dob))

        most_common_dob = int(df['Birth Year'].mode()[0])
        print('Most common DOB: {} '.format(most_common_dob))
    else:
        print('DOBs and gender data isn\'t available for washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print(df.iloc[:5])
        global i
        global x 
        i = 5
        x = 0
        question = input('Would you like to see 5 rows of raw data? ').lower()

        while question == 'yes':
            print(df.iloc[x:i])
            question = input('Would you like to see another 5 rows of raw data? ').lower()
            i += 5
            x += 5

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
        
if __name__ == "__main__":
	main()
