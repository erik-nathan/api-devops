# API DevOps

## 1. Primeiro Passo

- Inicializar o ambiente virtual
```
python3 -m venv .venv
```

- Ativar o ambiente virutal
```
source .venv/bin/activate
```

## 2. Instalar as bibliotecas que serão utilizadas na API

- Flask
```
pip install flask
```

- Flask RestFul
```
pip install flask-restful
```

### 3. Estrutura do projeto
- .
- ├── api
- │├── models -> Todo processamento interno da API
- │└── resources -> Apenas o que o usuário tem acesso
- └── README.md

### 4. Criar o __init__.py dentro da pasta ./api/
- Dentro do arquivo init, importar as bibliotecas a serem utilizadas no projeto
```
from flask import Flask
from flask_restful import Api
```


#### settings.py
- Esse arquivo contém as configurações, que serião

### Rodar a aplicação
- gunicorn --bind 0.0.0.0:5000 -w 4 run:app
- gunicorn -c setup.py run:app