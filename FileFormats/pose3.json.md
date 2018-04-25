# pose3.json File Format Specifications

## Json Schema

```json
{
    "$schema": "http://json-schema.org/schema#",
    "title": "Cubism pose3.json File Format",
    "type":"object",
    "properties": {
        "Type":{
          "description":"",
          "type":"string",
          "enum": ["Live2D Pose"]
        },
        "FadeInTime": {
            "description":"Time of the Fade-In for easing in seconds.",
            "type":"number"
        },
        "Groups": {
            "description": "List of the switching control groups.",
            "type":"array",
            "items":{
                "description": "Switching control group.",
                "type":"array",
                "items": {
                    "description": "Switching control node.",
                    "type": "object",
                    "properties": {
                        "Id":{
                            "description": "Main switching Part ID.",
                            "type":"string"
                        },  
                        "Link":{
                            "description": "List of the linked switching Part IDs.",
                            "type":"array", 
                            "items":{
                               "type":"string"
                            } 
                        }
                    },
                    "required": [ "Id" ],
                    "additionalProperties": false
                }
            }
        }
    },
    "required": [ "Type", "Groups"],
    "additionalProperties": false
}
```

---

## Description

### Group

Only one node is displayed in the group.

### Switching controll node

Id：Data is Part ID.

   Manipulate the opacity of the part while referring to non-existent parameters operated from motion.

Link:A list of parts IDs that manipulates the opacity of parts in cooperation with Id.

---

## Json Example

```json
{
  "Type": "Live2D Pose",
  "Groups": [
    [
      {
        "Id": "Part01ArmLB001",
        "Link": []
      },
      {
        "Id": "Part01ArmRA001",
        "Link": []
      }
    ],
    [
      {
        "Id": "Part01ArmRB001",
        "Link": []
      },
      {
        "Id": "Part01ArmLA001",
        "Link": []
      }
    ]
  ]
}
```
