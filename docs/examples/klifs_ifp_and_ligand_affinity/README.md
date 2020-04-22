# Example use cases of `klifs_utils`

- [Done] Get the interaction fingerprint (IFP) from KLIFS for a given kinase-ligand complex
  -  This already part of `klifs_utils` but maybe we can add some utility functions that allow bulk downloads directly (currently: kinases > kinase IDs > structures > structure IDs > IFPs)
- [Done] Get the associated binding affinity data
  - This is not part of `klifs_utils` yet. We use here web scraping to get the ligand affinities (since no API for this), however we might find a more elegant solution for this.
- Merge both data sets in one table
  - Per kinase-ligand complex, we get multiple ligand affinities. Think about whether merge is useful (probably not in the context of `klifs_utils`).
