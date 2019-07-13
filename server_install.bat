@ECHO OFF
echo Installing virtual environment
python -m venv .
call Scripts\activate.bat &
pip install Django & 
echo Creating DB &
python pingcheck\manage.py makemigrations first_one &
python pingcheck\manage.py migrate &
Scripts\deactivate.bat