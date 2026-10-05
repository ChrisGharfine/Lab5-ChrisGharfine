# Lab 5 – Postman and APIs

A Flask REST API for managing users in SQLite. All Python code is in `app.py`, with CORS enabled using Flask-CORS.

## Run locally

From the project folder on Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install Flask flask-cors
.\.venv\Scripts\python.exe app.py
```

The server runs at `http://localhost:5000`. Open `/api/users` to view users; the root URL `/` has no route.

The application creates `database.db` and the `users` table if they do not exist. The table contains `user_id`, `name`, `email`, `phone`, `address`, and `country`. SQLite assigns `user_id` when a user is added.

## API endpoints

| Method | Route | Response |
| --- | --- | --- |
| GET | `/api/users` | All users as a JSON array |
| GET | `/api/users/<user_id>` | One user, or `{}` if not found |
| POST | `/api/users/add` | The created user, including its ID |
| PUT | `/api/users/update` | The updated user, or `{}` if not found |
| DELETE | `/api/users/delete/<user_id>` | A JSON status message |

For POST and PUT, select **Body → raw → JSON** in Postman and use `Content-Type: application/json`.

POST body:

```json
{
  "name": "Lab Five Test",
  "email": "lab5@example.com",
  "phone": "0010000000",
  "address": "5 Test Street",
  "country": "Austria"
}
```

PUT body (replace `1` with the ID returned by POST):

```json
{
  "user_id": 1,
  "name": "Lab Five Updated",
  "email": "updated@example.com",
  "phone": "0020000000",
  "address": "10 Test Street",
  "country": "Lebanon"
}
```

## Postman and verification

The **Flask user app** collection contains all five requests. The **Local Flask** environment defines `base_url` as `http://localhost:5000`; requests use `{{base_url}}` followed by the route.

The database schema and all five endpoints were tested locally through a complete add, read, update, read, delete, and deletion-check sequence. CORS was also checked.

Successful response examples in Postman are still pending because the Postman Desktop Agent was disconnected. To finish, start the agent and Flask server, send POST, both GET requests, PUT, and DELETE, and save each successful response as an example. Confirm the updated user with GET before deleting it, then confirm deletion with GET afterward.

## Git workflow and screenshots

Database operations were committed first on `main`. The REST API was implemented on `rest-api`, then merged into `main`. Both branches are available in this repository.

The [outputs folder](outputs/) contains screenshots of the repository, commit history, Postman environment, and request setup. These are setup screenshots; successful Postman response screenshots are still pending.
