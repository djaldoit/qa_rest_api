GetUser = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "$ref": "#/definitions/Welcome9",
    "definitions": {
        "Welcome9": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "data": {
                    "$ref": "#/definitions/Data"
                },
                "support": {
                    "$ref": "#/definitions/Support"
                }
            },
            "required": [
                "data",
                "support"
            ],
            "title": "Welcome9"
        },
        "Data": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "id": {
                    "type": "integer"
                },
                "email": {
                    "type": "string"
                },
                "first_name": {
                    "type": "string"
                },
                "last_name": {
                    "type": "string"
                },
                "avatar": {
                    "type": "string",
                    "format": "uri",
                    "qt-uri-protocols": [
                        "https"
                    ],
                    "qt-uri-extensions": [
                        ".jpg"
                    ]
                }
            },
            "required": [
                "avatar",
                "email",
                "first_name",
                "id",
                "last_name"
            ],
            "title": "Data"
        },
        "Support": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "url": {
                    "type": "string",
                    "format": "uri",
                    "qt-uri-protocols": [
                        "https"
                    ]
                },
                "text": {
                    "type": "string"
                }
            },
            "required": [
                "text",
                "url"
            ],
            "title": "Support"
        }
    }
}
