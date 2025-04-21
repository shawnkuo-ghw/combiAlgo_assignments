import networkx as nx
import matplotlib.pyplot as plt

COLORS = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']

def draw_graphs(G, subG_vertices: list):
    global COLORS
    subG = G.subgraph(subG_vertices)
    G_node_colors = [G.nodes[node]['color'] for node in G.nodes]
    G_color_map = [COLORS[color % len(COLORS)] for color in G_node_colors]
    subG_node_colors = [G.nodes[node]['color'] for node in subG.nodes]  # 使用原始图的节点颜色
    subG_color_map = [COLORS[color % len(COLORS)] for color in subG_node_colors]
    pos_G = nx.shell_layout(G)
    
    # 获取原始图节点的位置信息
    fixed_positions = {node: pos_G[node] for node in G.nodes}
    
    # 使用固定位置绘制子图
    pos_subG = nx.spring_layout(subG, pos=fixed_positions, fixed=subG.nodes)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    nx.draw(G, pos_G, ax=ax1, with_labels=True, node_color=G_color_map, node_size=1000, font_size=16, font_color='black', font_weight='bold')
    ax1.set_title('Graph', fontsize=20)

    nx.draw(subG, pos_subG, ax=ax2, with_labels=True, node_color=subG_color_map, node_size=800, font_size=12, font_color='black', font_weight='bold')
    ax2.set_title('Subgraph', fontsize=20)
    
    plt.tight_layout()
    plt.show()

# 示例用法
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)])
for node in G.nodes:
    G.nodes[node]['color'] = node  # 为每个节点设置一个颜色
subG_vertices = [1, 3, 5]  # 指定子图的节点集合
draw_graphs(G, subG_vertices)

