# physics3.json File Format Specifications

## Json Schema

Refer [/Schemas/physics3.schema.json](/Schemas/physics3.schema.json).

---

## Description

Make physics3.json http://docs.live2d.com/cubism-editor-manual/physical-operation-setting/

Use physics3.json http://docs.live2d.com/cubism-sdk-manual/physics/

---

## Json Example

```json
{
  "Version": 3,
  "Meta": {
    "PhysicsSettingCount": 2,
    "TotalInputCount": 3,
    "TotalOutputCount": 4,
    "VertexCount": 5,
    "EffectiveForces": {
      "Gravity": {
        "X": 0,
        "Y": 1
      },
      "Wind": {
        "X": 0,
        "Y": 0
      }
    },
    "PhysicsDictionary": [
      {
        "Id": "PhysicsSetting1",
        "Name": "髪揺れ　左"
      },
      {
        "Id": "PhysicsSetting2",
        "Name": "髪揺れ　右"
      }
    ]
  },
  "PhysicsSettings": [
    {
      "Id": "PhysicsSetting1",
      "Input": [
        {
          "Source": {
            "Target": "Parameter",
            "Id": "ParamAngleX"
          },
          "Weight": 50,
          "Type": "X",
          "Reflect": false
        },
        {
          "Source": {
            "Target": "Parameter",
            "Id": "ParamBodyAngleX"
          },
          "Weight": 50,
          "Type": "X",
          "Reflect": false
        }
      ],
      "Output": [
        {
          "Destination": {
            "Target": "Parameter",
            "Id": "ParamHairFront"
          },
          "VertexIndex": 2,
          "Scale": 1,
          "Weight": 100,
          "Type": "X",
          "Reflect": false
        },
        {
          "Destination": {
            "Target": "Parameter",
            "Id": "ParamHairSide"
          },
          "VertexIndex": 2,
          "Scale": 1,
          "Weight": 100,
          "Type": "X",
          "Reflect": false
        },
        {
          "Destination": {
            "Target": "Parameter",
            "Id": "ParamHairBack"
          },
          "VertexIndex": 2,
          "Scale": 1,
          "Weight": 100,
          "Type": "X",
          "Reflect": false
        }
      ],
      "Vertices": [
        {
          "Position": {
            "X": 0,
            "Y": 0
          },
          "Mobility": 1,
          "Delay": 1,
          "Acceleration": 1,
          "Radius": 0
        },
        {
          "Position": {
            "X": 0,
            "Y": 5
          },
          "Mobility": 0.95,
          "Delay": 1,
          "Acceleration": 1,
          "Radius": 5
        },
        {
          "Position": {
            "X": 0,
            "Y": 5
          },
          "Mobility": 0.95,
          "Delay": 1,
          "Acceleration": 1,
          "Radius": 5
        }
      ],
      "Normalization": {
        "Position": {
          "Minimum": -10,
          "Default": 0,
          "Maximum": 10
        },
        "Angle": {
          "Minimum": -10,
          "Default": 0,
          "Maximum": 10
        }
      }
    },
    {
      "Id": "PhysicsSetting2",
      "Input": [
        {
          "Source": {
            "Target": "Parameter",
            "Id": "ParamAngleX"
          },
          "Weight": 1,
          "Type": "X",
          "Reflect": false
        }
      ],
      "Output": [
        {
          "Destination": {
            "Target": "Parameter",
            "Id": "ParamHairSideup"
          },
          "VertexIndex": 1,
          "Scale": 1,
          "Weight": 100,
          "Type": "Angle",
          "Reflect": false
        }
      ],
      "Vertices": [
        {
          "Position": {
            "X": 0,
            "Y": 0
          },
          "Mobility": 1,
          "Delay": 1,
          "Acceleration": 1,
          "Radius": 0
        },
        {
          "Position": {
            "X": 0,
            "Y": 5
          },
          "Mobility": 0.95,
          "Delay": 1,
          "Acceleration": 1,
          "Radius": 5
        }
      ],
      "Normalization": {
        "Position": {
          "Minimum": -10,
          "Default": 0,
          "Maximum": 10
        },
        "Angle": {
          "Minimum": -10,
          "Default": 0,
          "Maximum": 10
        }
      }
    }
  ]
}
```
