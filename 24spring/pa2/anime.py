import networkx as nx
import matplotlib.pyplot as plt

# 创建一个示例图
G = nx.Graph()
edges = [(1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (3, 5), (4, 5)]
G.add_edges_from(edges)

# 设置团的颜色和透明度
node_color = 'lightblue'
clique_color = 'orange'
alpha_value = 0.4

# 初始化画布和子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# 固定图的布局
pos = nx.shell_layout(G)
nx.draw(G, pos, with_labels=True, ax=ax1, node_color=node_color, node_size=1000, font_size=16, font_color='black', font_weight='bold')
ax1.set_title('Original Graph', fontsize=16)

# 逐步寻找团的过程
cliques = list(nx.find_cliques(G))
for i, clique in enumerate(cliques):
    # 绘制当前找到的团
    clique_nodes = list(clique)
    nx.draw_networkx_nodes(G, pos, nodelist=clique_nodes, ax=ax2, node_color=clique_color, node_size=1000, alpha=alpha_value)
    nx.draw_networkx_edges(G, pos, edgelist=edges, ax=ax2, alpha=0.5)
    nx.draw_networkx_labels(G, pos, ax=ax2, font_size=12, font_color='black', font_weight='bold')
    ax2.set_title(f'Finding Clique {i+1}', fontsize=16)
    plt.pause(1.5)
    ax2.clear()

# 最后显示找到的所有团
ax2.clear()
nx.draw(G, pos, with_labels=True, ax=ax2, node_color=node_color, node_size=1000, font_size=16, font_color='black', font_weight='bold')
for clique in cliques:
    clique_nodes = list(clique)
    nx.draw_networkx_nodes(G, pos, nodelist=clique_nodes, ax=ax2, node_color=clique_color, node_size=1000, alpha=alpha_value)
nx.draw_networkx_edges(G, pos, edgelist=edges, ax=ax2, alpha=0.5)
nx.draw_networkx_labels(G, pos, ax=ax2, font_size=12, font_color='black', font_weight='bold')
ax2.set_title('All Cliques Found', fontsize=16)

plt.tight_layout()
plt.show()

