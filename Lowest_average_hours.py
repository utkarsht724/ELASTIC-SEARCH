# Import elastic search module
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
#Lowest no of average hours
try:
    res=es.search(index="user_info",body={"from": 0, "size": 0, "query": {"match_all": {}}, "aggs": {"avg_hours":{"avg": {"field": "working_hours"}}}})
    lowest_average_hours=es.search(index="user_info", body={"_source": ["user_name"], "query": {"range": {"working_hours": {"lt":"2019-10-24T07:08:14.818Z"}}}})
    print(lowest_average_hours)

except Exception as e:
    print("something went wrong",e)
