# FastAPI pybites learning path

Welcome to this FastAPI learning path. In the next 10 Bites you will write a simple API to track food / calories.

Let's break this problem down in some easily digestable steps or Bite exercises:

1. Learn how to instantiate a FastAPI app instance and write your first view or endpoint < this Bite.

2. Get familiar with typing using the Pydantic library. We'll make a Food model which we'll use throughout this Learning Path.

3. Create food objects. To keep things simple we will use a simple list of Food objects in memory. We'll introduce databases and relational tables in our SQLModel learning path.

4. Retrieve food objects (all or a particular one).

5. Update and delete food object. This concludes the full CRUD (create-read-update-delete) of foods.

6. Pydantic part II: define two more models: User and FoodEntry.

7. Repeat the CRUD but now for food logging.

8. Add exception handling to our API.

9. Render the food log in a basic HTML template (Yes! FastAPI can also be used as web framework!)

10. Add authentication to our API.

## Bites of Py

### 1.1 - FastAPI Hello World ( bite 336 )

In this first Bite of the challenge, let's make a FastAPI app instance and a view that returns {"message": "Welcome to PyBites' FastAPI Learning Path 🐍 🎉"} when hitting the root endpoint (/) with a GET request (see the tests).

Some notes on this learning path:

- To use earlier solutions as template code for later exercises without spoiling anything, you must solve the exercises in order, that is completing earlier exercises unlocks later ones.

- You can make the FastAPI endpoints async or not, the tests will work either way.

Good luck and welcome onboard! We hope this will be a fun and rich learning experience.

### 1.2 - A little detour: Pydantic Intermediate level icon
### 2.1 - Create food objects
### 2.2 - Retrieve food objects
### 2.3 - Update and delete food objects
### 2.4 - Pydantic part II
### 2.5 - Food logging CRUD
### 2.6 - FastAPI Exception handling
### 2.7 - Return an HTML response

## Advanced level icon

### 3.1 - FastAPI Authentication with JWT (JSON Web Tokens)

## [FastAPI tutorial ](https://fastapi.tiangolo.com/tutorial/)

```bash
pip install "fastapi[all]"
```

```bash
uvicorn main:app --reload
```

- **main**: the file `main.py` (the Python 'module')
- **app**:  the object tcreated inside of main.py with the line app = `FastAPI()`.
- **--reload**: make the server restart after code changes.  Only use for development.

### uvicorn ERROR: [Errno 98] Address already in use

```bash
# find the process using the port
lsof -i :8000
# and kill it
kill -9 process_id
```
