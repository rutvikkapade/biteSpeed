
# Fluxkart

### Deployed on render.com 

```
https://bitespeed-rlgu.onrender.com/api/swagger/
```
### Available Endpoint 

```
[Post] 
https://bitespeed-rlgu.onrender.com/api/identify/
```

## Installation Guide for local

Follow these steps to set up the project on your local machine.

### 1. Create and Activate Virtual Environment
Create a virtual environment to manage project dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 2. Install Requirements
Install the necessary dependencies from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 3. Change Directory
Navigate to the project directory.

```bash
cd fluxkart
```

### 4. Make Migrations
Generate the database schema migrations for the `api` app.

```bash
python3 manage.py makemigrations api
```

### 5. Apply Migrations
Apply the migrations to create the database schema.

```bash
python3 manage.py migrate
```


### 6. Run the Development Server
Start the Django development server.

```bash
python3 manage.py runserver
```

Your project should now be running at `http://127.0.0.1:8000/`.

Start the Django development server.

```bash
python3 manage.py runserver
```

Your project should now be running at `http://127.0.0.1:8000/`.

### 7. Available Endpoint

Swagger

```
http://127.0.0.1:8000/api/swagger/
```

Identify [Post]

```
http://127.0.0.1:8000/api/identify/
```
