import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


# 데이터 정의
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [150, 200, 180, 220, 250, 230]
# 막대그래프 생성
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
plt.bar(months, sales, color='skyblue', label='Sales')  # 막대그래프 생성
plt.title('Monthly Sales')  # 제목 추가
plt.xlabel('Month')  # x축 레이블 추가
plt.ylabel('Sales')  # y축 레이블 추가
plt.legend()  # 범례 추가
plt.grid(True)  # 그리드 추가
plt.savefig('bar.png')  # 그래프 출력

# 데이터 정의
labels = ['Product A', 'Product B', 'Product C', 'Product D']
sizes = [400, 300, 500, 100]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # 첫 번째 조각을 약간 떨어뜨리기
# 간결한 디자인의 파이차트
plt.figure(figsize=(8, 8))  # 그래프 크기 설정
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Sales Distribution - Simple Design')
plt.axis('equal')  # 파이차트를 원형으로 유지
plt.savefig('pie1.png')
# 복잡한 디자인의 파이차트
plt.figure(figsize=(8, 8))  # 그래프 크기 설정
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Sales Distribution - Complex Design')
plt.axis('equal')  # 파이차트를 원형으로 유지
plt.savefig('pie2.png')

# 데이터 정의
data = {'Year': [2018, 2019, 2020, 2021], 'Visitors': [12000, 18000, 23000, 30000]}
df = pd.DataFrame(data)
# 선그래프 생성
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
sns.lineplot(x='Year', y='Visitors', data=df, marker='o', label='Visitors')
plt.title('Annual Website Visitors')  # 제목 추가
plt.xlabel('Year')  # x축 레이블 추가
plt.ylabel('Number of Visitors')  # y축 레이블 추가
plt.legend()  # 범례 추가
plt.grid(True)  # 그리드 추가
plt.savefig('lineplot.png')

# 데이터 정의
data = {'Year': [2018, 2019, 2020, 2021],
        'Product A': [1500, 2000, 2400, 2800],
        'Product B': [2300, 2700, 3000, 3500],
        'Product C': [1800, 2200, 2600, 3000]}
df = pd.DataFrame(data)
# 복합 차트 생성
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
sns.lineplot(x='Year', y='Product A', data=df, marker='o', label='Product A')
sns.lineplot(x='Year', y='Product B', data=df, marker='o', label='Product B')
sns.lineplot(x='Year', y='Product C', data=df, marker='o', label='Product C')
plt.title('Annual Product Sales')  # 제목 추가
plt.xlabel('Year')  # x축 레이블 추가
plt.ylabel('Sales')  # y축 레이블 추가
plt.legend()  # 범례 추가
plt.grid(True)  # 그리드 추가
plt.savefig('lineplot2.png')

# 데이터 생성
np.random.seed(10)
data = np.random.randn(1000)
# 히스토그램 생성
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram of Random Data')  # 제목 추가
plt.xlabel('Value')  # x축 레이블 추가
plt.ylabel('Frequency')  # y축 레이블 추가
plt.grid(True)  # 그리드 추가
plt.savefig('hist.png')

# 데이터 생성
np.random.seed(10)
data = {
    'x': np.random.randn(100),
    'y': np.random.randn(100)
}
df = pd.DataFrame(data)
# 산점도 생성
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
sns.scatterplot(x='x', y='y', data=df)
plt.title('Scatter Plot of Random Data')  # 제목 추가
plt.xlabel('X')  # x축 레이블 추가
plt.ylabel('Y')  # y축 레이블 추가
plt.grid(True)  # 그리드 추가
plt.savefig('scatterplot.png')

# 데이터 생성
np.random.seed(10)
data = {
    'Category': np.random.choice(['A', 'B', 'C'], 100),
    'Value': np.random.randn(100)
}
df = pd.DataFrame(data)
# 박스플롯 생성
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
sns.boxplot(x='Category', y='Value', data=df)
plt.title('Box Plot of Random Data by Category')  # 제목 추가
plt.xlabel('Category')  # x축 레이블 추가
plt.ylabel('Value')  # y축 레이블 추가
plt.grid(True)  # 그리드 추가
plt.savefig('boxplot.png')