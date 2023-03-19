print("Welcome to your stock Visualizer!\n")

Stock_Symbol = input("Enter Symbol you're looking for here: ")

print('Chart Types')
print("---------------")
print('1. Bar')
print('2. Line')
chart_type = input('Enter the chart type you want (1, 2): ')
try:
    chart_type = int(chart_type)
except ValueError:
    print("Plese pick from option above")
    if chart_type == 1:
     chart_type = 'Bar'
    elif chart_type == '2':
        chart_type = 'Line'
    else:
       print('Please pick from options above')


