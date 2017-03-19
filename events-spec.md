# Events Calendar

A public calendar of events of potential interest to Democratic party activists, candidates, and elected officials.
The calendar may include events from: local Democratic party organizations, candidates, elected officials, and allied organizations.

## Contents
* [Getting Involved](#getting-involved)
* [Project Goals](#project-goals)
  * [v1.0 Feature Goals](#v10-feature-goals)
  * [vNext Feature Goals](#vnext-feature-goals)
* [Event Listing Policy](#event-listing-policy) (DRAFT)
* [Events Data Schema](#events-data-schema) 

## Getting Involved
The project maintainers are using a [public GitHub repository](https://github.com/WashDems-Public/Data) for data, code, and discussion:
* **Specification/Plan**: https://github.com/WashDems-Public/Data/blob/gh-pages/events-spec.md
* **Prototype**: https://washdems-public.github.io/Data/events.html
* **Data**: Open, public JSON data on GitHub: 
  [View](https://washdems-public.github.io/Data/events.json) 
  | [Edit](https://github.com/WashDems-Public/Data/blob/gh-pages/events.json)
* **Code**: Open source (MIT License) HTML and JavaScript on GitHub: 
  [View](https://washdems-public.github.io/Data/events.html)
  | [Edit](https://github.com/WashDems-Public/Data/blob/gh-pages/events.html)
* **Discussion**: [Slack #events-calendar](https://washdems.slack.com/messages/C27GEDBGT/details/) channel
* **Bugs/Issues**: [GitHub Issues](https://github.com/WashDems-Public/Data/issues)

## Project Goals

* Democratic activists, potential activists, candidates, and elected officials can find an upcoming event
* Democratic activists, party leaders, candidates, elected officials, and staff have a single, central source for events
* Democratic party organizations, candidates, and elected officials can suggest an event to add
 
### v1.0 Feature Goals

#### Event display
* [X] Event title, date, time, location, title
* [X] Event title hyperlinks to more info about the event

#### Views
* [X] Default list of events
* [X] Mini list of events for embedding in a web widget
* [X] Full list of events for embedding in a web page
* [ ] Calendar view of events [#66](https://github.com/WashDems-Public/Data/issues/66)

#### Filters
* [ ] Date
  * [X] All events
  * [ ] Upcoming events
  * [ ] Past event
* [ ] Organization
  * [X] All orgs
  * [ ] Single selected organization [#67](https://github.com/WashDems-Public/Data/issues/67)

#### Export
* [ ] Add a single event to your calendar [#69](https://github.com/WashDems-Public/Data/issues/69)
  * [ ] Google Calendar
  * [ ] Microsoft Outlook
  * [ ] iPhone calendar
* [ ] Add events from a filtered view to your calendar [#70](https://github.com/WashDems-Public/Data/issues/70)
  * [ ] Google Calendar
  * [ ] Microsoft Outlook
  * [ ] iPhone calendar


### vNext Feature Goals

#### Event display
* [ ] Event organization hyperlinks to that organization if in [Orgs JSON](https://washdems-public.github.io/Data/orgs.json)

#### Filters
* [ ] Organization
  * [ ] Filtering to a geographic organization (ex: LD or County) includes events within that LD or County [#68](https://github.com/WashDems-Public/Data/issues/68)
  
#### Export
* [ ] WordPress plug-in or module for displaying a view on the events calendar [#59](https://github.com/WashDems-Public/Data/issues/59)


## Event Listing Policy
Below is a DRAFT event listing policy.  
SHOULD, MAY, and SHOULD NOT are intended to have meanings as described in IETF [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

These events SHOULD be listed:
* (Non-recurring) events hosted by local Democratic party organizations
* (Non-recurring) events for Democratic candidates
* (Non-recurring) events for Democratic elected officials
* (Non-recurring) events for non-partisan candidates who are endorsed by a preponderance of local Democratic party organizations
* (Non-recurring) events for ballot measure positions endorsed by a preponderance of local Democratic party organizations

These events MAY be listed:
* Recurring events with specific agendas (ex: monthly meeting with a panel, endorsements vote, officer elections, etc.)
* Recurring events with a special guest (ex: weekly campaign phone bank joined by a special guest)
* Events for non-partisan candidates who have previously been endorsed by a local Democratic organization but not endorsed this cycle

These events SHOULD NOT be listed:
* Recurring Democratic organization business meetings or board meetings without agendas specific to that meeting
* Campaign events for non-partisan candidates who have never been endorsed by a local Democratic organization


## Events Data Schema
This section describes the fields in the orgs.json file.

### eventDate
(Required) The day and date on which the event takes place.  (ex: "Thu, 12/1")

### eventStartTime
(Required) The time at which the evnet starts.  (ex: "7:00 PM")

### eventEndTime
(Optional) The time at which the event ends.  

### eventOrgShort
(Required) Short name for the organization hosting.  
See [Orgs Spec](https://github.com/WashDems-Public/Data/blob/gh-pages/orgs-spec.md#orgshort)

### eventOrgType
(Required) A descriptor of the organization type.  (ex: "LD", "County", "State", "Ally")
See [Orgs Spec](https://github.com/WashDems-Public/Data/blob/gh-pages/orgs-spec.md#orgtype)

### eventTitle
(Required) A title for the event.  
Please do NOT include the name of the organization hosting the event.

### eventLocationName
(Required) Name of the location where the event will be held. 
(ex: "Yakima County Democrats office", 
"Mercer Island Community Center", 
"Home of John Smith")

### eventLocationStreet
(Optional) Street address for the event location. (ex: "123 Main St.")

### eventLocationCity
(Optional) City for the event location (ex: "Wenatchee")

### eventLocationST
(Optional) Two-letter state abberviation for the event location (ex: "WA")

### eventLocationZip
(Optional) ZIP code for the event location (ex: "98040")

### eventWeb
(Required) Web address where visitors can find more information about this event.

### eventFbId
(Optional) Facebook ID for this event (ex: "1811175945791682")

### eventDescription
(Optional) Additional details about this event. 
(ex: "Doors open at 6pm and program starts at 7pm", 
"Dinner will be served", 
"Suggested $20 donation")
