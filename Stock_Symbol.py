#importing resources
import pygal
import requests
from alpha_vantage.timeseries import TimeSeries

#begining menu/ entering symbol and selecing chart type
def startMenu():
    print("Welcome to your Stock Visualizer!\n")
    Stock_Symbol = input("Enter Symbol you're looking for here: ")
    chart_options = [1, 2, 3]
    chart_type = None
    while chart_type not in chart_options:
        print('Chart Types')
        print("---------------")
        print('1. Bar')
        print('2. Line')
        print('3. Exit')
        
        try:    
            chart_type = int(input('Enter the chart type you want (1, 2, 3): '))
        except ValueError:
            print("\nPlese pick from options above\n")
        else:   
            if chart_type == 1:
                chart_type = pygal.Bar()
                break
            elif chart_type == 2:
                chart_type = pygal.Line()
                break
            elif chart_type == 3:
                print("\nThank You for Using Our Program! Goodbye!\n")
                quit()
startMenu()

#Selecting the time series
def timeSeries():
    Time_Series_options = [1,2,3,4,5]
    Time_Series = None

    while Time_Series not in Time_Series_options:
        print("Select the Time Series of the char you want to Generate")
        print("--------------------------------------------------------")
        print('1. Intraday')
        print('2. Daily')
        print('3. Weekly')
        print('4. Monthly')
        print('5. Exit')
        try: 
            Time_Series = int(input('Enter time series option (1, 2, 3, 4, 5) : '))
        except ValueError: 
                print("\nPlease choose from options above.\n")
                continue
        else:
            if Time_Series == 1:
                function = 'TIME_SERIES_INTRADAY'
                break
            elif Time_Series == 2:
                function = 'TIME_SERIES_DAILY'
                break
            elif Time_Series == 3: 
                function = 'TIME_SERIES_WEEKLY'
                break
            elif Time_Series == 4:
                function ='TIME_SERIES_MONTHLY'
                break
            elif Time_Series == 5:
                print("\nThank You for Using Our Program! Goodbye!\n")
                quit()
     
timeSeries()
  
#Selecting a date
#Can be used to get a start date and an end date   
def date():
    Selected_Date = None
    Date_Error_Message = "That date is not formatted correctly. Please try again."

    while Selected_Date == None:
        userResponse = input("Please enter a date in YYYY-MM-DD format: ")
        if (userResponse.find("-") == -1):
            print(Date_Error_Message)
            date()
        elif (userResponse.count() != 10):
            print(Date_Error_Message)
            date()
        else:
            Selected_Date = userResponse
            return Selected_Date

date()