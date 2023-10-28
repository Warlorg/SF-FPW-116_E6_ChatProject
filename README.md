### Quick start

Platform-depending options and libraries are adjusted to Windows.

Clone repository to ChatProject_dir directory


At ChatBoard_dir directory, start and adjust virtual environment
```bash
python -m venv venv
venv/scripts/activate
cd .\ChatProject\ 
pip install -r requirements.txt
```

Mark ChatProject directory as Sources root

Create superuser
```
python manage.py createsuperuser
``` 

Start server
```bash
python manage.py runserver
```

Main page works at url http://127.0.0.1:8000/chat_app/ 