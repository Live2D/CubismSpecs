# motionsync3 File Format Specifications

## Json Schema

```json
{
  "$schema": "http://json-schema.org/schema#",
  "title": "Cubism motionsync3 File Format",
  "type": "object",
  "definitions": {
    "dictionary" : {
      "description": "Settings name and id template.",
      "type": "object",
        "properties": {
          "Id": {
            "description": "Setting id.",
            "type": "string"
          },
          "Name": {
            "description": "Setting name.",
            "type": "string"
          }
        },
        "required": ["Id", "Name"],
            "additionalProperties": false
    },
    "cubismParameter" : {
      "description": "Parameter about model.",
      "type": "object",
        "properties": {
          "Name": {
            "description": "Parameter name.",
            "type": "string"
          },
          "Id": {
            "description": "Parameter ID.",
            "type": "string"
          },
          "Min": {
            "description": "Parameter minimum value.",
            "type": "number"
          },
          "Max": {
            "description": "Parameter maximum value.",
            "type": "number"
          },
          "Damper": {
            "description": "Damping value.",
            "type": "number"
          },
          "Smooth": {
            "description": "Smoothing Value.",
            "type": "number"
          },
        },
        "required": ["Name", "Id", "Min", "Max", "Damper", "Smooth"],
            "additionalProperties": false
    },
    "audioParameter" : {
      "description": "Parameter about audio analysis library.",
      "type": "object",
        "properties": {
          "Name": {
            "description": "Parameter name.",
            "type": "string"
          },
          "Id": {
            "description": "Parameter ID.",
            "type": "string"
          },
          "Min": {
            "description": "Parameter minimum value.",
            "type": "number"
          },
          "Max": {
            "description": "Parameter maximum value.",
            "type": "number"
          },
          "Scale": {
            "description": "Scale value.",
            "type": "number"
          },
          "Enabled": {
            "description": "Prameter enabled state.",
            "type": "boolean"
          },
        },
        "required": ["Name", "Id", "Min", "Max", "Scale", "Enabled"],
            "additionalProperties": false
    },
    "mappingParameter" : {
      "description": "Mapping parameter for converting audio parameter to cubism parameter.",
      "type": "object",
        "properties": {
          "Id": {
            "description": "Parameter name.",
            "type": "string"
          },
          "Value": {
            "description": "Parameter value.",
            "type": "number"
          }
        },
        "required": ["Id", "Value"],
            "additionalProperties": false
    },
    "mappingTarget" : {
      "description": "Mapping parameter for converting audio parameter to cubism parameter.",
      "type": "object",
        "properties": {
          "Type": {
            "description": "Mapping type.",
            "type": "string"
          },
          "Id": {
            "description": "Audio parameter ID.",
            "type": "string"
          },
          "Targets": {
            "description": "Array about the mappingParameter.",
            "type": "array",
            "items": {
              "description": "Mapping Parameter.",
              "$ref": "#/definitions/mappingParameter"
            }
          }
        },
        "required": ["Type", "Id", "Targets"],
            "additionalProperties": false
    },
  },
  "properties": {
    "Version": {
      "description": "Json file format version.",
      "type": "number"
    },
    "Meta": {
      "description": "Meta.",
      "type": "object",
      "SettingCount": {
        "description": "Number about `Settings`.",
        "type": "number"
      },
      "Dictionary": {
        "description": "Id-Name pairs in `Settings` array.",
        "type": "array",
        "items": {
          "description": "Id and name about setting",
          "$ref": "#/definitions/dictionary"
        }
      }
    },
    "Settings": {
      "description": "Info about motion-sync settings.",
      "type": "array",
      "items": {
        "AnalysisType": {
          "description": "Types about analysis libraries.",
          "type": "string"
        },
        "UseCase": {
          "description": "Types about use case.",
          "type": "string"
        },
        "CubismParameters": {
          "description": "Data about cubism parameters",
          "type": "array",
          "items": {
            "description": "Motion-sync settings about cubism parameter.",
            "$ref": "#/definitions/cubismParameter"
          }
        },
        "AudioParameters": {
          "description": "Data about audio parameters.",
          "type": "array",
          "items": {
            "description": "Motion-sync settings about audio parameter.",
            "$ref": "#/definitions/audioParameter"
          }
        },
        "Mappings": {
          "description": "Connecting audio parameters to cubism parameters.",
          "type": "array",
          "items": {
            "description": "Mapping target info.",
            "$ref": "#/definitions/mappingTarget"
          }
        },
        "PostProcessing": {
          "description": "Post-processing information.",
          "type": "object",
          "properties": {
            "BlendRatio": {
              "description": "Ratio about motion sync blending.",
              "type": "number"
            },
            "Smoothing": {
              "description": "Value about motion sync smoothing.",
              "type": "number"
            },
            "SampleRate": {
              "description": "Settings about motion sync update speed.",
              "type": "number"
            },
          },
          "required": ["BlendRatio", "Smoothing", "SampleRate"],
            "additionalProperties": false
        }
      },
      "required": ["Id", "AnalysisType", "UseCase", "CubismParameters", "AudioParameters", "Mappings", "PostProcessing"],
        "additionalProperties": false
    },
  },
  "required": ["Version", "Meta", "Settings"],
    "additionalProperties": false
}
```

