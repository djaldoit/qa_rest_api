CreateUser = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "$ref": "#/definitions/Welcome2",
    "definitions": {
        "Welcome2": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "name": {
                    "type": "string"
                },
                "job": {
                    "type": "string"
                },
                "id": {
                    "type": "string",
                    "format": "integer"
                },
                "createdAt": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "createdAt",
                "id",
                "job",
                "name"
            ],
            "title": "Welcome2"
        }
    }
}
