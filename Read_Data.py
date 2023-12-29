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
