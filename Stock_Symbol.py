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
                chart_type = pygal.Line()
                return chart_type




#Selecting the time series
def getTimeSeries():
    Time_Series_options = [1,2,3,4]
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
            Time_Series = int(input('Enter time series option (1, 2, 3, 4) : '))
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


#Selecting a date
#Can be used to get a start date and an end date   
def getStartDate():
    date = input("Enter a start date in YYYY-MM-DD format: ")
    return date

def getEndDate():
    endDate = input("Enter a end date in YYYY-MM-DD format: ")
    #datetime.strptime(endDate, '%Y-%M-%D') 
    return endDate

def compareDates(date1, date2):
   if date1 < date2:
    return True
   else:
       return False
   



def main():
    print("Welcome! ")
Symbol = getSymbol()
chart = getChart()
function = getTimeSeries() # will help configure the url, currently does not change anything regardless of answer
start_date = getStartDate()
end_date = getEndDate()
    # configure url 
    
#url = f'https://www.alphavantage.co/query?function={function}&symbol={Symbol}&interval=5min&apikey=16M4EW4M4DAV8AZZ' #this is an example url
url = f'https://www.alphavantage.co/query?function={function}&symbol={Symbol}&apikey=WNHA95VNGXUV2S6K' # this is an example url
r = requests.get(url)
data = r.json()
    
date_data ={} 
for date in data.keys():
    if date >= start_date and date <= end_date:
        date_data[date] = data[date]
        
chart.title = f'{Symbol} Stock prices for ({start_date} - {end_date})'
chart.x_labels = sorted(date_data.keys())
chart.add('Open', [float(date_data[date]['Open']) for date in chart.x_labels])
chart.add('High', [float(date_data[date]['High']) for date in chart.x_labels])  
chart.add('Low', [float(date_data[date]['Low']) for date in chart.x_labels])  
chart.add('Close', [float(date_data[date]['Close']) for date in chart.x_labels])     

chart.render_in_browser()

main()