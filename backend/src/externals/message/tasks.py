import json
from .config import MessageConfig
from src.externals.cache.database import RedisDatabaseConnection
from src.externals.elasticsearch import ElasticConnection
from src.crawler import Browser, ExtractBenefit

message_config = MessageConfig(name_app='tasks')

app = message_config.get_client()

@app.task
def verify_cached_data(cpf: str):
    cache_db = RedisDatabaseConnection()
    cache_conn = cache_db.get_connection()

    cached_data = cache_conn.get(cpf)

    if not cached_data:
        return cpf
    
    return cached_data
      
@app.task
def extract_data(arg: any, username: str, password: str):
    if isinstance(arg, bytes):
        return arg

    browser = Browser(headless=True)
    extract_benefit = ExtractBenefit(browser)
    
    response = extract_benefit.execute(arg, username, password)

    if 'msg' in response:
        return response

    data = {
        'cpf': arg,
        'matriculas': [response]
    }

    return data

@app.task
def save_in_cache(data: any):
    if isinstance(data, bytes):
        return data
    
    if 'msg' in data:
        return data
    
    cache_db = RedisDatabaseConnection()
    cache_conn = cache_db.get_connection()
    
    cache_conn.set(data['cpf'], json.dumps(data))

    return data
    

@app.task
def index_data(data: any):
    if isinstance(data, bytes):
        return json.loads(data)
    
    if 'msg' in data:
        return data
    
    es = ElasticConnection()
    es_conn = es.get_connection()
    
    es_conn.index(index='matriculas', id=data['cpf'], document=data)

    return data
    



    

    
