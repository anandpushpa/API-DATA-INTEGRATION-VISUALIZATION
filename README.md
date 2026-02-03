# API-DATA-INTEGRATION-VISUALIZATION

*COMPANY*:CODTECH IT SOLUTIONS

*NAME*:SARANYA

*INTERN ID*:CTIS2726

*DOMAIN*:PYTHON 

*DURATION*:4 WEEKS

*MENTOR*:NEELA SANTHOSH

OUTPUT
 Internship Task Alternative – No API Required
# Weather Data Visualization using Hardcoded Values

import matplotlib.pyplot as plt

# Hardcoded weather data (example)
city = "Chennai"
temperature = 32      # °C
humidity = 70         # %
pressure = 1015       # hPa
wind_speed = 5.2      # m/s

# Print weather details
print("Weather Report")
print("----------------")
print("City Name :", city)
print("Temperature :", temperature, "degree Celsius")
print("Humidity :", humidity, "%")
print("Pressure :", pressure, "hPa")
print("Wind Speed :", wind_speed, "m/s")

# Data for graph
parameters = ["Temperature", "Humidity", "Pressure", "Wind Speed"]
values = [temperature, humidity, pressure, wind_speed]

# Plot bar graph
plt.figure(figsize=(8,5))
plt.bar(parameters, values, color=['red','blue','green','orange'])
plt.title("Weather Data Visualization for " + city)
plt.xlabel("Weather Parameters")
plt.ylabel("Values")
plt.show(block=True)
plt.savefig("output.png")
plt.show()
