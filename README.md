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
