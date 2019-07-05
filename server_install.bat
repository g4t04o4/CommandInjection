@ECHO OFF
echo Installing virtual environment
python -m venv .
call Scripts\activate.bat &
pip install Django & 
Scripts\deactivate.bat