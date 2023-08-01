from elasticsearch import Elasticsearch

es = Elasticsearch(['http://localhost:9200/'])

doc = {
    "teste": '56498623'
}

es.index(index='teste', id=2, document=doc)

resp = es.get(index="matriculas", id="dsaasd")
print(resp['_source'])
