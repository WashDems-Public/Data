## Organizations (Orgs)
This document describes the fields in the orgs.json file.

### orgShort
(Required) A short name for the organization.  Counties should be the county name.  Legislative districts should be the LD number, zero-padded if a single digit (ex: 03rd)

### orgType
(Required) A descriptor of the organization type.  Expected values are: "County", "LD", "County Young", "College Young", "HS Young", and "Caucus".  Concatenation of orgShort & orgType & Democrats should yield a reasonable but sometimes imperfect organization full name.

### orgWeb
(Optional) URL to the organization's public-facing website

### orgFbPage
(Optional) URL to the organization's Facebook page

### orgFbGroup
(Optional) URL to the organization's Facebook group

### orgTwAlias
(Optional) Twitter alias used by the organization (ex: "43rdDems" from https://twitter.com/43rdDems)

### orgOfficers
(Optional) URL to the organization's list of officers

### orgEndorsements2016
(Optional) URL to the organization's list of endorsed candidates and ballot measures for 2016







