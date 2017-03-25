## Organizations (Orgs)
This document describes the fields in the orgs.json file.

### orgShort
(Required) A short name for the organization.  Counties should be the county name.  Legislative districts should be the LD number, zero-padded if a single digit (ex: 03rd)

### orgType
(Required) A descriptor of the organization type.  Expected values are: "County", "LD", "State Young", "County Young", "College Young", "HS Young", "Caucus", and "CD" (Congressional District).  Concatenation of orgShort & orgType & "Democrats" (or "Dems") should yield a reasonable but sometimes imperfect organization full name.

### orgFull
(Optional) Full name of the organization (ex: "1st Legislative District Democrats" or "King County Democratic Central Committee")

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

### orgBylaws
(Optional) URL to the organization's governing documents such as a charter, bylaws, or standing rules

### orgBylawsArchive
(Optional) URL to an archived copy of the organization's governing documents

### orgEndorsements2016
(Optional) URL to the organization's list of endorsed candidates and ballot measures for 2016
