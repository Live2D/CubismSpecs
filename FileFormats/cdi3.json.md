# cdi3.json File Format Specifications

## Json Schema

```json
{
  "$schema": "http://json-schema.org/schema#",
  "title": "Cubism cdi3.json File Format",
  "type": "object",
  "definitions": {
    "Parameter": {
      "description": "Information to correlate Id, Group, and Display-Name in the parameter.",
      "type": "object",
      "properties": {
        "Id": {
          "description": "Identifier for the parameter.",
          "type": "string"
        },
        "GroupId": {
          "description": "Identifier for the parent group of the parameter.",
          "type": "string"
        },
        "Name": {
          "description": "Name of the parameter.",
          "type": "string"
        }
      },
      "required": ["Id", "GroupId", "Name"],
      "additionalProperties": false
    },
    "ParameterGroup": {
      "description": "Information to correlate Id, Group, and Display-Name in the ParameterGroup.",
      "type": "object",
      "properties": {
        "Id": {
          "description": "Identifier for the parameter group.",
          "type": "string"
        },
        "GroupId": {
          "description": "Identifier for the parent group of the parameter group.",
          "type": "string"
        },
        "Name": {
          "description": "Name of the parameter group.",
          "type": "string"
        }
      },
      "required": ["Id", "GroupId", "Name"],
      "additionalProperties": false
    },
    "Part": {
      "description": "Information to correlate Id and Display-Name in the Part.",
      "type": "object",
      "properties": {
        "Id": {
          "description": "Identifier for the part.",
          "type": "string"
        },
        "Name": {
          "description": "Name of the part.",
          "type": "string"
        }
      },
      "required": ["Id", "Name"],
      "additionalProperties": false
    }
  },
  "properties": {
    "Version": {
      "description": "Json file format version.",
      "type": "number"
    },
    "Parameters": {
      "description": "All Parameters.",
      "type": "array",
      "items": {            
        "description": "Array of the Paramter",
        "$ref": "#/definitions/Parameter"
      }
    },
    "ParameterGroups": {        
      "description": "All ParameterGroups.",
      "type": "array",
      "items": {            
        "description": "Array of the ParameterGroup",
        "$ref": "#/definitions/ParameterGroup"
      }
    },
    "Parts": {            
      "description": "All Parts.",
      "type": "array",
      "items": {            
        "description": "Array of the Part",
        "$ref": "#/definitions/Part"
      }
    },
    "CombinedParameters": {        
      "description": "[Optional] Parameter combination informations.",
      "type": "array",
      "items": {
        "description": "Array of the Combine.",

        "type": "array",
        "items": {
            "description": "Array of the ParameterId",
            "type": "string"
        },
        "minItems": 2,
        "maxItems": 2
      }
    }
  },
  "required": ["Version", "ParameterGroups", "Parts"],
  "additionalProperties": false
}
```

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
	],
	"CombinedParameters": [
		[
			"ParamAngleX",
			"ParamAngleY"
		]
	]
}
```
