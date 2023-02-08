# Пример структуры python библиотеки + REST API сервис

## Установка проекта
### 1. Скачать репозиторий
```
git clone https://github.com/albellov/snippet.git
```

### 2. Перейти в папку
```
cd snippet
```

### 3. Установить зависимости
```
pip install -r requirements.txt
```

### 4. Установить проект
```
pip install -e .
```

### 5. Запустить сервис
```
python service/app.py
```

## Использование сервиса
### 1. Ping
```
import requests

url = 'http://localhost:8080'

res = requests.get(url + '/api/v1/ping')
print(res.content.decode())
```
### 2. Predict
```
import requests
import json

url = 'http://localhost:8080'

res = requests.post(url + '/api/v1/predict', json={'count': 5, 'user_id': '125235235235'})
print(json.loads(res.content.decode()))
```
