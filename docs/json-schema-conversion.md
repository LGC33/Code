# `xdf2` JSON Schema Conversion

JSON Schema has three kinds of basic data types: `object`, `array` and `primitive` (e.g. `string` or `integer`).
The mapping from the tree of elements within a Stammdatenschema to these data types tries to
retain the structure of the original data as much as possible.

## Mapping `Schema` and `Datenfeldgruppe`

As JSON Schema does not have support for many of the attributes from XDatenfelder,
the top-level Schema and the contained Datenfeldgruppen are mapped identically as `object`s.
Each child of the node `<xdf:Struktur>` is modelled as a property of this `object`.
Depending on the field `anzahl`, this property is either `required` or `optional`.
If `anzahl` allows multiple items, the property is modelled as an `array`.

## Mapping `Datenfeld`

All elements of type `label` are ignored.
Each Datenfeld of type `input` is mapped to the closest possible `primitive` data type of JSON Schema:

| Datentyp       | JSON Schema                                 |
| -------------- | ------------------------------------------- |
| `text`         | `{"type": "string"}`                        |
| `text_latin`   | `{"type": "string"}`                        |
| `date`         | `{"type": "string", "format": "date"}`      |
| `time`         | `{"type": "string", "format": "time"}`      |
| `datetime`     | `{"type": "string", "format": "date-time"}` |
| `num`          | `{"type": "number"}`                        |
| `num_int`      | `{"type": "integer"}`                       |
| `num_currency` | `{"type": "number", "multipleOf": 0.01}`    |
| `bool`         | `{"type": "boolean"}`                       |
| `file`         | `{"type": "string"}`                        |
| `obj`          | `{"type": "string"}`                        |

For a Datenfeld of type `input` all code list information is always ignored.

For type `select`, the specified `Datentyp` is always ignored and mapped do `string` instead.
If a code list is referenced or a value list is embedded, the options defined by the list are included as an `enum` property.

## Rules

For both xdf2 and xdf3, all `Regel` elements are ignored for the conversion.
