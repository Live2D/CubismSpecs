# exp3.json File Format Specifications

- [Json Schema](/Schemas/exp3.schema.json)
- [Example Json](/Examples/example.exp3.json)

## Description

### Parameters

exp3.json targets only the parameters of the model.

#### Blend

| Type | Description | Value |
| --- | --- | --- |
| `Add` | Add to the original value of the parameter | `Value = SettingValue - DefaultValue` |
| `Multiply` | Multiply the original value of the parameter | `Value = SettingValue` |
| `Overwrite` | Overwrite parameters | `Value = SettingValue` |
