# # B The Cause Village Stakeholder API

## Welcome to the Village Stakeholder API Docs

## Base Url
https://mypersonalvillage.com/

## Some information about the API
Frontend
    - **Make sure to include the session tokens when using sending API calls**

Basic Terminology
    - Post -> used to send data to the API, think of User Registration, also the backend team needs to check for duplications since it can create duplicates.
    - Get -> used to fetch data from the API, think of getting a User profile.
    - Put -> used to update records in an existing source, think of updating user profile.
    - Patch -> Similar to put but only updates a part of the record, think of updating the user profile but only with one part.
    - Delete -> Removes a record completely, self explanatory. 

## User Registration
Post /village/vl/register HTTP1.1

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

## Signing In
POST /village/v1/login HTTP1.1
Content application.JSON

```json
{
    "identifier": "bruh@bruh.com", // can be username or email
    "password": "password"
}
```
```json
201 (Success) Response
{
    "user_id":4356557756,
    "message": "Login successful"
}
```

Errors:
```json
400 (Bad request)
{
    "error": "Missing username or password"
}
```

401 (Unauthorized)
```json
{
    "error": "Session cookie invalid
}
```

## Signing Out
Post /village/v1/signout HTTP1.1
Content application.json

```json
Cookie: sessionid=COOKIE_STORED_IN_BROWSER
```

```json
200 (Success)
{
    "message": "Logged out successfully"
}
```

```json
401 (Unauthorized)
{
    "error": "Session cookie invalid logging user out"
}
```

## User Profile
Get /village/v1/getprofile
Content application.json

```json
Cookie: sessionid=COOKIE_STORED_IN_BROWSER
```

```json
200 (Success)
{
    "user_id": "12345567",
    "username": "bruhbruh",
    "email": "bruh@bruh.com",
    "profile_setting": {
        "profile_image": "https://cdn.example.com/images/bruh.jpg",
        "description": "Hi my name is bruh"
    }
}
```

## Updating User Profile
Put /village/v1/updateprofile
Content application.json

```json
Cookie: sessionid=COOKIE_STORED_IN_BROWSER
{
    "username": "bruh_updated",
    "email": "bruh@bruh.com",
    "profile_settings": {
        "profile_image": "https://cdn.example.com/images/bruh.jpg",
        "description": "Hi my name is bruh"
    }
}
```

```
200 (Success)
{
    "message": "Profile updated successfully"
}
```

## Delete Profile
Delete /village/v1/{random large string insert here}/delete_profile
```json
Cookie: sessionid=COOKIE_STORED_IN_BROWSER
```

```json
200 (Success) {
  "message": "Account deleted successfully"
}
```

```json
400 (Bad response) {
    "error": "Message not completed"
}
```
