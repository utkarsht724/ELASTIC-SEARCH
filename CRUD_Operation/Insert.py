from elasticsearch import Elasticsearch
es = Elasticsearch(host="localhost", port=9200)

#Insert Operation

data = {
        "author": "billgates",
        "gender": "male",
        "age": "26",
        "email":"billgates@forbes.com"
    }

def create_index():
    es.indices.create(index="book_name", ignore=400)

def insert_one_data( data):
    res = es.index(index="books_name", doc_type='authors', id=5, body=data)
    print(res)
    "{'index': 'book_name', 'type': 'authors','result': 'created', '_shards': {'total': 2, 'successful': 1, 'failed': 0}, '_seq_no': 4, '_primary_term': 1}"

create_index()
insert_one_data(data)
