## Positions
This document describes the fields in the positions.json file.

### Example
Below is an example of an object from the positions.json file:
// TODO

### posTerm
(Required) An object representing the term of the position
* start (optional) - Year when the position was most recently previously elected 
* next (required) - Year when the position will be next up for election

### posTerm
(Optional) The number of years the position is elected for

### posCounty
(Required) The county that manages this election (or "Statewide")

### posJurisdiction

// TODO: Finish based on examples

### posIncumbent
(Optional) An object representing the incument hosting this position

Below are fields of the posIncumbent object:
* first
* last
* email
* phone
* party - Expected values: "Dem", "Rep", "Lib", "Gre", "Soc"
* contactId - A randomly generated integer unique to this person

