from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

#Update Operation

try:

 def update_data_by_index(index,update_data):
    res = es.update(
        index="books_name",
        doc_type="authors",
        id=5,
        body=update_data
    )
    return res

except Exception as e:
    print("there is something wrong",e)


if __name__ == "__main__":
   update_data = {"doc": {"age": 26}}
   res =update_data_by_index(update_data)
   query = {"author": "billgates"}
   field = "age"
   update_data = 19


