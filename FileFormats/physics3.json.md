# physics3.json File Format Specifications

## Json Schema

```json
{
	"$schema": "http://json-schema.org/schema#",
	"title": "Cubism physics3.json File Format",
	"type": "object",
	"definitions": {
		"vector2": {
			"description": "Two-dimensional vector.",
			"type": "object",
			"properties": {
				"X": {
					"type": "number"
				},
				"Y": {
					"type": "number"
				}
			},
			"required": ["X", "Y"],
      		"additionalProperties": false
		},
		"effective force": {
			"description": "Settings of external forces",
			"type": "object",
			"properties": {
				"Gravity": {
					"description": "Gravity.",
					"$ref": "#/definitions/vector2"
				},
				"Wind": {
					"description": "Wind.",
					"$ref": "#/definitions/vector2"
				}
			},
			"required": ["Gravity", "Wind"],
      		"additionalProperties": false
		},
		"physics dictionary" : {
			"description": "Related to the name and ID of Physics settings.",
			"type": "object",
			"properties": {
				"Id": {
					"description": "Identifier for Physics settings(each model is different).",
					"type": "string"
				},
				"Name": {
					"description": "Name of Physics settings(group name).",
					"type": "string"
				}
			},
			"required": ["Id", "Name"],
      		"additionalProperties": false
		},
		"normalization value": {
			"description": "Normalized values.",
			"type": "object",
			"properties": {
				"Minimum": {
					"description": "Normalized minimum.",
					"type": "number"
				},
				"Default": {
					"description": "Center of the range of normalization.",
					"type": "number"
				},
				"Maximum": {
					"description": "Normalized maximum.",
					"type": "number"
				}
			},
			"required": ["Minimum", "Default", "Maximum"],
      		"additionalProperties": false
		},
		"parameter" : {
			"description": "Targeted parameter of model.",
			"type": "object",
			"properties": {
				"Target": {
					"description": "Target type.",
					"type": "string"
				},
				"Id": {
					"description": "Parameter ID.",
					"type": "string"
				}
			},
			"required": ["Target", "Id"],
      		"additionalProperties": false
		},
		"input": {
			"description": "Input.",
			"type": "object",
			"properties": {
				"Source": {
					"description": "Targeted parameter.",
					"$ref": "#/definitions/parameter"
				},
				"Weight": {
					"description": "Effectiveness:propotion of each type（0～100%）.",
					"type": "number"
				},
				"Type": {
					"description": "Type X or Angle.",
					"type": "string"
				},
				"Reflect": {
					"description": "Reflect.",
					"type": "boolean"
				}
			},
			"required": ["Source", "Weight", "Type", "Reflect"],
      		"additionalProperties": false
		},
		"output": {
			"description": "Output.",
			"type": "object",
			"properties": {
				"Destination": {
					"description": "Targeted parameter.",
					"$ref": "#/definitions/parameter"
				},
				"VertexIndex": {
					"description": "Number（0 origin） of parent pendulum（Vertex）.",
					"type": "number"
				},
				"Scale": {
					"description": "Scale",
					"type": "number"
				},
				"Weight": {
					"description": "Effectiveness:propotion of each type（0～100%）.",
					"type": "number"
				},
				"Type": {
					"description": "Type X or Angle (Angle might be fixed)",
					"type": "string"
				},
				"Reflect": {
					"description": "Reflect",
					"type": "boolean"
				}
			},
			"required": ["Destination", "VertexIndex", "Scale", "Weight", "Type", "Reflect"],
      		"additionalProperties": false
		},
		"vertex": {
			"description": "Single vertex.",
			"type": "object",
			"properties": {
				"Position": {
					"description": "Default position.",
					"$ref": "#/definitions/vector2"
				},
				"Mobility": {
					"description": "Shaking influence.",
					"type": "number"
				},
				"Delay": {
					"description": "Reaction time.",
					"type": "number"
				},
				"Acceleration": {
					"description": "Overall acceleration.",
					"type": "number"
				},
				"Radius": {
					"description": "Radius of pendulum.",
					"type": "number"
				}
			},
			"required": ["Position", "Mobility", "Delay", "Acceleration", "Radius"],
      		"additionalProperties": false
		}
	},
	"properties": {
		"PhysicsSettings": {
			"description": "Physics Settings.",
			"type": "array",
			"itmes":{
				"description": "Physics Settings",
				"type": "object",
				"properties": {
					"Id": {
						"description": "Identifier for Physics settings(each model is different).",
						"type": "string"
					},
					"Input": {
						"description": "Input.",
						"type": "array",
						"items": {
							"description": "Array of the input",
							"$ref": "#/definitions/input"
						}
					},
					"Output": {
						"description": "Output.",
						"type": "array",
						"items": {
							"description": "Array of the output",
							"$ref": "#/definitions/output"
						}
					},
					"Vertices": {
						"description": "Array of the pendulums",
						"type": "array",
						"items": {
							"$ref": "#/definitions/vertex"
						}
					},
					"Normalization": {
						"description": "Parameter(input value normalized).",
						"type": "object",
						"properties": {
							"Position": {
								"description": "Normalization value of position.",
								"$ref": "#/definitions/normalization value"
							},
							"Angle": {
								"description": "Normalization value of angle.",
								"$ref": "#/definitions/normalization value"
							}
						},
						"required": ["Position", "Angle"],
		      			"additionalProperties": false
					}
				},
				"required": ["Id", "Input", "Vertices", "Output", "Normalization"],
		      	"additionalProperties": false
	      	}
		},
		"Version": {
			"description": "Json file format version.",
			"type": "number"
		},
		"Meta": {
			"description": "Additional data describing the physics.",
			"type": "object",
			"properties": {
				"PhysicsSettingCount": {
					"description": "Number of physics settings.",
					"type": "number"
				},
				"TotalInputCount": {
					"description": "Total number of input parameters.",
					"type": "number"
				},
				"TotalOutputCount": {
					"description": "Total number of output parameters.",
					"type": "number"
				},
				"VertexCount": {
					"description": "Total number of vertices.",
					"type": "number"
				},
				"EffectiveForces": {
					"description": "Settings of gravity and wind.",
					"$ref": "#/definitions/effective force"
				},
				"PhysicsDictionary": {
					"description": "List of names and identifiers of Physics setting.",
					"type": "array",
					"items": {
						"description": "",
						"$ref": "#/definitions/physics dictionary"
					}
				}
			},
			"required": ["PhysicsSettingCount", "TotalInputCount", "TotalOutputCount", "VertexCount", "EffectiveForces", "PhysicsDictionary"],
      		"additionalProperties": false
		}
	},
	"required": ["Version", "Meta", "PhysicsSettings"],
    "additionalProperties": false
}
```

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
