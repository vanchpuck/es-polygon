from elasticsearch import Elasticsearch

es = Elasticsearch("https://localhost:9200", http_auth=('elastic', 'changeme'), verify_certs=False)

doc = {
    'title': 'Kitchen',
    "polygon": {
        "type": "polygon",
        "coordinates": [
            [[0.0, 0.0], [0.0, 10.0], [10.0, 10.0], [10.0, 0.0], [0.0, 0.0]]
        ]
    }
}

resp = es.index(index="polygon", document=doc)
print(resp['result'])
