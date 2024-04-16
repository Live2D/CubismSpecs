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
      "AnalysisType": "CRI",
      "UseCase": "Mouth",
      "CubismParameters": [
        {
          "Name": "Mouth_Open",
          "Id": "ParamMouthOpenY",
          "Min": 0.0,
          "Max": 1.0,
          "Damper": 0.0,
          "Smooth": 25
        },
        {
          "Name": "A",
          "Id": "ParamA",
          "Min": 0.0,
          "Max": 1.0,
          "Damper": 0.0,
          "Smooth": 25
        },
        {
          "Name": "I",
          "Id": "ParamI",
          "Min": 0.0,
          "Max": 1.0,
          "Damper": 0.0,
          "Smooth": 25
        },
        {
          "Name": "U",
          "Id": "ParamU",
          "Min": 0.0,
          "Max": 1.0,
          "Damper": 0.0,
          "Smooth": 25
        },
        {
          "Name": "E",
          "Id": "ParamE",
          "Min": 0.0,
          "Max": 1.0,
          "Damper": 0.0,
          "Smooth": 25
        },
        {
          "Name": "O",
          "Id": "ParamO",
          "Min": 0.0,
          "Max": 1.0,
          "Damper": 0.0,
          "Smooth": 25
        }
      ],
      "AudioParameters": [
        {
          "Name": "Silence",
          "Id": "Silence",
          "Min": 0.0,
          "Max": 1.0,
          "Scale": 1.0,
          "Enabled": true
        },
        {
          "Name": "A",
          "Id": "A",
          "Min": 0.0,
          "Max": 1.0,
          "Scale": 0.30000001192092896,
          "Enabled": true
        },
        {
          "Name": "I",
          "Id": "I",
          "Min": 0.0,
          "Max": 1.0,
          "Scale": 1.0,
          "Enabled": true
        },
        {
          "Name": "U",
          "Id": "U",
          "Min": 0.0,
          "Max": 1.0,
          "Scale": 1.5,
          "Enabled": true
        },
        {
          "Name": "E",
          "Id": "E",
          "Min": 0.0,
          "Max": 1.0,
          "Scale": 6.0,
          "Enabled": true
        },
        {
          "Name": "O",
          "Id": "O",
          "Min": 0.0,
          "Max": 1.0,
          "Scale": 8.0,
          "Enabled": true
        }
      ],
      "Mappings": [
        {
          "Type": "Shape",
          "Id": "Silence",
          "Targets": [
            {
                "Id": "ParamMouthOpenY",
                "Value": 0.0
            },
            {
                "Id": "ParamA",
                "Value": 0.0
            },
            {
                "Id": "ParamI",
                "Value": 0.0
            },
            {
                "Id": "ParamU",
                "Value": 0.0
            },
            {
                "Id": "ParamE",
                "Value": 0.0
            },
            {
                "Id": "ParamO",
                "Value": 0.0
            }
          ]
        },
        {
          "Type": "Shape",
          "Id": "A",
          "Targets": [
            {
                "Id": "ParamMouthOpenY",
                "Value": 1.0
            },
            {
                "Id": "ParamA",
                "Value": 1.0
            },
            {
                "Id": "ParamI",
                "Value": 0.0
            },
            {
                "Id": "ParamU",
                "Value": 0.0
            },
            {
                "Id": "ParamE",
                "Value": 0.0
            },
            {
                "Id": "ParamO",
                "Value": 0.0
            }
          ]
        },
        {
          "Type": "Shape",
          "Id": "I",
          "Targets": [
            {
                "Id": "ParamMouthOpenY",
                "Value": 1.0
            },
            {
                "Id": "ParamA",
                "Value": 0.0
            },
            {
                "Id": "ParamI",
                "Value": 1.0
            },
            {
                "Id": "ParamU",
                "Value": 0.0
            },
            {
                "Id": "ParamE",
                "Value": 0.0
            },
            {
                "Id": "ParamO",
                "Value": 0.0
            }
          ]
        },
        {
          "Type": "Shape",
          "Id": "U",
          "Targets": [
            {
                "Id": "ParamMouthOpenY",
                "Value": 1.0
            },
            {
                "Id": "ParamA",
                "Value": 0.0
            },
            {
                "Id": "ParamI",
                "Value": 0.0
            },
            {
                "Id": "ParamU",
                "Value": 1.0
            },
            {
                "Id": "ParamE",
                "Value": 0.0
            },
            {
                "Id": "ParamO",
                "Value": 0.0
            }
          ]
        },
        {
          "Type": "Shape",
          "Id": "E",
          "Targets": [
            {
                "Id": "ParamMouthOpenY",
                "Value": 1.0
            },
            {
                "Id": "ParamA",
                "Value": 0.0
            },
            {
                "Id": "ParamI",
                "Value": 0.0
            },
            {
                "Id": "ParamU",
                "Value": 0.0
            },
            {
                "Id": "ParamE",
                "Value": 1.0
            },
            {
                "Id": "ParamO",
                "Value": 0.0
            }
          ]
        },
        {
          "Type": "Shape",
          "Id": "O",
          "Targets": [
            {
                "Id": "ParamMouthOpenY",
                "Value": 1.0
            },
            {
                "Id": "ParamA",
                "Value": 0.0
            },
            {
                "Id": "ParamI",
                "Value": 0.0
            },
            {
                "Id": "ParamU",
                "Value": 0.0
            },
            {
                "Id": "ParamE",
                "Value": 0.0
            },
            {
                "Id": "ParamO",
                "Value": 1.0
            }
          ]
        }
      ],
      "PostProcessing": {
          "BlendRatio": 0.5,
          "Smoothing": 60,
          "SampleRate": 60.0
      }
    }
  ]
}
```
