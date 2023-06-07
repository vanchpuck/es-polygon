from elasticsearch import Elasticsearch

es = Elasticsearch("https://localhost:9200", http_auth=('elastic', 'changeme'), verify_certs=False)

query = {
    "shape": {
        "polygon": {
            "shape": {
                "type": "point",
                "coordinates": [5.0, 5.0]
            },
            "relation": "INTERSECTS"
        }
    }
}

resp = es.search(index="polygon", query=query)
print(resp)
