"""
Helper functions and constants for the COM6003 CW1 analysis.

Centralises mappings and colour palettes used in multiple notebook
sections, so they only have to be edited in one place.
"""
import numpy as np


# Ordinal scale used by every *_energy_eff column in the EPC dataset.
# Maps to 1-5 so it can be averaged into composite scores.
EFF_MAP = {
    'Very Poor': 1,
    'Poor': 2,
    'Average': 3,
    'Good': 4,
    'Very Good': 5,
    'unknown': np.nan,
    'N/A': np.nan,
}

# Official EPC band colours, taken from the colour values used on the
# certificate itself (see DESNZ EPC visual standards).
EPC_COLOURS = {
    'A': '#008054',
    'B': '#19B459',
    'C': '#8DCE46',
    'D': '#FFD500',
    'E': '#FCAA65',
    'F': '#EF8023',
    'G': '#E9153B',
}

# Band edges as used by RdSAP, for histogram backgrounds and binning.
# Each tuple is (lower_inclusive, upper_inclusive, letter).
BAND_EDGES = [
    (92, 100, 'A'),
    (81, 91,  'B'),
    (69, 80,  'C'),
    (55, 68,  'D'),
    (39, 54,  'E'),
    (21, 38,  'F'),
    (1,  20,  'G'),
]

RATING_ORDER = list('ABCDEFG')


def sap_to_band(score):
    """Convert a numeric SAP score (1-100) to its letter band."""
    for lo, hi, letter in BAND_EDGES:
        if lo <= score <= hi:
            return letter
    return None


def parse_age_band(s):
    """Parse the EPC construction_age_band string to a numeric year.

    Handles three formats found in the raw data:
    - 'England and Wales: 1950-1966'  -> 1958 (midpoint)
    - '2012 onwards'                  -> 2012
    - '2019'                          -> 2019
    Returns NaN for unrecognised values.
    """
    import pandas as pd

    if pd.isna(s):
        return np.nan
    s = str(s).replace('England and Wales:', '').strip()
    if 'before 1900' in s.lower():
        return 1899
    if 'onwards' in s.lower():
        return int(s.split()[0])
    if '-' in s:
        try:
            a, b = s.split('-')
            return (int(a.strip()) + int(b.strip())) / 2
        except ValueError:
            return np.nan
    try:
        return int(s)
    except ValueError:
        return np.nan
