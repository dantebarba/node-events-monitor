# Node Events Monitor

Monitor events from a list of nodes using a webhook.

## Usage

```http
POST https://your-ip.com/action

Authentication: Bearer $bearer
```

### Body

```json
{ "server" : "node-name", "status": "action_payload" }
```

### Response

```http
HTTP 200 OK

HTTP 400 BAD REQUEST

HTTP 404 NOT FOUND - Unable to find node in node-list

HTTP 401 Unauthenticated - No bearer or invalid bearer
```
