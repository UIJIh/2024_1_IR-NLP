import os, csv
import pandas as pd
csv.field_size_limit(100000000)

def load_scripts_vsm(directory):    
    f = open(directory,'r', encoding='utf-8')
    rdr = csv.reader(f)
    
    script_list = []
    title_list = []
    
    # make scriptlist and titlelist
    for idx, line in enumerate(rdr):
        #print(idx)
        #if len(line) <= 2:
         #   continue
        script_list.append(line[2])
        title_list.append(line[1])
    f.close()
    return script_list, title_list    

def load_scripts_trans(directory):    
    input_csv_path = directory
    df = pd.read_csv(input_csv_path)
    
    script_list = df['script'].tolist()
    title_list = df['title'].tolist()

    return script_list, title_list

import pandas as pd
from collections import Counter
import random

# 데이터 전처리 및 로드
def load_data(input_csv_path):
    df = pd.read_csv(input_csv_path)
    scripts = df['script'].tolist()
    labels = df['label'].tolist()
    titles = df['title'].tolist()
    # 데이터 필터링 및 균형 맞추기
    def filter_and_balance_dataset(scripts, labels, titles, target_labels):
        # 필터링
        filtered_data = [(script, label, title) for script, label, title in zip(scripts, labels, titles) if label in target_labels]
    
        # 필터링된 데이터 분리
        filtered_scripts, filtered_labels, filtered_titles = zip(*filtered_data)
    
        # 균형 맞추기
        data = list(zip(filtered_scripts, filtered_labels, filtered_titles))
        counter = Counter(filtered_labels)
        min_count = min(counter.values())
    
        balanced_data = []
        for label in counter:
            label_data = [item for item in data if item[1] == label]
            balanced_data.extend(random.sample(label_data, min_count))
    
        random.shuffle(balanced_data)
        balanced_scripts, balanced_labels, balanced_titles = zip(*balanced_data)
        return list(balanced_scripts), list(balanced_labels), list(balanced_titles)
        
    # 포함할 레이블
    target_labels = ['Action', 'Drama', 'Comedy']    
    # 데이터 필터링 및 균형 맞추기
    scripts, labels, titles = filter_and_balance_dataset(scripts, labels, titles, target_labels)
    
    return scripts, labels, titles