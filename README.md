# RDScanning
### Download:

We provide the weights of two pre-trained models after fine-tuning, and their downloads and descriptions are provided below:
* **[model-TC](https://cellknowledge.com.cn/RDScanning/model1-TC.rar)** - fine-tuned BioBERT V1.1 model weights based on RNA and disease sentence classification tasks
* **[model-NER](https://cellknowledge.com.cn/RDScanning/model2-NER-RD.rar)** - fine-tuned Bioformer8L model weights based on RNA and disease named entity recognition tasks
### Datasets:

- fine-tuning_statement.csv: There are 2082 positive sentences and 2000 negative sentences, involving a total of 3229 documents.
- fine-tuning_token.txt: 2082 positive sentences were segmented and BIO marked, with a total of 54148 tokens.
- independent_test.csv: There are 500 positive sentences and 500 negative sentences, involving a total of 874 documents.
- independent_test_token.txt: 500 positive sentences were segmented and BIO marked, with a total of 13230 tokens.
### Usage:
#### Text Classification

run `python run_classification.py -i/--input [input_file] -o/--output [output_file]` in command

- **input_file:** route to your file containing peptides to be predicted in **CSV** format.
- **output_file:** route to your result file containing prediction results in **Directory**.
- An example dataset is given in **example_classication.csv**
  
After executing the command, you will get two files: **eval_results.txt** (evaluation result) and **output.csv** (the probability of each sentence being predicted to be positive).
