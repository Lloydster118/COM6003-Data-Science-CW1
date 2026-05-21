# COM6003 Data Science — CW1

Coursework 1 for **COM6003 Data Science** at Buckinghamshire New University.
Analysis of Energy Performance Certificate (EPC) data for the Buckinghamshire
local authority (`E06000060`), covering data wrangling, descriptive and
diagnostic analytics, and a predictive model for current energy efficiency
ratings.

## Project structure

```
.
├── data/
│   ├── raw/                 # raw EPC zip (gitignored — see Data section)
│   └── processed/
│       └── bucks_epc_clean.csv
├── notebooks/
│   └── bucks_epc_analysis.ipynb
├── figures/                 # exported PNGs


├── src/                     # helper scripts
├── requirements.txt
└── README.md
```

## Data

The dataset is the **Domestic Energy Performance Certificates** for
Buckinghamshire (local authority code `E06000060`), obtained from the
official EPC Open Data service:

> Ministry of Housing, Communities and Local Government (2026)
> *Energy Performance of Buildings Data: England and Wales*.
> Available at: <https://epc.opendatacommunities.org/> (Accessed: 22 May 2026).

The raw zip is **not** committed to this repository because:

1. The dataset is large.
2. It contains personal address data subject to Royal Mail / Crown copyright
   restrictions.
3. The licence requires users to obtain the data directly from the source.

To reproduce, download the Buckinghamshire domestic certificates zip from the
EPC Open Data portal and place it at `data/raw/`, then run the notebook.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Then open `notebooks/bucks_epc_analysis.ipynb` and run all cells.

## Author

Harry Lloyd — Student ID 22224922
BSc Computer Science with AI, Buckinghamshire New University
