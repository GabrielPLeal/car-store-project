# Car Store Project


Project serves to add and list customers and cars they own. With this you can visualize the sales possibilities. The project oSelective process of AdviceHealth.


## Authors

- [@GabrielPLeal](https://www.github.com/GabrielPLeal)


## Documentation

### 1 - Business rules:

```text
Nork-Town is a weird place. Crows cawk the misty morning while old men squint. It’s a small
town, so the mayor had a bright idea to limit the number of cars a person may possess. One
person may have up to 3 vehicles. The vehicle, registered to a person, may have one color,
‘yellow’, ‘blue’ or ‘gray’. And one of three models, ‘hatch’, ‘sedan’ or ‘convertible’.
Carford car shop want a system where they can add car owners and cars. Car owners may
not have cars yet, they need to be marked as a sale opportunity. Cars cannot exist in the
system without owners.

Requirements

● Setup the dev environment with docker
○ Using docker-compose with as many volumes as it takes
● Use Python’s Flask framework and any other library
● Use any SQL database
● Secure routes
● Write tests
```

### 2 - Technologies used:

```text
- Django
- Html
- Css
- Sqlite
```

### 3 - How run the project:

#### 3.1 - Clone the project:

```text
Open the terminal and clone the project with command below:

git clone link
```

#### 3.2 - Create virtualenviroment:

```text
virtualenv -p /usr/bin/python3.10 venv
```

#### 3.3 - Activate virtualenv:

```text
source venv/local/bin/activate

OR

source venv/bin/activate
```

#### 3.4 - Install the requirements:

```text
Entry in project directory and install the requirements with command below:

pip install -r requirements.txt
```

#### 3.5 - Run project:

```text
In the terminal run the command below:

python manage.py runserver

The command will generate a link. Click on it to access the website.
```

### 4 - Create new customers and vehicles:


#### 4.1 - Acesses django admin page:

```text
http://127.0.0.1:8000/admin

User: admin
Password: admin1234

Later of acess the page you see four fields in the window"groups", "users", "customers" and "vehicles".
```

#### 4.2 - Create customers

```text
Just click in "customers" field and fill in the fields.
```

#### 4.2 - Create vehicles

```text
Just click in "vehicles" field and fill in the fields.
```

#### 5 - Run tests:

```text
python manage.py test
```
