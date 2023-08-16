from pyserini.search import SimpleSearcher
import pandas as pd
import re
import numpy as np
import argparse
import json
######################clean tweets######################################
def clean(text):
   if text is np.nan:
    return ""
   else:
    text = re.sub(r"http\S+", " ", text) # remove urls
    text = re.sub(r"RT ", " ", text) # remove rt
    text = re.sub(r"@[\w]*", " ", text) # remove handles
    text = re.sub(r"[\.\,\#_\|\:\?\?\/\=]", " ", text) # remove special characters
    text = re.sub(r'\t', ' ', text) # remove tabs
    text = re.sub(r'\n', ' ', text) # remove line jump
    text = re.sub(r"\s+", " ", text) # remove extra white space
    accents = re.compile(r'[\u064b-\u0652\u0640]') # harakaat and tatweel (kashida) to remove
     
    arabic_punc= re.compile(r'[\u0621-\u063A\u0641-\u064A\d+]+') # Keep only Arabic letters/do not remove number
    text=' '.join(arabic_punc.findall(accents.sub('',text)))
    text = text.strip()
    return text
  
#####################normalize tweets#################################

def normalize(text):
   if text is np.nan:
    return ""
   else:
    text = re.sub("[إأٱآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "ء", text)
    text = re.sub("ئ", "ء", text)
    text = re.sub("ة", "ه", text)
    return(text)

#######################################################################

def retrieve_lexical_authorities(queries_file,results_file,index,N):
    #pyserini BM25
    searcher=SimpleSearcher(index)
    searcher.set_language('ar')
    #train=pd.read_csv(queries_file, sep='\t',encoding='utf8',dtype = str)
    train = pd.read_json(queries_file)
    print(train)
    clean_queries=train['tweet_text'].apply(lambda x: clean(x)).apply(lambda x: normalize(x))
    #print(clean_queries)
    queries=clean_queries.tolist()
    queries_ids=train['rumor_id'].tolist()
    hits_number=N
    hits=searcher.batch_search(queries,queries_ids,k=hits_number)
    finaldf=pd.DataFrame()
    tweet_id_arr=[]
    Q0=[]
    user_id=[]
    rank=[]
    score=[]
    tag=[]

    for key, values in hits.items(): 
    
      for i in range(len(values)):
        tweet_id_arr.append(key)
        tag.append('BM25')
        user_id.append(values[i].docid)
        score.append(values[i].score)
        rank.append(i+1)
        #print(f'{i+1:2} {values[i].docid:15} {values[i].score:.5f} {values[i].raw}')

    finaldf['tweetID']=tweet_id_arr
    finaldf['Q0']=['Q0']*len(tweet_id_arr)
    finaldf['userid']=user_id
    finaldf['rank']=rank
    finaldf['score']=score
    finaldf['tag']=tag
    finaldf['userid']=finaldf['userid'].astype(str)
    finaldf.to_csv(results_file,sep='\t',index=False,header=False)    
    


if __name__ == '__main__':
   parser = argparse.ArgumentParser()
   
   parser.add_argument("--queries-file-path", "-q", required=True, type=str,
                        help="Path to file with queries.")
   parser.add_argument("--results-file-path", "-r", required=True, type=str,
                        help="Path to retrieved results.")
   parser.add_argument("--index-path", "-i", required=True,
                        help="indexed collection path.")

   parser.add_argument("--number-of-retrieved_results_per_query", "-n", required=True, type=int,
                        help="Number of retrieved results per query.") 

   

   args = parser.parse_args()
   queries_file = args.queries_file_path
   results_file = args.results_file_path
   index_path=args.index_path
   number_of_results=args.number_of_retrieved_results_per_query
   retrieve_lexical_authorities(queries_file, results_file,index_path, number_of_results)
