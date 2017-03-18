# Events Calendar (Orgs)

A public calendar of events of potential interest to Democratic party activists.  
The calendar may include events from: local Democratic party organizations, 

## Project Goals

 * Democratic activists, potential activists, candidates, and elected officials can find an upcoming event
 * Democratic activists, party leaders, candidates, elected officials, and staff can
 * Democratic party organizations, candidates, and elected officials can suggest an event to add
 
## Feature Goals for v1.0
* [ ] Event display
  * [X] Event title, date, time, location, title
  * [ ] Event title hyperlinks to more info about the event
* [ ] Views
  * [X] Default list of events
  * [X] Mini list of events for embedding in a web widget
  * [X] Full list of events for embedding in a web page
  * [ ] Calendar view of events
* [ ] Filters
  * [ ] Date
    * [ ] All events
    * [ ] Upcoming events
    * [ ] Past event
  * [ ] Organization
    * [ ] All orgs
    * [ ] Single selected organization
* [ ] Export
  * [ ] Add events from a filtered view to Google Calendar
  * [ ] Add events from a filtered view to Microsoft Outlook
  * [ ] Add events from a filtered view to iPhone calendar

### Feature Goals for vNext
* [ ] Event display
  * [ ] Event organization hyperlinks to that organization if in [Orgs JSON](https://washdems-public.github.io/Data/orgs.json)
* [ ] Filters
  * [ ] Organization
    * [ ] Filtering to a geographic organization (ex: LD or County) includes events within that LD or County

## Events Data Schema
This document describes the fields in the orgs.json file.

### eventDate
(Required) The day and date on which the event takes place.  (ex: "Thu, 12/1")

### eventStartTime
(Required) The time at which the evnet starts.  (ex: "7:00 PM")

### eventEndTime
(Optional) The time at which the event ends.  