---

## Description


Make motionsync3 https://docs.live2d.com/cubism-editor-manual/motion-sync/

Use motionsync3 https://docs.live2d.com/cubism-sdk-manual/motion-sync-addon/

---

## Json Example

```json
{
  "Version": 1,
  "Meta": {
    "SettingCount": 1,
    "Dictionary": [
      {
        "Id": "MotionSyncSetting1",
        "Name": "プリセット1"
      }
    ]
  },
  "Settings": [
    {
      "Id": "MotionSyncSetting1",
      "AnalysisType": "OVR",
      "UseCase": "Mouth",
      "CubismParameters": [
        {
          "Name": "口 変形",
          "Id": "ParamMouthForm",
          "Min": -1.0,
          "Max": 1.0,
          "Damper": 0.0,
          "Smooth": 25
        },
        {
          "Name": "口　開閉",
          "Id": "ParamMouthOpenY",
          "Min": -1.0,
          "Max": 1.0,
          "Damper": 0.0,
          "Smooth": 25
        },
        {
          "Name": "舌",
          "Id": "ParamTongue",
          "Min": -1.0,
          "Max": 1.0,
          "Damper": 0.0,
          "Smooth": 25
        },
        {
          "Name": "顎",
          "Id": "ParamJaw",
          "Min": -1.0,
          "Max": 1.0,
          "Damper": 0.0,
          "Smooth": 25
        }
      ],
      "AudioParameters": [
        {
          "Name": "sil",
          "Id": "sil",
          "Min": 0.0,
          "Max": 1.0,
          "Scale": 6.9,
          "Enabled": true
        },
        {
          "Name": "PP",
          "Id": "PP",
          "Min": 0.0,
          "Max": 1.0,
          "Scale": 6.9,
          "Enabled": false
        },
        {
          "Name": "FF",
          "Id": "FF",
          "Min": 0.0,
          "Max": 1.0,
          "Scale": 1.0,
          "Enabled": false
        },
        {
          "Name": "TH",
          "Id": "TH",
          "Min": 0.0,
          "Max": 1.0,
          "Scale": 1.0,
          "Enabled": true
        },
        {
          "Name": "DD",
          "Id": "DD",
          "Min": 0.0,
          "Max": 1.0,
          "Scale": 1.0,
          "Enabled": true
        },
        {
          "Name": "kk",
          "Id": "kk",
          "Min": 0.0,
          "Max": 1.0,
          "Scale": 1.0,
          "Enabled": true
        },
        {
          "Name": "CH",
          "Id": "CH",
          "Min": 0.0,
          "Max": 1.0,
          "Scale": 1.0,
          "Enabled": true
        },
        {
          "Name": "SS",
          "Id": "SS",
          "Min": 0.0,
          "Max": 1.0,
          "Scale": 1.0,
          "Enabled": true
        },
        {
          "Name": "nn",
          "Id": "nn",
          "Min": 0.0,
          "Max": 1.0,
          "Scale": 1.0,
          "Enabled": true
        },
        {
          "Name": "RR",
          "Id": "RR",
          "Min": 0.0,
          "Max": 1.0,
          "Scale": 1.0,
          "Enabled": true
        },
        {
          "Name": "aa",
          "Id": "aa",
          "Min": 0.0,
          "Max": 1.0,
          "Scale": 1.0,
          "Enabled": true
        },
        {
          "Name": "E",
          "Id": "E",
          "Min": 0.0,
          "Max": 1.0,
          "Scale": 1.0,
          "Enabled": true
        },
        {
          "Name": "ih",
          "Id": "ih",
          "Min": 0.0,
          "Max": 1.0,
          "Scale": 1.0,
          "Enabled": true
        },
        {
          "Name": "oh",
          "Id": "oh",
          "Min": 0.0,
          "Max": 1.0,
          "Scale": 4.0,
          "Enabled": true
        },
        {
          "Name": "ou",
          "Id": "ou",
          "Min": 0.0,
          "Max": 1.0,
          "Scale": 4.0,
          "Enabled": true
        }
      ],
      "Mappings": [
        {
          "Type": "Shape",
          "Id": "sil",
          "Targets": [
            {
              "Id": "ParamMouthForm",
              "Value": 0
            },
            {
              "Id": "ParamMouthOpenY",
              "Value": 0
            },
            {
              "Id": "ParamTongue",
              "Value": 0
            },
            {
              "Id": "ParamJaw",
              "Value": 0
            }
          ]
        },
        {
          "Type": "Shape",
          "Id": "PP",
          "Targets": [
            {
              "Id": "ParamMouthForm",
              "Value": -0.5
            },
            {
              "Id": "ParamMouthOpenY",
              "Value": 0
            },
            {
              "Id": "ParamTongue",
              "Value": 0
            },
            {
              "Id": "ParamJaw",
              "Value": 0
            }
          ]
        },
        {
          "Type": "Shape",
          "Id": "FF",
          "Targets": [
            {
              "Id": "ParamMouthForm",
              "Value": -0.8
            },
            {
              "Id": "ParamMouthOpenY",
              "Value": 0.1
            },
            {
              "Id": "ParamTongue",
              "Value": 0
            },
            {
              "Id": "ParamJaw",
              "Value": 0
            }
          ]
        },
        {
          "Type": "Shape",
          "Id": "TH",
          "Targets": [
            {
              "Id": "ParamMouthForm",
              "Value": 0.5
            },
            {
              "Id": "ParamMouthOpenY",
              "Value": 0.35
            },
            {
              "Id": "ParamTongue",
              "Value": 0.5
            },
            {
              "Id": "ParamJaw",
              "Value": 0.1
            }
          ]
        },
        {
          "Type": "Shape",
          "Id": "DD",
          "Targets": [
            {
              "Id": "ParamMouthForm",
              "Value": 0.6
            },
            {
              "Id": "ParamMouthOpenY",
              "Value": 0.45
            },
            {
              "Id": "ParamTongue",
              "Value": 0.6
            },
            {
              "Id": "ParamJaw",
              "Value": 0.3
            }
          ]
        },
        {
          "Type": "Shape",
          "Id": "kk",
          "Targets": [
            {
              "Id": "ParamMouthForm",
              "Value": 0.7
            },
            {
              "Id": "ParamMouthOpenY",
              "Value": 0.55
            },
            {
              "Id": "ParamTongue",
              "Value": 0.2
            },
            {
              "Id": "ParamJaw",
              "Value": 0.3
            }
          ]
        },
        {
          "Type": "Shape",
          "Id": "CH",
          "Targets": [
            {
              "Id": "ParamMouthForm",
              "Value": -0.7
            },
            {
              "Id": "ParamMouthOpenY",
              "Value": 0.3
            },
            {
              "Id": "ParamTongue",
              "Value": 0.7
            },
            {
              "Id": "ParamJaw",
              "Value": 0.2
            }
          ]
        },
        {
          "Type": "Shape",
          "Id": "SS",
          "Targets": [
            {
              "Id": "ParamMouthForm",
              "Value": 0.6
            },
            {
              "Id": "ParamMouthOpenY",
              "Value": 0.35
            },
            {
              "Id": "ParamTongue",
              "Value": 0.6
            },
            {
              "Id": "ParamJaw",
              "Value": 0.2
            }
          ]
        },
        {
          "Type": "Shape",
          "Id": "nn",
          "Targets": [
            {
              "Id": "ParamMouthForm",
              "Value": 0.35
            },
            {
              "Id": "ParamMouthOpenY",
              "Value": 0.45
            },
            {
              "Id": "ParamTongue",
              "Value": 0.6
            },
            {
              "Id": "ParamJaw",
              "Value": 0.3
            }
          ]
        },
        {
          "Type": "Shape",
          "Id": "RR",
          "Targets": [
            {
              "Id": "ParamMouthForm",
              "Value": 0.65
            },
            {
              "Id": "ParamMouthOpenY",
              "Value": 0.45
            },
            {
              "Id": "ParamTongue",
              "Value": 1
            },
            {
              "Id": "ParamJaw",
              "Value": 0.2
            }
          ]
        },
        {
          "Type": "Shape",
          "Id": "aa",
          "Targets": [
            {
              "Id": "ParamMouthForm",
              "Value": 1
            },
            {
              "Id": "ParamMouthOpenY",
              "Value": 1
            },
            {
              "Id": "ParamTongue",
              "Value": 0.5
            },
            {
              "Id": "ParamJaw",
              "Value": 1
            }
          ]
        },
        {
          "Type": "Shape",
          "Id": "E",
          "Targets": [
            {
              "Id": "ParamMouthForm",
              "Value": 1
            },
            {
              "Id": "ParamMouthOpenY",
              "Value": 0.7
            },
            {
              "Id": "ParamTongue",
              "Value": 0.5
            },
            {
              "Id": "ParamJaw",
              "Value": 0.4
            }
          ]
        },
        {
          "Type": "Shape",
          "Id": "ih",
          "Targets": [
            {
              "Id": "ParamMouthForm",
              "Value": 1
            },
            {
              "Id": "ParamMouthOpenY",
              "Value": 0.4
            },
            {
              "Id": "ParamTongue",
              "Value": 0.5
            },
            {
              "Id": "ParamJaw",
              "Value": 0.1
            }
          ]
        },
        {
          "Type": "Shape",
          "Id": "oh",
          "Targets": [
            {
              "Id": "ParamMouthForm",
              "Value": -1
            },
            {
              "Id": "ParamMouthOpenY",
              "Value": 1
            },
            {
              "Id": "ParamTongue",
              "Value": 0
            },
            {
              "Id": "ParamJaw",
              "Value": 0.5
            }
          ]
        },
        {
          "Type": "Shape",
          "Id": "ou",
          "Targets": [
            {
              "Id": "ParamMouthForm",
              "Value": -1
            },
            {
              "Id": "ParamMouthOpenY",
              "Value": 0.4
            },
            {
              "Id": "ParamTongue",
              "Value": 0.2
            },
            {
              "Id": "ParamJaw",
              "Value": 0.2
            }
          ]
        }
      ],
      "PostProcessing": {
        "BlendRatio": 0.5,
        "Smoothing": 30,
        "SampleRate": 30
      }
    }
  ]
}
```
