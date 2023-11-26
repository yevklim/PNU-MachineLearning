# environment and requirements

How to create new python environment and put it into .env folder:
```bash
python3 -m venv .env
```

How to activate python environment:
```bash
source ./.env/bin/activate
```

How to freeze python packages list into requirements.txt:
```bash
pip freeze > requirements.txt
```

How to istall python packages from requirements.txt:
```bash
pip install -r requirements.txt
```