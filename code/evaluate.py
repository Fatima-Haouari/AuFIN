import pyterrier as pt
from pyterrier.measures import *
pt.init()
import glob
import pandas as pd
import argparse


def evaluate_run(pred_path,golden_path):
     golden = pt.io.read_qrels(golden_path)
     pred=pt.io._read_results_trec(pred_path)
     eval=pt.Utils.evaluate(pred, golden , metrics = [P@1, P@5,AP@5, R@5,R@100,NDCG@5],perquery=False)
     return eval
     

if __name__ == '__main__':
   parser = argparse.ArgumentParser()
   parser.add_argument("--gold-file-path", "-g", required=True, type=str,
                        help="Path to file with gold annotations.")
   parser.add_argument("--pred-file-path", "-p", required=True, type=str,
                        help="Path to file with predictions.")
   args = parser.parse_args()
   gold_file = args.gold_file_path
   pred_file = args.pred_file_path
   eval=evaluate_run(pred_file,gold_file)
   print(eval)
