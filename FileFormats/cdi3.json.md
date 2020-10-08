# cdi3.json File Format Specifications

- [Json Schema](/Schemas/cdi3.schema.json)
- [Example Json](/Examples/example.cdi3.json)

[Official manual](https://docs.live2d.com/cubism-sdk-manual/cdi3json)

## Description

Each parameter or parameter group has a groupId identifier. The corresponding group is defined in ParameterGroups. Empty string means it doesn't belong to any groups. The elements in the list are sorted. Therefore, if a parameter AngleX has a groupId ParamGroupHead, you should create a parameter group called Head then add the parameter AngleX in to it. The next parameter AngleY has a groupId with empty string will be placed right after the parameter group Head.
