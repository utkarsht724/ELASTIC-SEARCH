#import elastic search module
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Delete Operation

try:

  def delete_by_query(_index, query):
    res = es.delete_by_query(
        index="books_name",
        body={"query": {"match": query}},
        _source=True
    )
    return res

except Exception as e:
   print("there is something went wrong",e)

if __name__ == "__main__":
    query = {"author": "biilgates"}
    res = delete_by_query(query)