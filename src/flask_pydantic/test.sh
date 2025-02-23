# request 200
curl -X POST http://localhost:8888 -H "Content-Type: application/json" -d '{"id": 1, "name": "Taro"}'

# bad request 400
curl -X POST http://localhost:8888 -H "Content-Type: application/json" -d '{"id": 1, "name": "22072727651", "age": 30}'
# {
#   "errors": "Value error, ame is too long, it must be 255 characters or less"
# }