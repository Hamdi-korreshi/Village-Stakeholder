# B The Cause Village Stakeholder API

## Welcome to the Village Stakeholder API Docs

## Base Url
https://mypersonalvillage.com/

## Signing In
POST /village/v1/signin HTTP1.1
Content application.JSON

{
    "identifier": "bruh@bruh.com", // can be username or email
    "password": "password"
}

Response
{
    "user_id":4356557756,
    "message": "Login successful"
}

Errors:
400 (Bad request)
{
    "error": "Missing username or password"
}

401 (Unauthorized)
{
    "error": "Invalid creds"
}


## Messaging


