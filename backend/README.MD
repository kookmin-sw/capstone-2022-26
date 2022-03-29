# Getting Started
    
Install virtualenv:

    $ pip install virtualenv
    

Create virtualenv:

    $ virtualenv venv
    
    
Activate the virtualenv for your project:

    $ venv/Scripts/activate
    
    
Install project dependencies:

    $ pip install -r requirements/requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
