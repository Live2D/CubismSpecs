# userdata3.json File Format Specifications

## Json Schema

Refer [/Schemas/userdata3.schema.json](/Schemas/userdata3.schema.json).

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
