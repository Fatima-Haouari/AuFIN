import json
import pandas as pd
import glob
import math
import time
import pickle
import argparse

    
#initial retrieval by reranking using users network features
def initial(lexical_users,lists_count_file,followers_following_file):
    # get the start time
    st = time.time()
    file_to_read = open(followers_following_file, "rb")
    followers_count_dict = pickle.load(file_to_read)
    file_to_read = open(lists_count_file, "rb")
    lists_count_dict = pickle.load(file_to_read)
    new_scores = []
    for row in lexical_users.itertuples():
        new_scores.append((row.score * math.log2(lists_count_dict[row.userid]+2))+(row.score * math.log2(followers_count_dict[row.userid]+2)))
    lexical_users['new_score']=new_scores
    lexical_users['tag']=['initial']*len(lexical_users) 
    lexical_users=lexical_users.groupby('tweetid').apply(lambda x: x.sort_values('new_score',ascending=False))
    lexical_users=lexical_users.reset_index(drop=True)
    lexical_users['new_rank']=lexical_users.groupby('tweetid')['new_score'].rank(ascending=False,method='first').astype('int32')
    lexical_users=lexical_users[['tweetid','Q0','userid','new_rank','new_score','tag']]
    #print(lexical_users)
    # get the end time
    et = time.time()
    # get the execution time
    elapsed_time = et - st
    print('Initial execution time:', elapsed_time, 'seconds')
    return lexical_users



if __name__ == '__main__':
   parser = argparse.ArgumentParser()
   
   parser.add_argument("--lists-count-file-path", "-i", required=True, type=str,
                        help="Path to dictionary with lists count for all users.")

   parser.add_argument("--followers-following-file-path", "-f", required=True, type=str,
                        help="Path to dictionary with followers to followers ratio for all users.")

   parser.add_argument("--lexical-file-path", "-l", required=True, type=str,
                        help="Path to file with lexically retrieved users.")
   parser.add_argument("--results-file-path", "-r", required=True, type=str,
                        help="Path to initially retrieved results.")
  
   

   args = parser.parse_args()

   lists_count_file = args.lists_count_file_path
   followers_following_file = args.followers_following_file_path
   lexical_file = args.lexical_file_path
   results_file = args.results_file_path
   
   lexical_users=pd.read_csv(lexical_file,names=['tweetid','Q0','userid','rank','score','tag'],sep="\t")
   lexical_users['userid']=lexical_users['userid'].astype('str')
   initial_users=initial(lexical_users,lists_count_file,followers_following_file)
   initial_users.to_csv(results_file,sep='\t',index=False,header=False)

    
