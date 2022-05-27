### Admin 
Admin can add questions too along with a Teacher
- Create Admin account using command
    python manage.py createsuperuser

## HOW TO RUN THIS PROJECT
- Open Terminal and Execute Following Commands :
pip install -r requirements. txt

- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

- Now enter following URL in Your Browser Installed On Your Pc
http://127.0.0.1:8000/

## How to run Evaluation metrics
- Open Terminal and Execute Following Commands :
locust

This is detect the "locustfile.py" automatically.

- Go to http://0.0.0.0:8089 and locust interface will open up
- Enter number of peak users and Spawn rate and host as "http://127.0.0.1:8000/"
    and get the Evaluation.


