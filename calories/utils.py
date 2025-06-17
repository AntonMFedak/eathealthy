import matplotlib.pyplot as plt
import base64
from io import BytesIO

def encode_chart_to_image():
    buffer = BytesIO() # Create a BytesIO buffer to hold the image data
    plt.savefig(buffer, format='png') # Save the plot to the buffer in PNG format
    buffer.seek(0) # Reset buffer position to the beginning
    image_png = buffer.getvalue() # Get the PNG image data from the buffer
    chart = base64.b64encode(image_png).decode('utf-8') # Encode the image to base64 and decode to utf-8
    buffer.close()
    return chart

def plot_data(x, y):
    plt.switch_backend('Agg')  # Use a non-GUI backend for rendering
    plt.figure(figsize=(10, 5))
    plt.title('Calories Data')
    fig, ax = plt.subplots()
    ax.pie(y, labels=x)
    #plt.show()
    chart = encode_chart_to_image()  # Encode the chart to base64
    return chart