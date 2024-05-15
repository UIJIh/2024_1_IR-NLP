import networkx as nx
import pandas as pd

def networkx_pagerank(df):
    Graph = nx.DiGraph()
    for url, links in zip(df['idx'], df['link_idx']):
        links = [int(item) for item in links if item.isdigit()]
        for link in links:
            Graph.add_edge(url, link)
            result = nx.pagerank(Graph, alpha=0.85, max_iter=1000, tol= 0.00001) # 내가 만든 파일이랑 조건을 맞추기 위함            
    return result