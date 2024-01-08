# environment and requirements

How to create new python environment and put it into .env folder:
```bash
python3 -m venv .env
```

How to activate python environment:
```bash
source ./.env/bin/activate
```
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
./.env/Scripts/Activate.ps1
```
Going forward, `(.env)` means that the command must be executed with the environment turned on.

(.env) How to freeze python packages list into requirements.txt:
```bash
pip freeze > requirements.txt
```

(.env) How to istall python packages from requirements.txt:
```bash
pip install -r requirements.txt
```

# jupyter

(.env) How to launch JupyterLab:
```bash
jupyter lab
```

(.env) How to launch Jupyter Notebook:
```bash
jupyter notebook
```