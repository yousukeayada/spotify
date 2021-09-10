from collections import defaultdict

import pandas as pd


def str_to_list(df, column: str):
    for i in range(len(df)):
        l = df.loc[i, column][1:-1].split(", ")
        l = [s.strip("'") for s in l]
        df.loc[i, column] = l
    return df

def count_genres(artists_df):
    genres_dict = defaultdict(int)
    for genres in artists_df["genres"]:
        for g in genres:
            genres_dict[g] += 1
    genres_dict = sorted(genres_dict.items(), key=lambda x:x[1], reverse=True)

    genres_dict2 = {}
    for k, v in genres_dict:
        genres_dict2[k] = v
    return genres_dict2
    
def count_degree(G):
    degree_dict = {}
    for d in G.degree():
        degree_dict[d[0]] = d[1]
    return sorted(degree_dict.items(), key=lambda x:x[1], reverse=True)

# 双方向のエッジのみ残す
def remove_unidirectional(G):
    unidirectional = [(u, v) for u, v in G.edges() if not (v, u) in G.edges()]
    for u, v in unidirectional:
        G.remove_edge(u, v)
    return G
