@ECHO OFF
call Scripts\activate.bat &
start "" http:\\localhost:8000\ &
python pingcheck\manage.py runserver