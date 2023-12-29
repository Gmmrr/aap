import re
from collections import Counter
import matplotlib.pyplot as plt

#### Read Data ####
def read_fasta(file_path):
    """
    讀取FASTA檔案，返回一個字典，其中鍵是序列的標識，值是對應的序列字符串。
    """
    sequences = {}
    current_id = None
    current_sequence = ""

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                # 這是標識行
                if current_id is not None:
                    # 將前一個序列保存到字典中
                    sequences[current_id] = current_sequence
                current_id = line[1:]
                current_sequence = ""
            else:
                # 這是序列行
                current_sequence += line

        # 處理最後一個序列
        if current_id is not None:
            sequences[current_id] = current_sequence

    return sequences

# 使用範例
file_path = 'benchmarkdataset_train.fasta'  # 請替換成你的FASTA檔案的路徑
fasta_data = read_fasta(file_path)

# 打印第一個標識和序列
first_id = list(fasta_data.keys())[0]
first_sequence = fasta_data[first_id]
print("標識:", first_id)
print("序列:", first_sequence)
#### Read Data end ####


# 假設protein_sequences是包含所有蛋白質序列的列表
protein_sequences = ["FLKDHRISTFKNWPF", "FLSSRLQDLYSIVRRADRAA", ...]  # 包含所有蛋白質序列的列表

# 將所有蛋白質序列合併成一個長字符串
all_sequences = "".join(protein_sequences)

# 使用正則表達式找到所有的三個胺基酸組合
three_aa_groups = re.findall(r'(?=(...))', all_sequences)

# 計算每組三個胺基酸的出現次數
aa_counts = Counter(three_aa_groups)

# 取得前8000個組合
top_aa_counts = aa_counts.most_common(8000)

# 提取組合和對應的次數
groups, counts = zip(*top_aa_counts)

# 繪製長條圖
plt.bar(range(len(groups)), counts, tick_label=groups)
plt.xlabel('三個胺基酸組合')
plt.ylabel('出現次數')
plt.title('蛋白質序列中每組三個胺基酸的出現次數')
plt.show()
