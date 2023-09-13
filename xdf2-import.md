# `xdf2` Import

All of the created `xdf2` files are located in decentralized repositories.
Some of those repositories use the `FRED` editor, which provides an interface to import all
available schemas. We use this interface to fill our database with the available schemas.

The import must run in several steps:

1. Load an initial `html` page containing a list of all the available files of the types "Dokumentensteckbrief" and "Stammdatenschema" respetively.
2. For each Dokumentensteckbrief, load a custom `json` object containing several fields of the Dokumentensteckbrief. The `xml` file of the Dokumentensteckbrief as defined in `xdf2` is not available via this method. Parts of the Dokumentensteckbrief are therefore imported by mapping the available fields to those defined by the standard (see below).
3. For each Stammdatenschema, load a custom `json` object containing links to the schema itself and the code lists used by the schema as well as additional metadata. All of those files are then loaded and imported. In addition, the field `freigabe_status` is not part of `xdf2` and is therefore also imported from the `json` file.

### Mapping for "Dokumentensteckbrief"

The fields available in the custom `json` object for a Dokumentensteckbrief have a tight correspondence to the fields available in `xdf3`. Since the internal representation of our project is in `xdf3`, those fields are mapped accordingly, for example:
`Status gesetzt durch` (`json`) is mapped to `status_gesetzt_durch` (`xdf3`).
