import json
from .config import MessageConfig
from src.externals.cache.database import RedisDatabaseConnection
from src.crawler import Browser, ExtractBenefit

message_config = MessageConfig(name_app='tasks')

app = message_config.get_client()

@app.task(bind=True)
def get_benefit(cpf: str, username: str, password: str):
    cache_db = RedisDatabaseConnection()
    cache_conn = cache_db.get_connection()

    cached_data = cache_conn.get(cpf)

    if cached_data:
        return cached_data
    
    browser = Browser(headless=False)
    extract_benefit = ExtractBenefit(browser)
    
    matriculas = extract_benefit.execute(cpf, username, password)

    data = {
        'cpf': cpf,
        'matriculas': [matriculas]
    }

    cache_conn.set(cpf, json.dumps(data))
    
    return data

    

    
