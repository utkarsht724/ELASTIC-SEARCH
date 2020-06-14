from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

#Read Operation

try:


 def search_by_index_and_id():
    res = es.get(
        index="book_name",
        id=5
    )
    return res


 def search_by_index_and_query(doc_type, query):
    res = es.search(
        index="book_name",
        body=query
    )
    return query

except Exception as e:
    print("there is something wrong",e)


if __name__ == "__main__":
    res = search_by_index_and_id()
    doc_type = "authors"
    query = {}
    search_by_index_and_query(doc_type, query)