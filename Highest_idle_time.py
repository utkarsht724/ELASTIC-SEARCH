# Import elastic search module
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

#Highest no of time late coming by email
try:
     res= es.search(index="user_info",body={"from": 0, "size": 0, "query": {"match_all": {}}, "aggs": {"avg_hours":{"avg": {"field": "idle_time"}}}})
     highest_idle_time=es.search(index="user_info", body={"_source": ["user_name"], "query": {"range": {"idle_time": {"gt":"2019-10-24T02:01:52.500Z"}}}})
     print(highest_idle_time)

except Exception as e:
    print("there is something wrong", e)