import argparse
from simpletransformers.classification import ClassificationModel
import pandas as pd
import numpy as np
import csv
from sklearn.metrics import f1_score, accuracy_score
import os

def classification_model(input_file, output_file):
    if not os.path.exists(output_file):
        os.makedirs(output_file)

    sens = []
    labels = []

    with open(input_file, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sens.append(row['Description'])
            labels.append(row['Labels'])

    labels = list(map(int, labels))

    data = {
        'text': sens,
        'labels': labels
    }

    file_df = pd.DataFrame(data)

    print(file_df)

    model = ClassificationModel('bert','model1-TC',num_labels=2,use_cuda=False)

    def f1_multiclass(labels, preds):
        return f1_score(labels, preds, average='micro')

    result, model_outputs, wrong_predictions = model.eval_model(file_df, f1=f1_multiclass, acc=accuracy_score, output_dir=output_file)
    probabilities = np.exp(model_outputs) / np.sum(np.exp(model_outputs), axis=1, keepdims=True)
    probabilities_Pos = probabilities[:, 1]

    output_df = pd.DataFrame({
        'text': sens,
        'probabilities_Pos': probabilities_Pos
    })

    output_df.to_csv(os.path.join(output_file, 'output.csv'), index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Input file path')
    parser.add_argument('-o', '--output', help='Output directory path')
    args = parser.parse_args()
    classification_model(args.input, args.output)
