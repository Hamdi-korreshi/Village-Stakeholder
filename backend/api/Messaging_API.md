## Base Url
https://mypersonalvillage.com/

## Messenger

POST /village/vl/messages/{recipient}

Send a direct message to a user
**Request body**
```json
{
    "sender_id" : 123,
    "receiver_id" : 456,
    "message" : "Hey, what's up?"
}
```

**Response**
```json
{
    "message_id": 311,
    "sender_id": 123,
    "reciever_id": 456,
    "message": "Hey, what's up?",
    "attachment_url" : "https:example.com/image.png",
    "timestamp" : "2025-01-10T14:30:00Z"
}
```
---

GET /village/vl/messages/{recipient}

Retrieving messages between two users
**Response**
```json
[
    {
        "message_id": 311,
        "sender_id": 123,
        "reciever_id": 456,
        "message": "Hey, what's up?",
        "attachment_url" : "https:example.com/wave.png",
        "timestamp" : "2025-01-10T10:30:00Z"
    }
    {
        "message_id": 312,
        "sender_id": 456,
        "reciever_id": 123,
        "message": "Nothing much, hbu?",
        "attachment_url" : "",
        "timestamp" : "2025-01-10T10:30:30Z"
    }
]
```

**Error**
```json
404 (Not Found)
{
    "error" : "messages not found"
}
```
---

PATCH /village/vl/messages/{recipient}/{message_id}

Edit a specified message
**Request Body**
```json
{
    "message" : ""
}
```
**Response**
```json 

{
    "message" : "message successfully changed"
}
```

**Errors**
```json
401 (Unauthorized) //subject to change 
{
    "error": "Cant edit others' message" 
}
```
---

DELETE /village/vl/messages/{recipient}/{message_id}

Delete a specific message
**Response**
```json
{
    "message" : "message successfully deleted"
}
```

**Error**
```json
401 (Unauthorized) //subject to change 
{
    "error": "Cant delete others' message" 
}
```

