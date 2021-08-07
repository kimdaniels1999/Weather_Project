import csv
from datetime import datetime
from sqlite3.dbapi2 import converters

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    return f"{temp}{DEGREE_SYBMOL}"  # no change required

    # """Takes a temperature and returns it in string format with the degrees and celcius symbols..
    # Args:
    # temp: A string representing a temperature.
    # Returns:
    # A string contain the temperature and "degrees celcius."
    # """

def convert_date(iso_string):
    date = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z") #added variable 
    date_new = date.strftime("%A %d %B %Y") # use previous variable, datetime changed to date, forgot to add "" inside parenthesis,  
    return date_new   # return 2nd new variable

    # """Converts an ISO formatted date into a human readable format.
    # Args
    # iso_string: An ISO date string.
    # Returns:
    # A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    # """

def convert_f_to_c(temp_in_farenheit):  # (temp_in_farenheit is an int)
    return round((float(temp_in_farenheit)-32)*(5/9),1) # round(number, 1) #combine all to one line 

    # """Converts a temperature from farenheit to celcius. 

    # Args:
    #     temp_in_farenheit: float representing a temperature.
    # Returns:
    #     A float representing a temperature in degrees celcius, rounded to 1dp. 
    # """

def calculate_mean(weather_data): # what format is the weather data (error = unsupported operand types +: 'int' and 'str')
    new_list = [float(i) for i in weather_data] # 
    return sum(new_list)/len(weather_data)
        
    # calculate_mean = sum(data) / len(data)
    # return float(calculate_mean)
    # """Calculates the mean value from a list of numbers.

    # Args:
    #     weather_data: a list of numbers.
    # Returns:
    #     A float representing the mean value.
    # """


def load_data_from_csv(csv_file):

    data_list = []  # create an empty list
    with open(csv_file, mode="r", encoding="utf-8") as csv_file:  #open csv file
        csv_reader = csv.reader(csv_file, delimiter = ",")  #read csv file
        for index, row in enumerate(csv_reader):   #two loop variables index and row
            if index != 0 and len(row) != 0:   # index is not equal to zero lenth of row is not equal to zero (non-empty lines)
                data_list.append([row[0],int(row[1]),int(row[2])])  #append to the empty list 
    return data_list

    # """Reads a csv file and stores the data in a list.

    # Args:
    #     csv_file: a string representing the file path to a csv file.
    # Returns:
    #     A list of lists, where each sublist is a (non-empty) line in the csv file.
    # """

def find_min(weather_data):
    # list_float = [float(i) for i in weather_data]
    if len(weather_data) == 0:
        return()
    min_value = float(weather_data[0])
    min_position = 0
    
    for index, num in enumerate(weather_data):
        if float(num) <= min_value:
            min_value = float(num)
            min_position = index
    return (min_value, min_position)
            # AssertionError: None != (49.0, 0)
            # ValueError: min() arg is an empty sequence
    
    # """Calculates the minimum value in a list of numbers.
    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The minium value and it's position in the list.
    # """

def find_max(weather_data):
    if len(weather_data) == 0:
        return()
    max_value = float(weather_data[0])
    max_position = 0
    
    for index, num in enumerate(weather_data):
        if float(num) >= max_value:
            max_value = float(num)
            max_position = index
    return (max_value, max_position)

    # """Calculates the maximum value in a list of numbers.

    # Args:
    #     weather_data: A list of numbers.
    # Returns:
    #     The maximum value and it's position in the list.
    # """



def generate_summary(weather_data):
    count = 0
    all_min = []
    all_max = []
    for row in weather_data:
        count += 1
        all_min.append(row[1])
        all_max.append(row[2])
    min_value, min_position = find_min(all_min)
    minimum_c = convert_f_to_c (min_value)
    min_temp = format_temperature (minimum_c)
    min_date = convert_date(weather_data[min_position][0])
    max_value, max_position = find_max(all_max)
    max_c = convert_f_to_c (max_value)
    max_temp = format_temperature (max_c)
    max_date = convert_date(weather_data[max_position][0])
    av_low = calculate_mean(all_min)
    av_low_c = convert_f_to_c(av_low)
    av_high = calculate_mean(all_max)
    av_high_c = convert_f_to_c(av_high)
    summary = ""
    summary += f"{count} Day Overview\n"
    summary += f"  The lowest temperature will be {min_temp}, and will occur on {min_date}.\n"
    summary += f"  The highest temperature will be {max_temp}, and will occur on {max_date}.\n"
    summary += f"  The average low this week is {format_temperature(av_low_c)}.\n"
    summary += f"  The average high this week is {format_temperature(av_high_c)}.\n"
    return summary


    # """Outputs a summary for the given weather data.

    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    # """


def generate_daily_summary(weather_data):
    summary = ""
    for rows in weather_data:
        if len(rows) != 0:
            summary += f"---- {convert_date(rows[0])} ----\n"
            summary += f"  Minimum Temperature: {format_temperature(convert_f_to_c(int(rows[1])))}\n"
            summary += f"  Maximum Temperature: {format_temperature(convert_f_to_c(int(rows[2])))}\n"
            summary += f"\n"
    return summary

    # """Outputs a daily summary for the given weather data.

    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    # """
    