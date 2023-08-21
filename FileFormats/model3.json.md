# model3.json File Format Specifications

## Json Schema

```json
{
  "$schema": "http://json-schema.org/schema#",
  "title": "Cubism model.3json File Format",
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
      "required": ["Target", "Name", "Ids"],
      "additionalProperties": false
    },
    "hitareas": {
      "description": "Collision detection.",
      "type": "object",
      "properties": {
        "Name": {
          "description": "Unique name of group.",
          "type": "string"
        },
        "Id": {
          "description": "IDs for mapping to target.",
          "type": "string"
        }
      },
      "required": ["Name", "Id"],
      "additionalProperties": false
    },
    "motion": {
      "description": "Motion.",
      "type": "object",
      "properties": {
        "File": {
          "description": "File name.",
          "type": "string"
        },
        "FadeOutTime": {
          "description": "[Optional] Time of the Fade-out for motion easing in seconds.",
          "type": "number"
        },
        "FadeInTime": {
          "description": "[Optional] Time of the Fade-In for motion easing in seconds..",
          "type": "number"
        },
        "Sound": {
          "description": "[Optional] Audio files playback with motion.",
          "type": "string"
        },
        "MotionSync": {
          "description": "[Optional] Name of motion-sync setting.",
          "type": "string"
        }
      },
      "required": ["File"],
      "additionalProperties": false
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
        },
        "UserData": {
          "description": "[Optional] Relative path to the userdata3.json file.",
          "type": "string"
        },
        "Pose": {
          "description": "[Optional] Relative path to the pose3.json file.",
          "type": "string"
        },
        "DisplayInfo": {
          "description": "[Optional] Relative path to the cdi3.json file.",
          "type": "string"
        },
        "MotionSync": {
          "description": "[Optional] Relative path to the motionsync3.json file.",
          "type": "string"
        },
        "Expressions": {
          "description": "[Optional] Relative path to the exp3.json file.",
          "type": "array",
          "items":{
            "type":"object",
            "properties":
            {
              "Name":{"type":"string"},
              "File":{"type":"string"}
            },
            "required": ["Name", "File"],
            "additionalProperties": false
          }
        },
        "Motions": {
          "description": "[Optional] Relative path to the motion3.json file.",
          "type": "object",
          "patternProperties":
          {
            ".*":
            {
              "type": "array",
              "items":{
                "$ref": "#/definitions/motion"
              }
            }
          },
          "additionalProperties": false
        }
      },
      "required": ["Moc", "Textures"],
      "additionalProperties": false
    },
    "Groups": {
      "description": "[Optional] groups.",
      "type": "array",
      "items": {
        "$ref": "#/definitions/group"
      }
    },
    "HitAreas": {
      "description": "[Optional]Collision detection",
      "type": "array",
      "items": {
        "$ref": "#/definitions/hitareas"
      }
    },
    "Layout": {
      "description": "[Optional]Layout",
      "type": "object",
      "properties":{
        "width" : { "type": "number" },
        "height" : { "type": "number" },
        "x" : { "type": "number" },
        "y" : { "type": "number" },
        "center_x" : { "type": "number" },
        "center_y" : { "type": "number" },
        "top" : { "type": "number" },
        "bottom" : { "type": "number" },
        "left" : { "type": "number" },
        "right" : { "type": "number" }
      },
      "additionalProperties": false
    }
  },
  "required": ["Version", "FileReferences"],
  "additionalProperties": false
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
    "Physics": "Sample.physics3.json",
    "UserData": "Sample.userdata3.json"
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
