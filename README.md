# Simple-Backend-Project

### Purpose
A project used to implement a FastAPI backend with a MySQL database. We have a table called `Items` and we perform the following CRUD operations:
1. `GET` - get the item with the specified `/{item_id}` 
2. `POST` - create a new item 
3. `PUT` - update an existing item with `/{item_id}`
4. `DELETE` -  Delete an existing item 

### How to Run File:
From the `/simple-backend-project` directory, run the following:
- `python3 -m uvicorn app.main:app --reload`

Once the backend server is running, access the Swagger Docs by appending `/docs` to the url given 


