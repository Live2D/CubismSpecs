# physics3.json File Format Specifications

## Json Schema

```json
{
	"$schema": "http://json-schema.org/schema#",
	"title": "Cubism physics3.json File Format (Draft)",
	"type": "object",
	"definitions": {
		"vector2": {
			"description": "2-component vector.",
			"type": "object",
			"properties": {
				"X": {
					"type": "number"
				},
				"Y": {
					"type": "number"
				}
			},
			"required": ["X", "Y"]
		},
		"effective force": {
			"description": "",
			"type": "object",
			"properties": {
				"Gravity": {
					"description": "�d��",
					"$ref": "#/definitions/vector2"
				},
				"Wind": {
					"description": "���i�g�p���Ă��Ȃ��j",
					"$ref": "#/definitions/vector2"
				}
			},
			"required": ["Gravity", "Wind"]
		},
		"physics dictionary" : {
			"description": "�������Z�ݒ��ID�Ɩ��O���֘A�t����",
			"type": "object",
			"properties": {
				"Id": {
					"description": "�������Z�ݒ��ID�i���f�����Ƀ��j�[�N�j",
					"type": "string"
				},
				"Name": {
					"description": "�������Z�ݒ�̖��O�i�O���[�v���j",
					"type": "string"
				}
				"required": ["Id", "Name"]
			}
		},
		"normalization value": {
			"description": "���K�������ŗ��p����l���i�[",
			"type": "object",
			"properties": {
				"Minimum": {
					"description": "���K���̍ŏ��l",
					"type": "number"
				},
				"Default": {
					"description": "���K���͈͂̒��S",
					"type": "number"
				}
				"Maximum": {
					"description": "���K���̍ő�l",
					"type": "number"
				},
				"required": ["Minimum", "Default", "Maximum"]
			}
		},
		"parameter" : {
			"description": "Target parameter of model.",
			"type": "object",
			"properties": {
				"Target": {
					"description": "Target type.",
					"type": "string"
				},
				"Id": {
					"description": "Parameter ID.",
					"type": "string"
				},
				"required": ["Target", "Id"]
			}
		},
		"input": {
			"description": "����",
			"type": "object",
			"properties": {
				"Source": {
					"description": "Target parameter.",
					"$ref": "#/definitions/parameter"
				},
				"Weight": {
					"description": "�e���x ��ʖ��̔䗦�i0�`100%�j",
					"type": "number"
				},
				"Type": {
					"description": "��� X or Angle",
					"type": "string"
				},
				"Reflect": {
					"description": "���]",
					"type": "boolean"
				},
				"required": ["Source", "Weight", "Type", "Reflect"]
			}
		},
		"output": {
			"description": "�o��",
			"type": "object",
			"properties": {
				"Destination": {
					"description": "Target parameter.",
					"$ref": "#/definitions/parameter"
				},
				"VertexIndex": {
					"description": "�Q�Ɛ�̐U��q�iVertex�j�̔ԍ��i0 origin�j",
					"type": "number"
				},
				"Scale": {
					"description": "�{��",
					"type": "number"
				},
				"Weight": {
					"description": "�e���x ��ʖ��̔䗦�i0�`100%�j",
					"type": "number"
				},
				"Type": {
					"description": "��� X or Angle (Angle �Œ�̗\��)",
					"type": "string"
				},
				"Reflect": {
					"description": "���]",
					"type": "boolean"
				},
				"required": ["Destination", "VertexIndex", "Scale", "Weight", "Type", "Reflect"]
			}
		},
		"vertex": {
			"description": "Single vertex.",
			"type": "object",
			"properties": {
				"Position": {
					"description": "�����ʒu",
					"$ref": "#/definitions/vector2"
				},
				"Mobility": {
					"description": "�h��₷��",
					"type": "number"
				},
				"Delay": {
					"description": "�������x",
					"type": "number"
				},
				"Acceleration": {
					"description": "�S�̂̑��x",
					"type": "number"
				},
				"Radius": {
					"description": "����",
					"type": "number"
				}
			},
			"required": ["Position", "Mobility", "Delay", "Acceleration", "Radius"]
		}
	},
	"PhysicsSettings": {
		"description": "�������Z�ݒ�",
		"type": "object",
		"properties": {
			"Id": {
				"description": "�������Z�ݒ��ID�i���f�����Ƀ��j�[�N�j",
				"type": "string"
			},
			"Input": {
				"description": "����",
				"type": "array",
				"items": {
					"description": "���͔z��",
					"$ref": "#/definitions/input"
				}
			},
			"Output": {
				"description": "�o��",
				"type": "array",
				"items": {
					"description": "�o�͔z��",
					"$ref": "#/definitions/output"
				}
			},
			"Vertices": {
				"description": "�U��q�̔z��",
				"type": "array",
				"items": {
					"$ref": "#/definitions/vertex"
				}
			},
			"Normalization": {
				"description": "���͒l�iinput�j�̐��K�������Ŏg�p����p�����[�^",
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
				"required": ["Position", "Angle"]
			}
		},
		"required": ["Id", "Input", "Vertices", "Output", "Normalization"]
	},
	"properties": {
		"Version": {
			"description": "Json file format version.",
			"type": "number"
		},
		"Meta": {
			"description": "Additional data describing physics.",
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
				"TotalVertexCount": {
					"description": "Total number of vertices.",
					"type": "number"
				},
				"EffectiveForces": {
					"description": "�d�́A�����̐ݒ�l",
					"$ref": "#/definitions/effective force"
				},
				"PhysicsDictionary": {
					"description": "�������Z�ݒ�ID�Ɩ��O�̈ꗗ",
					"type": "array",
					"items": {
						"description": "",
						"$ref": "#/definitions/physics dictionary"
					}
				}
			},
			"required": ["PhysicsSettingCount", "TotalInputCount", "TotalOutputCount", "TotalVertexCount", "EffectiveForces", "PhysicsDictionary"]
		}
	},
	"required": ["Version", "Meta", "PhysicsSettings"]
}
```

---

## Description

* Cubism Editor 3.0.10�i2017/08/17 �����[�X�\��j �őΉ��\��

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
				"Name": "���h��@��"
			},
			{
				"Id": "PhysicsSetting2",
				"Name": "���h��@�E"
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
