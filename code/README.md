# Lexical retrieval
To replicate our results we provide our [lexical retrieval model](https://github.com/Fatima-Haouari/AuFIN/blob/main/code/lexical_retrieval.py). To run the code you need to install [Pyserini](https://github.com/castorini/pyserini) as shown bellow:
> pip install pyserini==0.14.0 <br/>

then run the code as follows:
> python lexical_retrieval.py -q rumors.json -r lexical_authorities.txt -i bio_lists_index -n 1000
 <br/>



# Scorer
To evaluate your models, we provide a [scorer](https://github.com/Fatima-Haouari/AuFIN/blob/main/code/evaluate.py). To run the scorer you need to install [Pyterrier](https://pyterrier.readthedocs.io/en/latest/) as shown below:
> pip install python-terrier==0.7.2 <br/>

To evaluate the output of your model which should be in the output format required, please run the below:

> python evaluate.py -g relevance_judgments.txt -p lexical_authorities.txt <br/>

where lexical_authorities.txt is the output of your model, and [relevance_judgments.txt](https://github.com/Fatima-Haouari/AuFIN/blob/main/data/relevance_judgments.txt) is the golden qrels file provided by us.
