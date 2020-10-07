# pose3.json File Format Specifications

## Json Schema

Refer [/Schemas/pose3.schema.json](/Schemas/pose3.schema.json).

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
