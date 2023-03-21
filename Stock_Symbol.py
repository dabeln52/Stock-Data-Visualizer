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
                chart_type = "bar"
                return [Stock_Symbol, chart_type]
            elif chart_type == 2:
                chart_type = "line"
                return [Stock_Symbol, chart_type]
            elif chart_type == 3:
                print("\nThank You for Using Our Program! Goodbye!\n")
                quit()


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
                return 'TIME_SERIES_INTRADAY'
            elif Time_Series == 2:
                return 'TIME_SERIES_DAILY'
            elif Time_Series == 3: 
                return 'TIME_SERIES_WEEKLY'
            elif Time_Series == 4:
                return 'TIME_SERIES_MONTHLY'
            elif Time_Series == 5:
                print("\nThank You for Using Our Program! Goodbye!\n")
                quit()

  
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

def compareDates(date1, date2):
    # part of what we need implement is having a start and stop date, we also need to be able to tell when a date is before another one or not
    # wouldn't hurt to make a function that compares if date1 is ahead of or after date2

    # also need to be able to 
    return

def main():

    Stock_Symbol_Chart_Type = startMenu()
 
    function = timeSeries() # will help configure the url, currently does not change anything regardless of answer

    # configure url 
    
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=16M4EW4M4DAV8AZZ' #this is an example url
    # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo' # this is an example url
    r = requests.get(url)
    data = r.json()
    # print(data)

    # making data accessable
    data = data['Time Series (5min)']
    # data = data['Time Series (Daily)']
    for dataPoint in data:
        print(f"open is {data[dataPoint]['1. open']}\nhigh is {data[dataPoint]['2. high']}\nlow is {data[dataPoint]['3. low']}\nclose is {data[dataPoint]['4. close']}\nvolume is {data[dataPoint]['5. volume']}\n----------------")
    # dataPoint is just the date, it is used as the key in the dictionary

    # print dates
    for dataPoint in data:
        print(dataPoint)

    # bar graph
    if (Stock_Symbol_Chart_Type[1] == "bar"):
        # still need to figure out how to use the data to make a useful bar graph
        return

        
    # line graph
    else:
        chart = pygal.Line()
        chart.title = "Data from 2023-03-17"
        open = []
        high = []
        low = []
        close = []
        for dataPoint in data:
            open.append(float(data[dataPoint]['1. open']))
            high.append(float(data[dataPoint]['2. high']))
            low.append(float(data[dataPoint]['3. low']))
            close.append(float(data[dataPoint]['4. close']))

        chart.add("Open", open)
        chart.add("High", high)
        chart.add("Low", low)
        chart.add("Close", close)
        
        chart.render_in_browser()

main()