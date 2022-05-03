import mysql.connector
import pandas as pd
from datetime import datetime


def conn(db_name, sql_query):
    # establishing the connection
    conn = mysql.connector.connect(
        user=user, password=password, host=host, database=db_name)
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Retrieving single row
    sql = sql_query

    # Executing the query
    cursor.execute(sql)

    # Fetching 1st row from the table
    result = cursor.fetchall()
    # print(result)

    # Closing the connection
    conn.close()
    return result


def sol():
    user_level_data = conn(db_name='test', sql_query='select * from user_level_info')
    events_data = conn(db_name='db_event', sql_query='select * from de_events_op')

    # Converting events and user_level_info data into Pandas Dataframes
    df_events = pd.DataFrame(events_data, columns=['event_date', 'event_timestamp', 'inititied_by', 'partner_id',
                                                   'utm_medium', 'utm_campaign', 'unique_users_coming_to_web',
                                                   'unique_users_coming_to_web_list', 'unique_users_installed',
                                                   'unique_users_installed_list'])
    df_user_info = pd.DataFrame(user_level_data, columns=['signup', 'KYC', 'UNLOCK', 'first_transaction_date',
                                                          'last_transaction_date', 'partner_id', 'user_id'])

    # Joining both the tables
    df = pd.merge(df_events, df_user_info, on='partner_id')

    '''
     1 Which utm_medium(from de_events_op) performs best for the users of  a particular partner_id.
     (Best is if user installs the app and gets credit(from unlock in user_level_info) from karmalife) 
     '''
    # filter the data having not null values in column UNLOCK
    df = df[df.UNLOCK.notnull()]
    utm_medium_count_df = df.groupby('utm_medium')['partner_id'].count().reset_index().rename(
        columns={'partner_id': 'count'}).sort_values(['count'], ascending=False)
    print("%s performs best for the users" % utm_medium_count_df.iloc[0][0])

    '''
    2 Which utm_campaign(from de_events_op) can be discarded
    '''
    utm_campaign_df = df['utm_campaign'].value_counts().reset_index().sort_values(['utm_campaign'], ascending=True)
    print("%s can be discarded" % utm_campaign_df.iloc[0][0])

    '''
    3 What’s the best time for each utm_medium(from de_events_op).(Best is if user installs the app and 
    gets credit(from unlock in user_level_info) from karmalife)
    '''
    # filter the data having not null values in column UNLOCK
    df = df[df.UNLOCK.notnull()]

    # Splitting date column to get month value
    df[["year", "month", "day"]] = df['UNLOCK'].astype(str).str.split('-', expand=True)
    df_month_count = df['month'].value_counts().reset_index().sort_values(['month'], ascending=False)
    print("Best time for each utm_medium is", datetime.strptime(df_month_count.iloc[0][0], "%m").strftime("%b"))


if __name__ == '__main__':
    host = input("Please enter Mysql's host number: ")
    user = input("Please enter the MySql user name: ")
    password = input("Please enter the MySql password: ")

    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    sol()
