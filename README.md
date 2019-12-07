# Video Gallery App

A Video Gallery made using python3 and django.
This gallery has the following features:

- Users only can be registered via admin site
- The displayed tree is made scanning the "media" folder inside the project and render the structure only showing folders and videos"

## Prerequisites

- Python3
- Django
- Virtualenv

### Installing

A step by step series of examples that tell you how to get a development env running

- Clone the repository
- Open a terminal and move the de videogalleryapp
- Create a virtualenv using this command: virtualenv -p python3 venv
- Activate the virtualenv
    -- Unix: source venv/bin/activate
    -- Windows: venv\Scripts\activate
- Install dependencies: pip install -r requirements.txt
- Create an internal database and apply migrations: python manage.py migrate
- Create the superuser: python manage.py createsuperuser
- Create a filesystem structure with videos under the "media" folder. If you dont perform this, you will see an empty tree :)
- Launch the program using: python manage.py runserver 0:8000
- Connect via browser to the IP:8000
