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
					"description": "重力",
					"$ref": "#/definitions/vector2"
				},
				"Wind": {
					"description": "風（使用していない）",
					"$ref": "#/definitions/vector2"
				}
			},
			"required": ["Gravity", "Wind"]
		},
		"physics dictionary" : {
			"description": "物理演算設定のIDと名前を関連付ける",
			"type": "object",
			"properties": {
				"Id": {
					"description": "物理演算設定のID（モデル毎にユニーク）",
					"type": "string"
				},
				"Name": {
					"description": "物理演算設定の名前（グループ名）",
					"type": "string"
				}
				"required": ["Id", "Name"]
			}
		},
		"normalization value": {
			"description": "正規化処理で利用する値を格納",
			"type": "object",
			"properties": {
				"Minimum": {
					"description": "正規化の最小値",
					"type": "number"
				},
				"Default": {
					"description": "正規化範囲の中心",
					"type": "number"
				}
				"Maximum": {
					"description": "正規化の最大値",
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
			"description": "入力",
			"type": "object",
			"properties": {
				"Source": {
					"description": "Target parameter.",
					"$ref": "#/definitions/parameter"
				},
				"Weight": {
					"description": "影響度 種別毎の比率（0～100%）",
					"type": "number"
				},
				"Type": {
					"description": "種別 X or Angle",
					"type": "string"
				},
				"Reflect": {
					"description": "反転",
					"type": "boolean"
				},
				"required": ["Source", "Weight", "Type", "Reflect"]
			}
		},
		"output": {
			"description": "出力",
			"type": "object",
			"properties": {
				"Destination": {
					"description": "Target parameter.",
					"$ref": "#/definitions/parameter"
				},
				"VertexIndex": {
					"description": "参照先の振り子（Vertex）の番号（0 origin）",
					"type": "number"
				},
				"Scale": {
					"description": "倍率",
					"type": "number"
				},
				"Weight": {
					"description": "影響度 種別毎の比率（0～100%）",
					"type": "number"
				},
				"Type": {
					"description": "種別 X or Angle (Angle 固定の予定)",
					"type": "string"
				},
				"Reflect": {
					"description": "反転",
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
					"description": "初期位置",
					"$ref": "#/definitions/vector2"
				},
				"Mobility": {
					"description": "揺れやすさ",
					"type": "number"
				},
				"Delay": {
					"description": "反応速度",
					"type": "number"
				},
				"Acceleration": {
					"description": "全体の速度",
					"type": "number"
				},
				"Radius": {
					"description": "長さ",
					"type": "number"
				}
			},
			"required": ["Position", "Mobility", "Delay", "Acceleration", "Radius"]
		}
	},
	"PhysicsSettings": {
		"description": "物理演算設定",
		"type": "object",
		"properties": {
			"Id": {
				"description": "物理演算設定のID（モデル毎にユニーク）",
				"type": "string"
			},
			"Input": {
				"description": "入力",
				"type": "array",
				"items": {
					"description": "入力配列",
					"$ref": "#/definitions/input"
				}
			},
			"Output": {
				"description": "出力",
				"type": "array",
				"items": {
					"description": "出力配列",
					"$ref": "#/definitions/output"
				}
			},
			"Vertices": {
				"description": "振り子の配列",
				"type": "array",
				"items": {
					"$ref": "#/definitions/vertex"
				}
			},
			"Normalization": {
				"description": "入力値（input）の正規化処理で使用するパラメータ",
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
					"description": "重力、風等の設定値",
					"$ref": "#/definitions/effective force"
				},
				"PhysicsDictionary": {
					"description": "物理演算設定IDと名前の一覧",
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

* Cubism Editor 3.0.10（2017/08/17 リリース予定） で対応予定

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
