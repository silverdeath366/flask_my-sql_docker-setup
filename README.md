# Flask + MySQL Dockerized App

A simple, ready-to-run Flask app that connects to a MySQL database using Docker Compose. Ideal for showcasing DevOps fundamentals, containerized development, and database integration.

---

##  What’s Inside

-  Flask API with basic `/users` route
-  MySQL with pre-loaded data
-  Dockerized setup using `docker-compose`
-  Clean `.env` integration for configuration
-  Persistent volume for MySQL data
-  One-command startup: `docker-compose up`

---

## uick Start

1. **Clone the repo**

```bash
git clone https://github.com/silverdeath366/flask_my-sql_docker-setup.git
cd flask_my-sql_docker-setup
```

2. **Set up environment variables**

No changes needed — it already works out of the box with default `.env` values.

3. **Build and run containers**

```bash
docker-compose up --build
```

4. **Test it**

Navigate to:

```
http://localhost:5000/users
```

You should see:

```json
[
  {
    "id": 1,
    "name": "yakov",
    "email": "yakov$@walla.com"
  },
  {
    "id": 2,
    "name": "moshe",
    "email": "moshe*@yahoo.com"
  }
]
```

---

##Project Structure

```
.
├── app/
│   ├── main.py
│   └── requirements.txt
├── db/
│   └── db.sql
├── Dockerfile
├── docker-compose.yml
└── .env
```
