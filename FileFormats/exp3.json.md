# exp3.json File Format Specifications

## Json Schema

Refer [/Schemas/exp3.schema.json](/Schemas/exp3.schema.json).

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
