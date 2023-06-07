from elasticsearch import Elasticsearch

es = Elasticsearch("https://localhost:9200", http_auth=('elastic', 'changeme'), verify_certs=False)

request_body = {
    "settings" : {
        "number_of_shards": 1,
        "number_of_replicas": 1
    },
    'mappings': {
        "properties": {
            "polygon": {
                "type": "shape"
            }
        }
    }
}

es.indices.create(index='polygon', body=request_body)
