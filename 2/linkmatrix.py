import pandas as pd
import numpy as np
from pagerank import power_iteration

def create_link_matrix(df):
    # links를 모두 idices로 바꿔서 새로운 칼럼에 저장
    def extract_links(df):
        df['link_idx'] = [[] for _ in range(len(df))]
        for row_idx, (idx, links) in enumerate(zip(df['idx'], df['links'])):
            for url_idx, url in zip(df['idx'], df['URL']):
                if (url in links): 
                    df.at[row_idx, 'link_idx'].append(url_idx) 
    extract_links(df)    

    # 노드 목록 생성
    nodes = df['idx'].tolist()
    
    # 인바운드 링크와 아웃바운드 링크를 저장할 딕셔너리 초기화
    inlinks = {node: set() for node in df['idx']} # 고유 'idx'
    outlinks = {node: set() for node in df['idx']}

    # 인바운드 링크와 아웃바운드 링크 채우기
    for idx, links in zip(df['idx'], df['link_idx']):
        outlinks[idx].update(links) 
        for link in links:
            inlinks[link].add(idx)
            
    # 링크 행렬 생성
    link_matrix = pd.DataFrame(0, index=nodes, columns=nodes) # 모든 값 0으로 초기화
    
    # 행렬 채우기
    for url in nodes:
        for link in outlinks[url]:
            link_matrix.loc[url, link] = 1

    # 'in'과 'out' 계산
    inlinks_num = {node: len(inlinks[node]) for node in nodes}
    inlinks_num = list(inlinks_num.values())
    outlinks_num = {node: len(outlinks[node]) for node in nodes}
    outlinks_num = list(outlinks_num.values())

    return link_matrix, inlinks_num, outlinks_num

