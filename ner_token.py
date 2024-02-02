import csv
import argparse
from ops import json_to_sent, input_form

def process_file(input_file):
    with open(input_file, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        PMID = [row['PMID'] for row in reader]

    # 重新打开文件以读取 'Description' 列的值
    with open(input_file, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        Sentence = [row['Description'] for row in reader]


    # 检查 PMID 和 Sentence 列表的长度是否相等
    if len(PMID) != len(Sentence):
        print("Error: The lengths of PMID and Sentence lists are not equal.")
        exit(1)

    data = [{
        "pmid":"123",
        "abstract": "This is a dummy data to learn how these codes (ner.ops - json_to_sent and input form) are working. Thanks."
    }]

    MAX_CHARS_WORD = 22

    # 使用 'w' 模式打开文件，这将覆盖文件中的所有内容
    with open("test_token.csv", 'w', newline='', encoding='utf-8-sig') as csv_file:
        writer = csv.writer(csv_file)

        for count in range(len(PMID)):
            data[0]["pmid"] = PMID[count]
            data[0]["abstract"] = Sentence[count]

            sentData = json_to_sent(data, is_raw_text=True)
            sentData

            for key, values in input_form(sentData, max_input_chars_per_word = MAX_CHARS_WORD)[data[0]["pmid"]].items():
                if key == "words":
                    for sentence in values:
                        for word in sentence:
                            writer.writerow([word])
                        writer.writerow([" "])  # 在每个句子之后添加一个空行

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a csv file.')
    parser.add_argument('-i', '--input', help='Input file name', required=True)
    args = parser.parse_args()

    process_file(args.input)
