# motion3.json File Format Specifications

## Json Schema

Refer [/Schemas/motion3.schema.json](/Schemas/motion3.schema.json).

---

## Description

### Tracks

#### Track Targets

One of the following:

| Target | Description |
| - | - |
| "Model" | Track targets model. |
| "Parameter" | Track targets a parameter. The track ID then is the parameter ID. |
| "PartOpacity" | Track targets a part opacity. The track ID then is the parts ID. |

##### Model Target Identifiers

One of the following:

| Id | Description |
| - | - |
| "Opacity" | Opacity track applying to the model as a whole. |
| "EyeBlink" | Eye track. |
| "LipSync" | Mouth opening track. |

#### Track Curves

Curves are made up of points and segment identifiers packed into a single flat array.

A point is a sequence of 2 numbers, where *the first number is its timing in seconds*,
hereinafter simply t, and *the second number its value at t*.

A segment identifier is single number with one of the following values.

| Value | Description |
| - | - |
| 0 | Identifier for linear segment. |
| 1 | Identifier for cubic bézier segment. |
| 2 | Identifier for stepped segment |
| 3 | Identifier for inverse-stepped segment. |

*Each curve starts with the first point followed by the segment identifier*.
Therefore, *the first segment identifier is the third number in the flat segments array*.
Segments can be reconstructed by taking the point before the segment identifier and
combining it with the points until the next identifier (or until the end of the array).
A segment identifier is followed by *1 point in case of linear, stepped, and inverse stepped segments*,
that represents the end of the segment, or *3 point in case of bézier segments*, that represent P1, P2, P3.

The t components of bézier control points are proportionally fixed as follows.

```math
P1.t = (P3.t - P0.t) / 3
P2.t = ((P3.t - P0.t) / 3) * 2
```

Curves can't be empty.

---

## Json Example

```json
{
  "Version": 3,
  "Meta": {
    "Duration": 1,
    "Fps": 120,
    "FadeInTime": 2,
    "FadeOutTime": 2,
    "CurveCount": 3,
    "TotalSegmentCount": 3,
    "TotalPointCount": 6,
    "UserDataCount": 2,
    "TotalUserDataSize": 8
  },
  "UserData": [
    {
      "Time": 1.234,
      "Value": "hoge"
    },
    {
      "Time": 5.612,
      "Value": "fuga"
    }
  ],
  "Curves": [
    {
      "Target": "Model",
      "Id": "Opacity",
      "Segments": [0, 0, 0, 1, 1]
    },
    {
      "Target": "Parameter",
      "Id": "EyeLOpen",
      "Segments": [0, 0, 0, 1, 1]
    },
    {
      "Target": "PartOpacity",
      "Id": "ArmL",
      "FadeInTime": 2,
      "FadeOutTime": 2,
      "Segments": [0, 0, 0, 1, 1]
    }
  ]
}
```
