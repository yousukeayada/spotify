import sys
from ast import literal_eval

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

from util import *


artists_df = pd.read_csv("artists.csv", converters={"genres":literal_eval, "related_artist_ids":literal_eval, "related_artist_names":literal_eval})

genres_dict = count_genres(artists_df)
for k, v in genres_dict.items():
    print(k, v)


# ネットワーク可視化
# G = nx.Graph()
G = nx.MultiDiGraph()

# node データの追加
names = [name for name in artists_df["name"]]
G.add_nodes_from(names)

edges = []
for name, related_artist_names in zip(artists_df["name"], artists_df["related_artist_names"]):
    for related_name in related_artist_names:
        if related_name in names:
            e = (name, related_name)
            edges.append(e)
            # print(e)

# edge データの追加
G.add_edges_from(edges)

# print(G.number_of_edges())
# G = remove_unidirectional(G)
# print(G.number_of_edges())

degree_dict = count_degree(G)
print(degree_dict)

for d in zip(*G.in_degree()):
    max_in_degree = max(d)

plt.figure(figsize=(30, 30), dpi=300)
pos = nx.spring_layout(G, k=0.3, seed=23)

node_size = [popularity*40 for popularity in artists_df["popularity"]]
node_alpha = [d[1] / max_in_degree for d in G.in_degree()]
# nx.draw(G, with_labels=True, node_size=node_size, alpha=node_alpha)
nx.draw_networkx_nodes(G, pos, node_color='red',alpha=node_alpha, node_size=node_size, edgecolors="black")
text_items = nx.draw_networkx_labels(G, pos, font_size=5, font_weight="bold")
nx.draw_networkx_edges(G, pos, alpha=0.4, edge_color='royalblue')

# 日本語フォントを使う
if sys.platform == "darwin":
    font_path = "/System/Library/Fonts/ヒラギノ角ゴシック W8.ttc"
elif sys.platform == "linux":
    font_path = "~/.fonts/NotoSansCJKjp-hinted/NotoSansCJKjp-Bold.otf"
font_prop = FontProperties(fname=font_path, weight=1000, size=5)
for t in text_items.values():
    t.set_fontproperties(font_prop)

plt.savefig("network.png")
# plt.show()
