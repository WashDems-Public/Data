## Positions
This document describes the fields in the positions.json file.

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

