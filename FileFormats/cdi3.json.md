# cdi3.json File Format Specifications

## Json Schema

Refer [/Schemas/cdi3.schema.json](/Schemas/cdi3.schema.json).

---

## Description

Each parameter or parameter group has a groupId identifier. The corresponding group is defined in ParameterGroups. Empty string means it doesn't belong to any groups. The elements in the list are sorted. Therefore, if a parameter AngleX has a groupId ParamGroupHead, you should create a parameter group called Head then add the parameter AngleX in to it. The next paramter AngleY has a groupId with empty string will be placed right after the parameter group Head.

---

## Json Example

```json
{
  "Version": 3,
  "Parameters": [
    {
      "Id": "ParamAngleX",
      "GroupId": "ParamGroupHead",
      "Name": "Angle X"
    },
    {
      "Id": "ParamAngleY",
      "GroupId": "ParamGroupHead",
      "Name": "Angle Y"
    },
    {
      "Id": "ParamEyeBall",
      "GroupId": "ParameterGroupEye",
      "Name": "EyeBall"
    },
    {
      "Id": "ParamHair",
      "GroupId": "ParamGroupHead",
      "Name": "Hair"
    },
    {
      "Id": "ParamBody",
      "GroupId": "",
      "Name": "Body"
    }
  ],
  "ParameterGroups": [
    {
      "Id": "ParamGroupHead",
      "GroupId": "",
      "Name": "Head"
    },
    {
      "Id": "ParameterGroupEye",
      "GroupId": "ParamGroupHead",
      "Name": "Eye"
    }
  ],
  "Parts": [
    {
      "Id": "PartArmR",
      "Name": "Right Arm"
    },
    {
      "Id": "PartMouth",
      "Name": "Mouth"
    }
  ]
}
```
