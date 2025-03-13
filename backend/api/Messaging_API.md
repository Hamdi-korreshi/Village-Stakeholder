## Send Message 
Post

```json
{
    "email": "bruh@bruh.com",
    "username": "thebruhest",
    "password": "123456789"
}
```

```json
201 (Success) Response
{
    "Message": "User registered successfully",
    "user_id": 123
}
```

Errors:
```json
400 (Bad request)
{
    "error": "Missing username or password"
}
```

```json
401 (Unauthorized)
{
    "error": "Session cookie invalid"
}
```