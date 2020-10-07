# model3.json File Format Specifications

## Json Schema

Refer [/Schemas/model3.schema.json](/Schemas/model3.schema.json).

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
