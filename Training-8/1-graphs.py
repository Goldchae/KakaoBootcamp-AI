import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt



# 히트맵(HeatMap)

# 샘플 데이터 생성
data = np.random.rand(10, 12)

# 히트맵 생성
plt.figure(figsize=(10, 8))
sns.heatmap(data, annot=True, cmap='coolwarm')
plt.title('Sample Heatmap')
plt.savefig('HeatMap.png')




# 트리맵(TreeMap)

import plotly.express as px

df = px.data.gapminder().query("year == 2007")
fig = px.treemap(df, path=[px.Constant("world"), 'continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
plt.savefig('TreeMap.png')





# 버블차트(Bubble Chart)

# 샘플 데이터 정의
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]
sizes = [100, 200, 300, 400, 500]

# 버블 차트 생성
plt.figure(figsize=(10, 6))
plt.scatter(x, y, s=sizes, alpha=0.5, c=sizes, cmap='viridis')
plt.title('Sample Bubble Chart')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.colorbar()
plt.savefig('Bubble.png')




# Radar Chart
# 샘플 데이터 정의
labels = ['Shots', 'Speeds', 'Touches', 'Dribbles', 'Heading']
values = [4, 3, 2, 5, 4]
values += values[:1]
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]

# 레이더 차트 생성
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='red', alpha=0.4)
ax.plot(angles, values, color='black', linewidth=2)
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
plt.title('Football Player A')
plt.savefig('Radar.png')




# Sanky Diagram

import plotly.graph_objects as go

# 샘플 데이터 정의
fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=["A", "B", "C", "D", "E", "F"],
        color=["blue", "blue", "blue", "blue", "blue", "blue"]
    ),
    link=dict(
        source=[0, 1, 0, 2, 3, 3],
        target=[2, 3, 3, 4, 4, 5],
        value=[8, 4, 2, 8, 4, 2]
    )
))

fig.update_layout(title_text="Sample Sankey Diagram", font_size=10)
plt.savefig('Sanky.png')


