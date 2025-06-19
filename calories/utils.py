import matplotlib.pyplot as plt
import base64
from io import BytesIO

chart_labels = [] # List to hold cleaned x-axis labels
chart_values = [] # List to hold cleaned y-axis values

chart_macro_labels = ['Fat Total', 'Protein', 'Carbohydrates Total']  # Labels for the macro nutrients
chart_macro_values = []  # Values for the macro nutrients
explode_labels = [0, 0.2, 0]

""" 
PREPARATION FOR NESTED PIE CHART

# Define the outer and inner labels for the pie chart
chart_labels_outer = ['Carbohydrates', 'Total Fat', 'Protein']
chart_values_outer = [80, 40, 25]
colors_outer = ['red', 'blue', 'green']
chart_labels_inner = ['Sugar', 'Fiber Content', 'Saturated Fat', 'Cholesterol', 'Protein']
chart_values_inner = [20, 15, 5, 2, 25]
colors_inner = ['orange', 'yellow', 'turquoise', 'purple', 'olive']
 """

# Function to encode the chart to a base64 image
def encode_chart_to_image():
    buffer = BytesIO() # Create a BytesIO buffer to hold the image data
    plt.savefig(buffer, format='png') # Save the plot to the buffer in PNG format
    buffer.seek(0) # Reset buffer position to the beginning
    image_png = buffer.getvalue() # Get the PNG image data from the buffer
    chart = base64.b64encode(image_png).decode('utf-8') # Encode the image to base64 and decode to utf-8
    buffer.close()
    return chart

# Function to clean the x-axis labels by removing units and formatting them
# will be necessary for nested pie chart also
def clean_x(x):
    global chart_labels
    for item in x:
        if 'mg' in item:
            chart_labels.append(item[:-3].replace('_', ' ').title())  # Remove 'mg' from the end and replace underscores with spaces and title case
        else:
            chart_labels.append(item[:-2].replace('_', ' ').title())  # Remove 'g' from the end and replace underscores with spaces and title case
    return chart_labels

# Function to clean the y-axis values by converting mg to g if necessary
# will be necessary for nested pie chart also
def clean_y(x, y):
    global chart_values
    for str in x:
        if 'mg' in str:
            chart_values.append(y[x.index(str)]/1000)  # Convert mg to g
        else:
            chart_values.append(y[x.index(str)])  # Keep the value as is
    return chart_values

# Function to get the macro nutrients from the chart values
def get_macros():
    global chart_macro_values, chart_values, chart_labels
    for str in chart_labels:
        if str.title() in chart_macro_labels:
            chart_macro_values.append(chart_values[chart_labels.index(str.title())])
    return chart_macro_values

# Function to plot the data as a pie chart
def plot_data(x, y):
    global chart_labels, chart_values, chart_macro_labels, chart_macro_values, explode_labels
    #print(x)
    #print(y)
    clean_x(x)  # Ensure x strings are without units
    clean_y(x, y)  # Ensure y values are of the same greateness
    get_macros()  # Extract macro nutrient values
    plt.switch_backend('Agg')  # Use a non-GUI backend for rendering
    plt.figure(figsize=(10, 10))
    fig, ax = plt.subplots()
    # ENTIRE PIE CHART, BAD VISIBILITY, THUS TRASFORMATION TO MACRO NUTRIENTS UNTILL NESTED PIE CHART IS READY
    #ax.pie(chart_values, labels=chart_labels, autopct='%1.1f%%', startangle=90, counterclock=False, radius=1.5)
    ax.pie(chart_macro_values, labels=chart_macro_labels, autopct='%1.1f%%', startangle=90, counterclock=False, explode=explode_labels, wedgeprops={'edgecolor': 'white'})
    fig.tight_layout()  # Adjust layout to prevent overlap
    chart = encode_chart_to_image()  # Encode the chart to base64
    # Reset the global variables for the next plot
    chart_labels = []
    chart_values = []
    chart_macro_values = []
    return chart

""" 
    PREPARATION FOR NESTED PIE CHART
    
    def plot_data(x, y):
    global chart_labels, chart_values
    #print(x)
    #print(y)
    clean_x(x)  # Ensure x strings are without units
    clean_y(x, y)  # Ensure y values are of the same greateness
    plt.switch_backend('Agg')  # Use a non-GUI backend for rendering
    plt.figure(figsize=(10, 10))

    # Create the outer pie chart
    plt.pie(chart_values_outer, labels=chart_labels_outer, colors=colors_outer, autopct='%1.1f%%', radius=1.2, wedgeprops={'edgecolor': 'white', 'width': 0.3})

    # Create the inner pie chart
    plt.pie(chart_values_inner, labels=chart_labels_inner, colors=colors_inner, autopct='%1.1f%%', radius=0.8, wedgeprops={'edgecolor': 'white', 'width': 0.3})
 """