klifs_utils
==============================
[//]: # (Badges)
[![Travis Build Status](https://travis-ci.com/REPLACE_WITH_OWNER_ACCOUNT/klifs_utils.svg?branch=master)](https://travis-ci.com/REPLACE_WITH_OWNER_ACCOUNT/klifs_utils)
[![AppVeyor Build status](https://ci.appveyor.com/api/projects/status/REPLACE_WITH_APPVEYOR_LINK/branch/master?svg=true)](https://ci.appveyor.com/project/REPLACE_WITH_OWNER_ACCOUNT/klifs_utils/branch/master)
[![codecov](https://codecov.io/gh/REPLACE_WITH_OWNER_ACCOUNT/klifs_utils/branch/master/graph/badge.svg)](https://codecov.io/gh/REPLACE_WITH_OWNER_ACCOUNT/klifs_utils/branch/master)

Utility functions to work with KLIFS data


### KLIFS

The `klifs_utils` package offers functions to interact with data from KLIFS (remotely and locally).

What is KLIFS and who created it?

> Kinase-Ligand Interaction Fingerprints and Structures database (KLIFS), developed at the Division of Medicinal Chemistry - VU University Amsterdam, is a database that revolves around the protein structure of catalytic kinase domains and the way kinase inhibitors can interact with them
* KLIFS database: https://klifs.vu-compmedchem.nl
* KLIFS online service: https://klifs.vu-compmedchem.nl/swagger
* KLIFS citation
  * Description of the database itself [(*J. Med. Chem.* (2014), **57**, 2, 249-277)]()
  * Description of the online service [(*Nucleic Acids Res.* (2016), **44**, 6, D365–D371)]()



### Installation

1. Download GitHub repo:

    ```bash
    git clone https://github.com/dominiquesydow/klifs_utils.git
    ```
    
    The library lives now in this example path `/path/to/klifs_utils`.
    
2. Install and activate conda environment `klifs_utils`:
    ```bash
    conda env create -f /path/to/klifs_utils/devtools/conda_envs/env.yaml
    conda activate klifs
    ```

3. Install library in conda environment while being in path `/path/to`:

    ```bash
    pip install klifs_utils
    ```


### Usage

Check out the `klifs_utils` tutorial (Jupyter notebook):

```bash
/klifs_utils/tutorial/tutorial.ipynb
```

#### Work with KLIFS data from KLIFS server (remotely)

The `klifs_utils.remote` module offers you to access KLIFS data from the KLIFS server.

This module uses the official KLIFS API: https://klifs.vu-compmedchem.nl/swagger.

#### Work with KLIFs data from disc (locally)

The `klifs_utils.local` module offers you to access KLIFS data from the KLIFS server. In order to make use of the
module's functionality, you need a KLIFS download folder `KLIFS_download` with the following structure:

```
└── KLIFS_download
    ├── KLIFS_export.csv           # Metadata file
    ├── overview.csv               # Metadata file
    └── HUMAN     	               # Species name  
        ├── AAK1                   # Kinase name
        │   ├── 4wsq_altA_chainA   # PDB ID, alternate model ID, chain ID
        │   │   ├── complex.mol2
        │   │   ├── ligand.mol2
        │   │   ├── protein.mol2
        │   │   ├── pocket.mol2
        │   │   └── water.mol2
        │   └── ...
        └── ...
```

Download KLIFS data from: https://klifs.vu-compmedchem.nl

### Copyright

Copyright (c) 2020, Dominique Sydow


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.1.
