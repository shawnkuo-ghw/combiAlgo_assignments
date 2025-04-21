import networkx as nx
import matplotlib.pyplot as plt
import random

def generate_k_colored_graph(n, k):
    G = nx.erdos_renyi_graph(n, 0.4)
    colors = [random.randint(0, k-1) for _ in range(n)]
    for node in G.nodes:
        G.nodes[node]['color'] = colors[node]
    return G

def draw_k_colored_graph(G, k):
    global COLORS
    node_colors = [G.nodes[node]['color'] for node in G.nodes]
    color_map = [COLORS[color % len(COLORS)] for color in node_colors]
    pos = nx.shell_layout(G)
    nx.draw(G, pos, node_color=color_map, with_labels=True, node_size=500, font_color='white')
    plt.show()

def draw_subgraph(G, subgraph_vertices: list):
    global COLORS
    subG = G.subgraph(subgraph_vertices)
    node_colors = [subG.nodes[node]['color'] for node in subG.nodes]
    color_map = [COLORS[color % len(COLORS)] for color in node_colors]
    pos = nx.shell_layout(subG)
    nx.draw(subG, pos, node_color=color_map, with_labels=True, node_size=500, font_color='white')
    plt.show()

def draw_graphs(G, subG_vertices: list):
    global COLORS
    subG = G.subgraph(subG_vertices)
    G_node_colors = [G.nodes[node]['color'] for node in G.nodes]
    G_color_map = [COLORS[color % len(COLORS)] for color in G_node_colors]
    subG_node_colors = [G.nodes[node]['color'] for node in subG.nodes]  # 使用原始图的节点颜色
    subG_color_map = [COLORS[color % len(COLORS)] for color in subG_node_colors]
    pos_G = nx.shell_layout(G)
    fixed_positions = {node: pos_G[node] for node in G.nodes}
    pos_subG = nx.spring_layout(subG, pos=fixed_positions, fixed=subG.nodes)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    nx.draw(G, pos_G, ax=ax1, with_labels=True, node_color=G_color_map, node_size=1000, font_size=16, font_color='black', font_weight='bold')
    ax1.set_title('Graph', fontsize=20)
    nx.draw(subG, pos_subG, ax=ax2, with_labels=True, node_color=subG_color_map, node_size=800, font_size=12, font_color='black', font_weight='bold')
    ax2.set_title('Subgraph', fontsize=20)
    plt.tight_layout()
    plt.show()

def get_adjacency_matrix(G):
    adj_matrix = nx.adjacency_matrix(G)
    adj_matrix = adj_matrix.toarray()
    return adj_matrix

def get_nodes_colors(G, n):
    colors = []
    for node in range(n):
        colors.append(G.nodes[node]['color'])
    return colors

COLORS = [
    'red', 'blue', 'green', 'orange', 'gray',
    'brown', 'pink', 'olive', 'cyan'
]

def main():
    n = 12  # 节点数
    k = 5   # 颜色数
    
    G = generate_k_colored_graph(n, k)
    subg = [0, 1, 4]
    #draw_k_colored_graph(G, k)
    #draw_subgraph(G, subg)
    draw_graphs(G, subg)


    adjacent_matrix = get_adjacency_matrix(G)
    color_list = get_nodes_colors(G, n)
    print(adjacent_matrix)
    print('Color List:')
    for node in range(n):
        print('node:', node, 'color:', G.nodes[node]['color'], 'map_color:', color_list[node])

if __name__ == "__main__":
    main()

