# 文件名: visualize_graph.py

import networkx as nx
import matplotlib.pyplot as plt

def main():
    # 创建一个空的图
    G = nx.Graph()

    # 添加节点
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)

    # 添加边
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(2, 3)

    # 绘制图形
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=20, font_color='black')

    # 显示图形
    plt.show()

if __name__ == "__main__":
    main()

