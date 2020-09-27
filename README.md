# wddemo
# customer Api
# Requirements
    python 3.7.4/Latest
    pip
    Redis 
    
# To Run Project Local 

1. clone the repository by invoking the command at terminal.
    git clone https://github.com/abhidevx/wddemo.git

2. create a python virtual environment in directory
    python -m venv "your_environment_name"
    go to scripts and type activate.This way your virtual environment will be activated.

3. installing project dependencies.
    with virtual environment activated go to project root directory.
    Run Command pip install -r requirements.txt

4. migrations
    python manage.py makemigrations
    python manage.py migrate.

5. Running
    python manage.py runserver
    project will run at http://127.0.0.1:8000/