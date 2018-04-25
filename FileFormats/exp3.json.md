# exp3.json File Format Specifications

## Json Schema

```json
{
    "$schema": "http://json-schema.org/schema#",
    "title": "Cubism exp3.json File Format",
    "type":"object",
    "properties":
    {
        "Type":
         {
            "description":"Json file format type.",
            "type":"string",
            "enum": ["Live2D Expression"]
        },
        "FadeIn":
         {
            "description":"[Optional] Time of the Fade-In for easing in seconds.",
            "type":"number",
            "minimum":0
        },
        "FadeOut":
         {
            "description":"[Optional] Time of the Fade-Out for easing in seconds.",
            "type":"number",
            "minimum":0
        },
        "Parameters":
         {
            "type":"array",
            "items":
              {
                "description":"Targeted parameter list.",
                "type":"object",
                "properties":
                  {
                    "Id":{"type":"string"},
                    "Value":{"type":"number"},
                    "Blend":{"type":"string","enum":["Add","Multiply","Overwrite"]}
                },
                "required": ["Id", "Value"],
                "additionalProperties": false
            }
        }
    },
    "required": ["Type", "Parameters"],
    "additionalProperties": false
}
```

---

## Description

### Parameters

exp3.json targets only the parameters of the model.

#### Blend

| Type | Description | Value |
| - | - | - |
| "Add" | Add to the original value of the parameter | Value = SettingValue - DefalutValue |
| "Multiply" | Multiply the original value of the parameter | Value = SettingValue |
| "Overwrite" | Overwrite parameters | Value = SettingValue |

---

## Json Example

```json
{
  "Type": "Live2D Expression",
  "Parameters": [
    {
      "Id": "ParamBrowLY",
      "Value": -1,
      "Blend": "Add"
    },
    {
      "Id": "ParamBrowRY",
      "Value": -1,
      "Blend": "Add"
    },
    {
      "Id": "ParamBrowLForm",
      "Value": 1,
      "Blend": "Add"
    },
    {
      "Id": "ParamBrowRForm",
      "Value": 1,
      "Blend": "Add"
    },
    {
      "Id": "ParamMouthOpenY",
      "Value": 1,
      "Blend": "Add"
    },
    {
      "Id": "ParamEyeForm",
      "Value": 0.54,
      "Blend": "Add"
    }
  ]
}
```
