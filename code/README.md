# Indexing users documents
To index the users documents you need to install [Pyserini](https://github.com/castorini/pyserini) as shown bellow:
> pip install pyserini==0.14.0 <br/>

You need to process the users contents, e.g., Twitter lists by translating if needed, cleanining, normalizing and concatenate them into a single document as a json file. Please check the users documents format [here](https://github.com/Fatima-Haouari/AuFIN/tree/main/code/users_documents_sample)). The code to translate, clean, normalize the users content is [here]().

To index the users documents run the following command:

> python -m pyserini.index -input users_documents_sample -collection JsonCollection -generator DefaultLuceneDocumentGenerator -index indexes/bio_lists_index -threads 5 -storePositions -storeDocvectors -storeRaw -language ar <br/>

where [users_documents_sample](https://github.com/Fatima-Haouari/AuFIN/tree/main/code/users_documents_sample) is the sample of users documents provided by us, and indexes/bio_lists_index is the path to save the index.


# Lexical retrieval
To replicate our results we provide our [lexical retrieval model](https://github.com/Fatima-Haouari/AuFIN/blob/main/code/lexical_retrieval.py). To run the code you need to install [Pyserini](https://github.com/castorini/pyserini) as shown bellow:
> pip install pyserini==0.14.0 <br/>

then run the code as follows:
> python lexical_retrieval.py -q rumors.json -r lexical_users.txt -i bio_lists_index -n 1000
 <br/>

 where [rumors.json](https://github.com/Fatima-Haouari/AuFIN/blob/main/data/rumors.json) is the file containing all the 150 rumors, lexical_users.txt is the name of file to save the results, and [bio_lists_index](https://drive.google.com/drive/u/0/folders/1y0Fhc5IFNvdg0ZdUjS5lkBB9QZaEcQ7E)  is the selected indexed collection.

# Initial retrieval
To get the initial users, run the [initial retrieval model](https://github.com/Fatima-Haouari/AuFIN/blob/main/code/initial_retrieval.py) as follows:
> python initial_retrieval.py -i lists_count.pkl  -f followers_following_count.pkl -l lexical_users.txt -r initial_users.txt
<br/>

where [lists_count.pkl](https://github.com/Fatima-Haouari/AuFIN/blob/main/data/lists_count.pkl) is a dictionary with lists count of all users, [followers_following_count.pkl](https://github.com/Fatima-Haouari/AuFIN/blob/main/data/followers_following_count.pkl) is a dictionary with the ratio of followers to followees of all users, lexical_users.txt is the output of the lexical retrieval model, and initial_users.txt is the name of file to save the results.



# Scorer
To evaluate your models, we provide a [scorer](https://github.com/Fatima-Haouari/AuFIN/blob/main/code/evaluate.py). To run the scorer you need to install [Pyterrier](https://pyterrier.readthedocs.io/en/latest/) as shown below:
> pip install python-terrier==0.7.2 <br/>

To evaluate the output of your model which should be in the output format required, please run the below:

> python evaluate.py -g relevance_judgments.txt -p lexical_authorities.txt <br/>

where lexical_authorities.txt is the output of your model, and [relevance_judgments.txt](https://github.com/Fatima-Haouari/AuFIN/blob/main/data/relevance_judgments.txt) is the golden qrels file provided by us.
