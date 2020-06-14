# Import elastic search module
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
#Highest no of late comings
try:
    late_comers=es.search(index="user_info", body={"_source": ["user_name"], "query": {"range": {"start_time": {"gt":"2019-10-24T09:30:00.818Z"}}}})
    print(late_comers)

except Exception as e:
    print("there is something wrong", e)