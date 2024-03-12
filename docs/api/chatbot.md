# Create conversation

## Description

Creates a new conversation with user

## Definition

`POST /chatbot/conversations/`

## Content Types

- `application/json`

## Arguments

| Name    | Type   | Request | Default Value | Description  |
|---------|--------|:--------|---------------|--------------|
| message | String | Body    |               | User's query |

## Response

### Successful response

```json
//HTTP 201 Created
//Allow: GET, POST, HEAD, OPTIONS
//Content-Type: application/json
//Vary: Accept

{
    "url": "http://127.0.0.1:8000/app/chatbot/conversations/9d9e74fc-4330-4ec7-b546-8892a47cf644",
    "messages": [
        {
            "role": "user",
            "content": "Hi!"
        },
        {
            "role": "assistant",
            "content": "Hello! How can I assist you today?"
        }
    ],
    "user": "http://127.0.0.1:8000/app/users/1/"
}
```

### Unsuccessful response

```json
//(400 Bad Request)
```

## Example

```shell
curl -X POST --location "http://localhost:8000/app/chatbot/conversations/" \
-H "Content-Type: application/json" \
-H "Cookie: auth=<access_token> \
-d "{
\"message\": \"Could you do python coding for me?\"
}"

```

# Continue conversation

## Description

Continues created conversation

## Description

Creates a new conversation with user

## Definition

`PATCH /chatbot/conversations/<conversation_id>`

## Content Types

- `application/json`

## Arguments

| Name    | Type   | Request | Default Value | Description  |
|---------|--------|:--------|---------------|--------------|
| message | String | Body    |               | User's query |


## Notes

Responses and general semantics is the same as create conversation