import pygal
import requests
from alpha_vantage.timeseries import TimeSeries


print("Welcome to your stock Visualizer!\n")

Stock_Symbol = input("Enter Symbol you're looking for here: ")
chart_options = [1, 2]
chart_type = None
while chart_type not in chart_options:
    print('Chart Types')
    print("---------------")
    print('1. Bar')
    print('2. Line')
    try:    
      chart_type = int(input('Enter the chart type you want (1, 2): '))
    except ValueError:
        print("Plese pick from option above")
    else:   
     if chart_type == 1:
         chart_type = pygal.Bar()
         break
     elif chart_type == 2:
        chart_type = pygal.Line()
        break


Time_Series_options = [1,2,3,4]
Time_Series = None

while Time_Series not in Time_Series_options:
    print("Select the Time Series of the char you want to Generate")
    print("--------------------------------------------------------")
    print('1. Intraday')
    print('2. Daily')
    print('3. Weekly')
    print('4. Monthly')
    try: 
     Time_Series = int(input('Enter time series option (1, 2, 3, 4):'))
    except ValueError: 
            print("Please choose from options above.")
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
  
        


