# Lexical retrieval
To replicate our results we provide our [lexical retrieval model](). To run the code you need to install [Pyserini] as shown bellow:
> pip install pyserini==0.14.0 <br/>

then run the code as follows:
> python lexical_retrieval.py -q rumors.json -r lexical_authorities.txt -i bio_lists_index -n 1000
 <br/>



# Scorers
To evaluate your models, we provide a [scorer](https://gitlab.com/checkthat_lab/clef2023-checkthat-lab/-/blob/main/task5/scorer/evaluate.py). To run the scorer you need to install [Pyterrier](https://pyterrier.readthedocs.io/en/latest/) as shown below:
> pip install python-terrier==0.7.2 <br/>

To evaluate the output of your model which should be in the output format required, please run the below:

> python evaluate.py -g dev_relevance_judgments.txt -p dev_predicted.txt <br/>

where dev_predicted.txt is the output of your model on the dev set, and [dev_relevance_judgments.txt](https://gitlab.com/checkthat_lab/clef2023-checkthat-lab/-/blob/main/task5/data/subtask-5A-arabic/dev_relevance_judgments.txt) is the golden qrels file provided by us.
