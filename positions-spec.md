## Positions
This document describes the fields in the positions.json file.

### Goals
Below are some goals for this effort to collect a list of elected positions:
* Human AND machine readable
* Anyone can suggest edits (or file issues)
* Relatively "flat" - Data can be represented as a single table

Below are some features intentionally NOT in the initial scope:
* Geospatial data - Geospatial data like shape files can be kept separately and joined by jurisdiction (and possibly district)
* Non-public contact info - `contactId`could be used as a reference into another system that might store non-public contact info

### Use Cases / Scenarios
Below are some possible use cases / scenarios:
* Identify positions up for election in a given year
* Identify elected incumbents to support or challenge (including party affiliation and/or past support)

### Style
All fields are treated as text strings
* Years should use four digits
* Proper nouns should be capitalized

### Example
Below is an example of an object from the positions.json file:
``` JSON
{
  "posTermNext": "2017",
  "posCounty": "King",
  "posJurisdiction": "City of Kirkland",
  "posIncumbent": 
  {
    "first": "Jay",
    "last": "Arnold",
    "email": "jarnold@kirklandwa.gov",
    "phone": "425-587-3001",
    "party": "",
    "contactId": ""
  }
}
```

### posTermStart
(Optional) Year when the position was most recently previously elected

### posTermNext
(Required) Year when the position will be next up for election

### posTermLength
(Optional) The number of years the position is elected for

### posCounty
(Required) The county that manages this election (or "Statewide")

### posJurisdiction
(Required) The jurisdiction for the elected office

### pos...
// TODO: Finish based on data

### posIncumbent
(Optional) An object representing the incument hosting this position

Below are fields of the posIncumbent object:
* first
* last
* email
* phone
* party - Expected values: "Dem", "Rep", "Lib", "Gre", "Soc", "NPD", "NPR", "NPL", "NPG", "NPS"
* contactId - A randomly generated integer unique to this person

