import argparse
from simpletransformers.ner import NERModel
from sklearn.metrics import f1_score
import os
import pandas as pd

def ner_model(input_file, output_file):
    if not os.path.exists(output_file):
        os.makedirs(output_file)

    custom_labels = ["O", "B-Disease", "I-Disease", "B-RNA", "I-RNA"]

    model = NERModel(
        "bert", "model2-NER-RD",
        labels=custom_labels,
        use_cuda=False,
    )

    def f1_multiclass(labels, preds):
        return f1_score(labels, preds, average='micro')

    result, model_outputs, predictions = model.eval_model(input_file, output_dir=output_file)

    predictions_flattened = [pred for sublist in predictions for pred in sublist]

    with open(input_file, 'r') as f:
        lines = f.readlines()
    empty_line_indices = [i for i, line in enumerate(lines) if line.strip() == '']

    df = pd.read_csv(input_file, sep=' ', header=None)

    df['predictions'] = predictions_flattened

    lines = df.values.tolist()

    for index in empty_line_indices:
        lines.insert(index, [''])

    with open(os.path.join(output_file, 'ner_result_conll.txt'), 'w') as f:
        for line in lines:
            f.write(' '.join(str(x) for x in line) + '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Input file path')
    parser.add_argument('-o', '--output', help='Output directory path')
    args = parser.parse_args()
    ner_model(args.input, args.output)
