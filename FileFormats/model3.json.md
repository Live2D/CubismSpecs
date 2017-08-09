# model3.json File Format Specifications

## Json Schema

```json
{
  "$schema": "http://json-schema.org/schema#",
  "title": "Cubism model.3json File Format (Draft)",
  "type": "object",
  "definitions": {
    "group": {
      "description": "Group entry.",
      "type": "object",
      "properties": {
        "Target": {
          "description": "Target of group."
        },
        "Name": {
          "description": "Unique name of group.",
          "type": "string"
        },
        "Ids": {
          "description": "IDs for mapping to target.",
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      },
      "required": ["Target", "Name", "Ids"]
    }
   },
  "properties": {
    "Version": {
      "description": "Json file format version.",
      "type": "number"
    },
    "FileReferences":  {
      "description": "Relative paths from the model3.json to other files.",
      "type": "object",
      "properties": {
        "Moc": {
          "description": "Relative path to the moc3 file.",
          "type": "string"
        },
        "Textures": {
          "description": "Relative paths to the textures.",
          "type": "array",
          "items": {
            "type": "string"
          }
        },
        "Physics": {
          "description": "[Optional] Relative path to the physics3.json file.",
          "type": "string"
        }
      },
      "required": ["Moc", "Textures"]
    },
    "Groups": {
      "description": "[Optional] groups.",
      "type": "array",
      "items": {
        "$ref": "#/definitions/group"
      }
    }
  },
  "required": ["Version", "FileReferences"]
}
```

---

## Description

### Groups

#### Group Targets

One of the following:

| Target | Description |
| - | - |
| "Parameter" | Group targets parameter. The group IDs then are parameter IDs. |

##### Parameter Target Names

One of the following:

| Id | Description |
| - | - |
| "EyeBlink" | Eye blink parameters group. |
| "LipSync" | Mouth opening parameters group. |

---

## Json Example

```json
{
  "Version": 3,
  "FileReferences": {
    "Moc": "Sample.moc3",
    "Textures": [
      "Sample.png"
    ],
    "Physics": "Sample.physics3.json"
  },
  "Groups": [
    {
      "Target": "Parameter",
      "Name": "EyeBlink",
      "Ids": [
        "EyeLOpen",
        "EyeROpen"
      ]
    }
  ]
}
```