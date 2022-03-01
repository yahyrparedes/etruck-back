# ETruck Project 

### Requirement

- Python-3*
- pip - virtualenv




### Run Develoment Mode

1. Create Virtual Enviroment
1. Activate Virtual Enviroment
2. Install dependencies 
3. Execute migrations
4. Load data for fixtures (gender, documenttype)
5. Create super user for access /admin (email, first_name, last_name, password)
6. Run Server

### Commands

- ```$ virtualenv venv```
- ```$ .\venv\Scripts\activate  or source venv/bin/activate```
- ```$ pip install -r requirements.txt```
- ```$ python manage.py loaddata gender.json documenttype.json```
- ```$ python manage.py createsuperuser```
- ```$ python manage.py runserver``` 


## Happy Code 