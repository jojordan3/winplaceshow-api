# Terminal Commands

This was completed on a mac inside a conda base environment using the Anaconda-provided VS Code with integrated terminal
Python version used here was 3.6

Be sure you have Heroku installed. If not, get it at the [Heroku Dev Center](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)

**This is the initial setup** (comments specified with ^^^)

First, create a repo on your GitHub initialized with a README, .gitignore, and probably MIT license.

======================================================
$ git clone https://github.com/MYUSERNAME/MYREPO.git
        ^^^ Obviously use *your* username and *your* repo name
$ cd MYREPO
$ python -m venv venv
$ source venv/bin/activate
$ pip install -U pip
$ pip install -U pipenv
$ pipenv install Django djangorestframework django-cors-headers psycopg2 coreapi
        ^^^ coreapi is optional
$ django-admin startproject MYPROJECT
$ cd MYPROJECT
$ django-admin startapp MYAPI
$ cd ..
$ python manage.py migrate
$ python manage.py createsuperuser
$ 

$ heroku create
$ git push heroku master
$ heroku ps:scale web=1
        ^^^ Tells Heroku to set 1 web worker to run your app
            The command `$ heroku ps:scale web=0` will shut down your app until you run `heroku ps:scale web=1` again
$ pipenv install *anything else you'll need like sklearn libraries, pandas, numpy, keras...*
        ^^^ *Anything* else you install, also add it to `requirements.txt`
