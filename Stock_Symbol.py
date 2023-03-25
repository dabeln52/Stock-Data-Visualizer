#importing resources
import pygal
import requests
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime

#begining menu/ entering symbol and selecing chart type
def getSymbol():
    print("Welcome to your Stock Visualizer!\n")
    Stock_Symbol = input("Enter Symbol you're looking for here: ")
    return Stock_Symbol
def getChart():
    chart_options = [1, 2]
    chart_type = None
    while chart_type not in chart_options:
        print('Chart Types')
        print("---------------")
        print('1. Bar')
        print('2. Line')
        print('3. Exit')
        
        try:    
            chart_type = int(input('Enter the chart type you want (1, 2): '))
        except ValueError:
            print("\nPlese pick from options above\n")
        else:   
            if chart_type == 1:
                chart_type = pygal.Bar()
                return chart_type
            elif chart_type == 2:
                chart_type = pygal.Line(x_label_rotation=20)
                return chart_type
            elif chart_type == 3:
                exit()

#Selecting the time series
def getTimeSeries():
    Time_Series_options = [1,2,3,4,6]
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
                Time_Series = 'TIME_SERIES_INTRADAY'
                return Time_Series
            elif Time_Series == 2:
                Time_Series =  'TIME_SERIES_DAILY'
                return Time_Series
            elif Time_Series == 3: 
                Time_Series = 'TIME_SERIES_WEEKLY'
                return Time_Series
            elif Time_Series == 4:
                Time_Series = 'TIME_SERIES_MONTHLY'
                return Time_Series
            elif Time_Series == 5:
                exit()


#Selecting a date
#Can be used to get a start date and an end date   
def selectDates():

    start_date = None
    end_date = None

    Date_Error_Message = "That date is not formatted correctly. Please try again."

    # selecting start date
    while start_date == None:
        try:
            userResponse = input("Enter a start date in YYYY-MM-DD format: ")
            testDateTime = datetime.fromisoformat(userResponse) #used to check formatting and later to compare dates
        except Exception:
            print(Date_Error_Message)
            continue

        start_date = userResponse

    # selecting end date
    while end_date == None:
        try:
            userResponse = input("Enter a end date in YYYY-MM-DD format: ")
            testDateTime = datetime.fromisoformat(userResponse) #used to check formatting and later to compare dates
        except Exception:
            print(Date_Error_Message)
            continue

        end_date = userResponse
    
    return [start_date, end_date]

def compareDates(date1, date2):
   
    try:
       date1 = datetime.fromisoformat(date1)
       date2 = datetime.fromisoformat(date2)
    except:
        print("this is an error")

    if date1 <= date2:
        return True
    else:
        return False
   



def main():
    print("Welcome! ")
    Symbol = getSymbol()
    chart = getChart()
    function = getTimeSeries()
    date_data = []
    start_date = None
    end_date = None

    # making sure start date is before end date and vice versa
    startAndEndCorrect = False
    while (startAndEndCorrect == False):
        dates = selectDates()

        start_date = dates[0]
        end_date = dates[1]

        startAndEndCorrect = compareDates(start_date, end_date)
        if (startAndEndCorrect == False): print("Start date must be earlier than end date. Please try again.")

    if (function == "TIME_SERIES_INTRADAY"):
        # interval can be changed here, I chose 15 minute
        url = f'https://www.alphavantage.co/query?function={function}&symbol={Symbol}&interval=15min&apikey=16M4EW4M4DAV8AZZ'
        r = requests.get(url)
        data = r.json()

        date_data = data['Time Series (15min)'] # any interval changes need to be here too

    elif (function == "TIME_SERIES_DAILY"): # this is a premium feature and does not work right now. if a premium key was used it would likely work
        url = f'https://www.alphavantage.co/query?function={function}&symbol={Symbol}&apikey=16M4EW4M4DAV8AZZ'
        r = requests.get(url)
        data = r.json()

        date_data = data["Time Series (Daily)"]

    elif (function == "TIME_SERIES_WEEKLY"):
        url = f'https://www.alphavantage.co/query?function={function}&symbol={Symbol}&apikey=16M4EW4M4DAV8AZZ'
        r = requests.get(url)
        data = r.json()

        date_data = data['Weekly Time Series']

    else: # function == TIME_SERIES_MONTHLY
        url = f'https://www.alphavantage.co/query?function={function}&symbol={Symbol}&apikey=16M4EW4M4DAV8AZZ'
        r = requests.get(url)
        data = r.json()

        date_data = data['Monthly Time Series']        

    # configuring chart
    chart.title = f'{Symbol} Stock Prices for ({start_date} - {end_date})'
    open = []
    high = []
    low = []
    close = []
    labels = []
    for date in date_data:
        if (compareDates(start_date, date) and compareDates(date, end_date)):
            print(date)
            print(date_data[date])
            open.append(float(date_data[date]['1. open']))
            high.append(float(date_data[date]['2. high']))
            low.append(float(date_data[date]['3. low']))
            close.append(float(date_data[date]['4. close']))
            labels.append(date)

    chart.add('Open', open)
    chart.add('High', high)
    chart.add('Low', low)
    chart.add('Close', close)
    chart.x_labels = labels

    chart.render_in_browser()

main()