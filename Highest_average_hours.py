# Import elastic search module

from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
#Highest average no of hours by email

try:

 def average_hours():
  res=es.search(index="user_info",body={"from": 0, "size": 0, "query": {"match_all": {}}, "aggs": {"avg_hours":{"avg": {"field": "working_hours"}}}})
  highest_avergae_hours= es.search(index="user_info", body={"_source": ["user_name"], "query": {"range": {"working_hours": {"gt":"2019-10-24T07:08:14.818Z"}}}})
  print(highest_avergae_hours)

except Exception as e:
    print("there is something wrong" ,e)

average_hours()
