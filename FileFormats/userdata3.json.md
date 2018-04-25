# userdata3.json File Format Specifications

## Json Schema

```json
{
  "$schema": "http://json-schema.org/schema#",
  "title": "Cubism userdata3.json File Format",
  "type": "object",
  "definitions": {
    "userData": {
      "description": "User data.",
      "type": "object",
      "properties": {
        "Target": {
          "description": "Target type.",
          "type": "string"
        },
        "Id": {
          "description": "Identifier for mapping to target.",
          "type": "string"
        },
        "Value": {
          "description": "Content of user data.",
          "type": "string"
        }
      },
      "required": ["Target", "Id", "Value"],
      "additionalProperties": false
    }
   },
  "properties": {
    "Version": {
      "description": "Json file format version.",
      "type": "number"
    },
    "Meta": {
      "description": "Additional data describing the user data.",
      "type": "object",
      "properties": {
        "UserDataCount": {
          "description": "The total number of UserData.",
          "type": "number"
        },
        "TotalUserDataSize": {
          "description": "The total size of UserData in bytes.",
          "type": "number"
        }
      },
      "required": ["UserDataCount", "TotalUserDataSize"],
      "additionalProperties": false
    },
    "UserData": {
      "description": "User data.",
      "type": "array",
      "items": {
        "$ref": "#/definitions/userData"
      }
    }    
  },
  "required": ["Version", "Meta", "UserData"],
  "additionalProperties": false
}
```

---

## Description

### UserData

#### UserData Target Identifiers

One of the following:

| Target | Description |
| - | - |
| "ArtMesh" | User data targets a ArtMesh. The user data ID then is the ArtMesh ID. |

---

## Json Example

```json
{
	"Version": 3,
	"Meta": {
		"UserDataCount": 3,
		"TotalUserDataSize": 12
	},
	"UserData": [
		{
			"Target": "ArtMesh",
			"Id": "ArtMeshArm01",
			"Value": "hoge"
		},
		{
			"Target": "ArtMesh",
			"Id": "ArtMeshEye01",
			"Value": "fuga"
		},
		{
			"Target": "ArtMesh",
			"Id": "ArtMeshEye02",
			"Value": "piyo"
		}
	]
}
```
