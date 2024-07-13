import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# 데이터
weather_data = pd.read_csv('/Users/goldchae/Desktop/code/KakaoBootcamp-AI/Training-7/training/weather_classification_data.csv')

# 막대 그래프 : 계절별 온도 평균
seasons = ['Spring','Summer','Autumn','Winter']
temperatures = []
for season in seasons:
    average_temp = weather_data[weather_data['Season'] == season]['Temperature'].mean()
    temperatures.append(average_temp)

plt.figure(figsize=(10,6))
plt.bar(seasons,temperatures, color='purple' )
plt.title('seasonal temperature') 
plt.xlabel('season')
plt.xlabel('temperature')
plt.grid(True)
plt.savefig('bar.png')


# 파이 차트 : 계절별 Cloud한 날씨 수
clear_cloudCover =[]
for season in seasons:
    count = weather_data[(weather_data['Season'] == season) & (weather_data['Cloud Cover'] == 'clear')]['Season'].count()
    clear_cloudCover.append(count)

plt.figure(figsize=(8, 8))
plt.pie(clear_cloudCover, labels=seasons, autopct='%1.1f%%', startangle=140)
plt.title('Sales Distribution - Simple Design')
plt.axis('equal')  # 파이차트를 원형으로 유지
plt.savefig('pie.png')


# 선 그래프 : 계절별 온도 변화
data = {'Season': seasons, 'Average Temperature': temperatures}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6)) 
sns.lineplot(x='Season', y='Average Temperature', data=df, marker='o', label='Average Temperature')
plt.title('Seasonal Average Temperatures') 
plt.xlabel('Season') 
plt.ylabel('Temperature (°C)') 
plt.legend()  
plt.grid(True) 
plt.savefig('lineplot.png') 


# 히스토그램 : atmospheric_pressure 분포
atmospheric_pressure_list = weather_data['Atmospheric Pressure'].tolist()

plt.figure(figsize=(10, 6)) 
plt.hist(atmospheric_pressure_list, bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram of atmospheric_pressure Data')  
plt.xlabel('atmospheric_pressure')  
plt.grid(True)  
plt.savefig('hist.png')


# 산점도 : Humidity와 Wind Speed의 상관 관계 파악
data = {
    'Humidity': weather_data['Humidity'].tolist(),
    'Wind Speed':weather_data['Wind Speed'].tolist()
}
df = pd.DataFrame(data)

plt.figure(figsize=(25, 15)) 
sns.scatterplot(x='Humidity', y='Wind Speed', data=df)
plt.title('Scatter Plot of Humidity and Wind Speed')
plt.xlabel('Humidity')  
plt.ylabel('Wind Speed') 
plt.grid(True) 
plt.savefig('scatterplot.png')

# 박스 플롯 : 날씨별 UV Index 통계
data = {
    'Rainy': weather_data[weather_data['Weather Type'] == 'Rainy']['UV Index'].tolist(),
    'Cloudy': weather_data[weather_data['Weather Type'] == 'Cloudy']['UV Index'].tolist(),
    'Snowy': weather_data[weather_data['Weather Type'] == 'Snowy']['UV Index'].tolist(),
    'Sunny': weather_data[weather_data['Weather Type'] == 'Sunny']['UV Index'].tolist(),
}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))  
sns.boxplot(data=df)
plt.title('Box Plot of UV Index by weather')  
plt.xlabel('UV Index')  
plt.ylabel('weather')  
plt.grid(True) 
plt.savefig('boxplot.png')