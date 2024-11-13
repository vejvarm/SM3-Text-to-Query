import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from rank_bm25 import BM25Okapi
from typing import List, Tuple

class BM25Retriever:
    def __init__(self, csv_file: str):
        self.df = pd.read_csv(csv_file)
        self.group_templates()
        self.vectorizer = CountVectorizer(tokenizer=self.tokenize)
        self.bm25 = None
        self.preprocess()

    def group_templates(self):
        template_ids = {template: idx for idx, template in enumerate(self.df['question_template'].unique())}
        self.df['question_template_id'] = self.df['question_template'].map(template_ids)
    
    @staticmethod
    def tokenize(text: str) -> List[str]:
        return text.lower().split()

    def preprocess(self):
        corpus = self.df['question'].tolist()
        tokenized_corpus = [self.tokenize(doc) for doc in corpus]
        self.bm25 = BM25Okapi(tokenized_corpus)

    def retrieve(self, query: str, top_k: int = 5) -> List[Tuple[str, str, str, str, str]]:
        tokenized_query = self.tokenize(query)
        doc_scores = self.bm25.get_scores(tokenized_query)
        top_indices = np.argsort(doc_scores)[-top_k:][::-1]
        
        results = []
        for idx in top_indices:
            row = self.df.iloc[idx]
            results.append((
                row['question'],
                row['sparql'],
                row['sql'],
                row['cypher'],
                row['mql']
            ))
        
        return results
    
    def retrieve_by_template(self, query: str, top_k: int = 5) -> List[Tuple[str, str, str, str, str]]:
        tokenized_query = self.tokenize(query)
        doc_scores = self.bm25.get_scores(tokenized_query)
        top_indices = np.argsort(doc_scores)[-top_k*20:][::-1]
        
        results = []
        added_templates_ids = []
        for idx in top_indices:
            row = self.df.iloc[idx]
            if row['question_template_id'] in added_templates_ids:
                continue
            added_templates_ids.append(row['question_template_id'])
            results.append((
                row['question'],
                row['sparql'],
                row['sql'],
                row['cypher'],
                row['mql']
            ))
        return results[:top_k]


def get_examples(train_file, question, query_language, bm_shots):
    retriever = BM25Retriever(train_file)
    top_n = retriever.retrieve(question, bm_shots)
    l2p = {
        "cypher": "Cypher",
        "sql": "SQL",
        "mql": "MQL",
        "sparql1": "SPARQL",
        "sparql2": "SPARQL",
        "mql": "MongoDB"}
    res = []
    for i, (question, sparql, sql, cypher, mql) in enumerate(top_n, 1):
        if query_language not in l2p:
            raise ValueError(f"Unsupported query language: {query_language}")
        if "sparql" in query_language:
            query = sparql
        else:
            query = eval(query_language)
        res.append(f"[Q]: {question}\n[{l2p[query_language]}]: {query}\n")
    res = "\n".join(res)
    return res

def get_examples_from_diverse_template(train_file, question, query_language, bm_shots):
    retriever = BM25Retriever(train_file)
    top_n = retriever.retrieve_by_template(question, bm_shots)
    l2p = {
        "cypher": "Cypher",
        "sql": "SQL",
        "mql": "MQL",
        "sparql1": "SPARQL",
        "sparql2": "SPARQL",
        "mql": "MongoDB"}
    res = []
    for i, (question, sparql, sql, cypher, mql) in enumerate(top_n, 1):
        if query_language not in l2p:
            raise ValueError(f"Unsupported query language: {query_language}")
        if "sparql" in query_language:
            query = sparql
        else:
            query = eval(query_language)
        res.append(f"[Q]: {question}\n[{l2p[query_language]}]: {query}\n")
    res = "\n".join(res)
    return res
    

# Usage example
if __name__ == "__main__":
    retriever = BM25Retriever("data/dataset/train_dev/train.csv")
    query = "What is the city of residence of the patient with the ID 91987c26-58b8-49b9-a795-f6cff0501bc8?"
    top_5 = retriever.retrieve(query)
    print("Results:")
    for i, (question, sparql, sql, cypher, mql) in enumerate(top_5, 1):
        print(f"Result {i}:")
        print(f"Question: {question}")
        print(f"SPARQL: {sparql}")
        print(f"SQL: {sql}")
        print(f"Cypher: {cypher}")
        print(f"MQL: {mql}")
        print()
    
    top_t_by_template = retriever.retrieve_by_template(query)
    print("Results by template:")
    for i, (question, sparql, sql, cypher, mql) in enumerate(top_t_by_template, 1):
        print(f"Result {i}:")
        print(f"Question: {question}")
        print(f"SPARQL: {sparql}")
        print(f"SQL: {sql}")
        print(f"Cypher: {cypher}")
        print(f"MQL: {mql}")
        print()