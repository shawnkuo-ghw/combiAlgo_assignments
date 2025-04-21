import networkx as nx
import matplotlib.pyplot as plt

# 创建一个示例图
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)])

# 定义要生成子图的节点集合
nodes_of_interest = [1, 3, 5]

# 生成子图
subgraph = G.subgraph(nodes_of_interest)

# 使用 spring_layout 布局算法绘制原始图和子图
pos = nx.spring_layout(G)
pos_subgraph = nx.spring_layout(subgraph)

# 创建一个画布和两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# 绘制原始图
nx.draw(G, pos, ax=ax1, with_labels=True, node_color='lightblue', node_size=1000, font_size=16, font_color='black', font_weight='bold')
ax1.set_title('Original Graph', fontsize=20)

# 绘制子图
nx.draw(subgraph, pos_subgraph, ax=ax2, with_labels=True, node_color='lightgreen', node_size=800, font_size=12, font_color='black', font_weight='bold')
ax2.set_title('Subgraph', fontsize=20)

# 显示图形
plt.tight_layout()
plt.show()

