import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
""" I define variables for cities, months and days"""
cities = ['chicago', 'new york city', 'washington']
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'sunday', 'monday', 'tuesday', 'wendsday', 'thursday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    day = days[0]
    month = months[0]
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print('Choose a city! Chicago, New York city or Washington. Which you prefer to analyze?\n')
        city = input()
        if city.lower() not in cities:
            print('Ouch!It seems you have type an incorrect name,Try again!\n')
        else:
        # While loop used to avoid errors
            while True:
                filter = input('Do you prefer to filter by month, day or not at all? Type "all" for no time filter\n')
                if filter.lower() not in ['month', 'day', 'all']:
                    print('Ouch!It seems you have type an incorrect word,Try again!\n')
                else:
                    if filter.lower() == 'month':
                        print('You have choosen {}!\n'.format(filter))
                        # While loop used to avoid errors
                        while True:
                            # get user input for month (all, january, february, ... , june)
                            month = int(input('Which month? Type 0 for all, 1 for January, 2 for February, 3 for March and so on\n'))
                            if month not in range(0, 7):
                                print('Choose a correct month! A year does not have more than 12 months.\n')
                            else:
                                month = months[int(month)]
                                print('You have choosen {}\n'.format(month))
                                break
                        break
                    elif filter.lower() == 'day':
                        print('You have choosen {}!\n'.format(filter))
                        # While loop used to avoid errors
                        while True:
                            # get user input for day of week (all, monday, tuesday, ... sunday)
                            day = int(input('Which day? Type 0 for all, 1 for Sunday, 2 for Monday...\n'))
                            if day not in range(0, 8):
                                print("Choose a correct day!")
                            else:
                                day = days[int(day)]
                                print("You have choosen {}\n".format(day))
                                break
                        break
                    elif filter.lower() == 'all':
                        print('You have choosen {}!\n'.format(filter))
                        break
            break
    print('Fine! It seems you want to see the data of {}, filter by {} and {}\n'.format(city, month, day))

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
    # filter by month to create the new dataframe
        month = months.index(month) + 1
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
    # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    popular_month = df['month'].mode()[0]
    print('The most popular month is {}'.format(month[popular_month]))

    # display the most common day of week
    popular_weekday = df['day_of_week'].mode()[0]
    print('The most popular day is {}'.format(popular_weekday))

    # display the most common start hour
    # Extract hour from the Start Time column to create and hour column
    df['Start Hour'] = df['Start Time'].dt.time
    popular_starthour = df['Start Hour'].mode()[0]
    print('The most popular hour is {}'.format(popular_starthour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_startstation = df['Start Station'].mode()[0]
    print('The most popular start station is {}'.format(popular_startstation))

    # display most commonly used end station
    popular_endstation = df['End Station'].mode()[0]
    print('The most popular end station is {}'.format(popular_endstation))

    # display most frequent combination of start station and end station trip
    # Create new column with start station and end station
    df['Start-End Station'] = df['Start Station'] + ' - ' + df['End Station']
    most_freq_combin = df['Start-End Station'].mode()[0]
    print('The most frequent combination of start station and end station trip is', most_freq_combin)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    # rounded mean in order to avoid large number
    mean_travel_time_round = round(mean_travel_time, 4)
    print('Mean travel time', mean_travel_time_round)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types, '\n')


    # Display counts of gender
    # There is no 'Gender' column for washington, so while loop is use to avoid errors
    while 'Gender' not in df:
        print('No gender data for washington\n')
        break
    else:
        gender = df['Gender'].value_counts()
        print(gender, '\n')

    # Display earliest, most recent, and most common year of birth
    # There is no 'Birth Year' column for washington, so while loop is use to avoid errors
    while 'Birth Year' not in df:
        print('No birth year data for washington')
        break
    else:
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print('Earliest year of birth:', earliest_year)
        print('Most recent year of birth:', recent_year)
        print('Most common year of birth:', common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
