from linkmatrix import create_link_matrix
from pagerank import power_iteration
from networkx import networkx_pagerank
import pandas as pd

def main():
    df = pd.read_csv('df_links.csv') 
    # link matrix
    link_matrix, inlinks, outlinks = create_link_matrix(df)
    # 1. page ranks that i made
    page_ranks = power_iteration(link_matrix)
    # # 2. with networkx
    # net_pageranks = networkx_pagerank(df)
    print('\n\n===================== PAGERANK =====================')
    #print(page_ranks)
    # print('=====================PAGERANK WITH NETWORKX=====================')
    # print(net_pageranks)

    # graph - df
    result = pd.DataFrame({
        'id' : df['idx'],
        'rank' : page_ranks.values,
        'in' : inlinks,
        'out' : outlinks,
        'url' : df['URL']
    })
    print(result,'\n\n')

    print('===================== DESC =====================')
    desc = result.sort_values(by='rank', ascending=False)
    print(desc)

    print('\n\n===================== ASC =====================')
    asc = result.sort_values(by='rank', ascending=True)
    print(asc)

if __name__ == "__main__":
    main()
