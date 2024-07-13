import matplotlib.pyplot as plt

# 혼란스러움

# 데이터 정의
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [150, 180, 175, 200, 190, 210]

# 그래프 생성 (나쁜 예시)
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.bar(months, sales, zs=0, zdir='y', alpha=0.8)
ax.set_title('Monthly Sales (Confusing 3D Effect)')
ax.set_xlabel('Month')
ax.set_ylabel('Sales')
plt.savefig('confuse.png')



#불필요한 복잡성

# 데이터 정의
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [150, 180, 175, 200, 190, 210]
customers = [3000, 3500, 3400, 3700, 3600, 3900]

# 그래프 생성 (나쁜 예시)
plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o', label='Sales', color='blue')
plt.plot(months, customers, marker='x', label='Customers', color='green')
plt.title('Monthly Sales and Customers (Too Complex)')
plt.xlabel('Month')
plt.ylabel('Value')
plt.legend()
plt.savefig('complex.png')


# 왜곡된 데이터

# 데이터 정의
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
returns = [5, 4.5, 4, 3.8, 4.2, 3.5]

# 그래프 생성 (나쁜 예시)
plt.figure(figsize=(10, 6))
plt.bar(months, returns, color='red')
plt.title('Monthly Returns Rate (Distorted)')
plt.xlabel('Month')
plt.ylabel('Returns (%)')
plt.ylim(3.5, 5)
plt.savefig('complexity.png')


# 잘못된 차트 유형

# 데이터 정의
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [150, 180, 175, 200, 190, 210]

# 그래프 생성 (나쁜 예시)
plt.figure(figsize=(10, 6))
plt.pie(sales, labels=months, autopct='%1.1f%%')
plt.title('Monthly Sales (Inappropriate Chart Type)')
plt.savefig('wrong.png')
