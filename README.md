#  MY GALLERY

#### Author: [Kiptoo Rotich](https://github.com/kiptoo-rotich)

## Screenshot
### Home page
![screen](https://user-images.githubusercontent.com/48821300/125517611-8795a22b-2bb0-45f3-897e-5a07aa8587b1.png)

### Single post
![screen1](https://user-images.githubusercontent.com/48821300/125517708-6d6cd107-8078-4332-b0b4-4b9e745ef97e.png)

### Search
![screen2](https://user-images.githubusercontent.com/48821300/125517749-9048490f-095a-4132-8d22-a1954266ba61.png)

### Comment section
![screen3](https://user-images.githubusercontent.com/48821300/125517802-d0218d17-8f37-4616-96ac-de15c9ab661e.png)


## Description
This is a instagram clone project that allows authenticated user to post pictures, comment on other post and view other comment.

As a user of the web application you will be able to:

1. Sign up/Sign in
2. Post a pictures
3. Comment
4. Search a post


## Setup and installations
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.8 manage.py runserver`
* Access the live site using the local host provided
* Create your superuser account `python manage.py createsuperuser` inside virtual environment.
* Add data from admin dashboard



## Getting started

### Prerequisites
* python3.8
* virtual environment
* pip
* postgresql
  

#### Clone the Repo and rename it to suit your needs.
```bash
git clone `https://github.com/kiptoo-rotich/Gallery`
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.8 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY = 'your secret key'
DEBUG=True
DB_NAME='gallery'
DB_USER='<your database name>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='*'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.8 manage.py check
python manage.py makemigrations news
python3.8 manage.py sqlmigrate news 0001
python3.8 manage.py migrate
```

#### Run the app
```bash
python3.8 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)



## Testing the Application
`python manage.py test instapp`
        
## Built With

* [Python3.8](https://docs.python.org/3/)
* Django==3.2.5
* Postgresql 
* Boostrap
* HTML
* CSS


### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license)