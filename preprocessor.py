
import re
import pandas as pd
from datetime import datetime


def preprocess(data):
    if (data[15:17]=="pm")or(data[15:17]=="am")or(data[14:16]=="pm")or(data[14:16]=="am"):
        gh=12
        print("12")
        pattern = '\d{1,2}/\d{1,2}/\d{1,2},\s\d{1,2}:\d{1,2}\s(?:am|pm)\s-\s'
    else:
        gh=24
        print("24")
        pattern = '\d{1,2}/\d{1,2}/\d{1,2},\s\d{1,2}:\d{2}\s-\s'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    # convert message_date type
    def convert24(time):
        time = time.split(",")
        # Parse the time string into a datetime object
        t = datetime.strptime(time[1].strip(" -"), '%I:%M %p')
        # Format the datetime object into a 24-hour time string
        ta = time[0] + "," + t.strftime('%H:%M')
        return ta
    if gh==12:
        df['message_date'] = df['message_date'].apply(lambda x: convert24(x))
        df["message_date"] = pd.to_datetime(df["message_date"], format="%d/%m/%y,%H:%M")
    else:
        df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %H:%M - ')

    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:  # user name
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages

    df.drop(columns=['user_message'], inplace=True)
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df