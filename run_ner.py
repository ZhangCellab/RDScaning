import argparse
from simpletransformers.ner import NERModel
from sklearn.metrics import f1_score
import os
import pandas as pd

def ner_model(input_file, output_file):
    if not os.path.exists(output_file):
        os.makedirs(output_file)

    custom_labels = ["O", "B-Disease", "I-Disease", "B-RNA", "I-RNA"]

    # 使用训练好的模型
    model = NERModel(
        "bert", "model2-NER-RD",
        labels=custom_labels,
        use_cuda=False,
    )

    # 定义评估指标
    def f1_multiclass(labels, preds):
        return f1_score(labels, preds, average='micro')

    # 获取模型的预测结果
    result, model_outputs, predictions = model.eval_model(input_file, output_dir=output_file)

    # 将不规则的二维数组转换为一维数组
    predictions_flattened = [pred for sublist in predictions for pred in sublist]

    # 读取输入文件，并保存空行的位置
    with open(input_file, 'r') as f:
        lines = f.readlines()
    empty_line_indices = [i for i, line in enumerate(lines) if line.strip() == '']

    # 读取输入文件
    df = pd.read_csv(input_file, sep=' ', header=None)

    # 将预测结果添加到新的列中
    df['predictions'] = predictions_flattened

    # 将 DataFrame 转换为列表
    lines = df.values.tolist()

    # 将空行添加回去
    for index in empty_line_indices:
        lines.insert(index, [''])

    # 保存到新的文件中
    with open(os.path.join(output_file, 'ner_result_conll.txt'), 'w') as f:
        for line in lines:
            f.write(' '.join(str(x) for x in line) + '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Input file path')
    parser.add_argument('-o', '--output', help='Output directory path')  # 修改为目录路径
    args = parser.parse_args()
    ner_model(args.input, args.output)
