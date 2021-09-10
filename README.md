![](FLOW/network_edited.jpg)

- 詳しくは Qiita 参照：https://qiita.com/ysk0832/items/633a2ebedf26d78951a8
- Spotify API を使って、あるアーティストに対して、その関連アーティストをグラフにして可視化します。可視化には NetworkX を使用。
- [Google Colab でも実行できます](https://colab.research.google.com/drive/1Aev5FZ3an13QMwJuJzP9Ahekv_Oosfs1?usp=sharing)


```bash
git clone https://github.com/yousukeayada/spotify.git
cd spotify
pip install -r requirements.txt

# client_id と client_secret を記入
python artist_relation.py
python network_graph.py
```
