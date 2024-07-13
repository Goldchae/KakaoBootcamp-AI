import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

# 인터렉티브 시각화 (확대)

# 샘플 데이터 생성
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Sales': [150, 200, 180, 220, 250, 230]
}
df = pd.DataFrame(data)

# 인터랙티브 선 그래프 생성
fig = px.line(df, x='Month', y='Sales', title='Monthly Sales')
plt.savefig('interactive.png')



# 시각화 요소를 통한 설득력 있는 이야기 구성

# 데이터 정의
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 20, 25]

# 강조할 데이터
highlight = [False, False, True, False]

# 그래프 생성
plt.figure(figsize=(10, 6))
bars = plt.bar(categories, values, color=['grey' if not h else 'orange' for h in highlight])
plt.title('Category Values with Emphasis')
plt.xlabel('Category')
plt.ylabel('Value')

# 강조할 데이터 포인트에 텍스트 추가
for bar in bars:
    if bar.get_height() == max(values):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 5, 'Highest Value', ha='center', color='white', weight='bold')

plt.savefig('visualization1.png')



# 데이터 정의
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 20, 25]

# 그래프 생성
plt.figure(figsize=(10, 6))
plt.bar(categories, values, color='grey')
plt.title('Category Values')
plt.xlabel('Category')
plt.ylabel('Value')
plt.savefig('visualization2.png')


# 애니메이션
import matplotlib.animation as animation

# 데이터 정의
fig, ax = plt.subplots()
x = np.arange(0, 10, 0.1)
line, = ax.plot(x, np.sin(x))

# 애니메이션 함수
def update(num, x, line):
    line.set_ydata(np.sin(x + num / 10.0))
    return line,

ani = animation.FuncAnimation(fig, update, frames=100, fargs=[x, line], interval=50)
plt.title('Sine Wave Animation')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('visualization3.png')



from matplotlib import rc
rc('animation', html='jshtml')
ani

import numpy as np

# 데이터 정의
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# 그래프 생성
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('visualization4.png')


# 데이터 정의
years = ['2018', '2019', '2020', '2021']
sales = [15000, 18000, 22000, 25000]

# 그래프 생성
plt.figure(figsize=(10, 6))
plt.plot(years, sales, marker='o', linestyle='-', color='b')
plt.title('Annual Sales Over Time')
plt.xlabel('Year')
plt.ylabel('Sales')
for i, txt in enumerate(sales):
    plt.annotate(txt, (years[i], sales[i]), textcoords="offset points", xytext=(0,10), ha='center')
plt.savefig('visualization5.png')


# 데이터 정의
years = ['2018', '2019', '2020', '2021']
sales = [15000, 18000, 22000, 25000]

# 그래프 생성
plt.figure(figsize=(10, 6))
plt.plot(years, sales)
plt.title('Annual Sales')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.savefig('visualization6.png')