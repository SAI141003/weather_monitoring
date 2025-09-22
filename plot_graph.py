import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('weather_log.csv', names=['Time', 'Temperature', 'Humidity'])
data['Time'] = pd.to_datetime(data['Time'])

plt.figure(figsize=(10, 5))
plt.plot(data['Time'], data['Temperature'], marker='o', label='Temperature (°C)')
plt.plot(data['Time'], data['Humidity'], marker='x', label='Humidity (%)')

plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Vancouver Weather Monitoring')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.tight_layout()
plt.savefig('weather_graph.png')


