@ECHO OFF
echo Installing virtual environment
python -m venv .
call Scripts\activate.bat &
pip install Django & 
py manage.py makemigrations first_one &
py manage.py migrate &
Scripts\deactivate.bat