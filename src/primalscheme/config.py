"""
PrimalScheme: a primer3 wrapper for designing multiplex primer schemes

Copyright (C) 2020 Joshua Quick and Andrew Smith
www.github.com/aresti/primalscheme

This module contains config values.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""


PREFIX = "scheme"
OUTPUT_PATH = "./output"
MAX_ALN_GAP_PERCENT = 0.03

TARGET_OVERLAP = 0
STEP_DISTANCE = 11
AMPLICON_SIZE_MIN = 380
AMPLICON_SIZE_MAX = 420
SIZE_RANGE_AUTO = 0.1

PRIMER_SIZE_MIN = 22
PRIMER_SIZE_MAX = 30
PRIMER_OPT_SIZE = PRIMER_SIZE_MIN

PRIMER_OPT_TM = 61.0
PRIMER_WT_TM_GT = 1.0
PRIMER_WT_TM_LT = 1.0
PRIMER_MIN_TM = 59.5
PRIMER_MAX_TM = 62.5
PRIMER_WT_SIZE_GT = 1.0
PRIMER_WT_SIZE_LT = 1.0
PRIMER_OPT_GC_PERCENT = 50.0
PRIMER_WT_GC_PERCENT_GT = 0.0
PRIMER_WT_GC_PERCENT_LT = 0.0
PRIMER_MIN_GC = 30
PRIMER_MAX_GC = 55
PRIMER_MAX_HAIRPIN_TH = 50
PRIMER_MAX_HOMO = 5

PRIMER_MAX_MISMATCHES = 2
PRIMER_MISMATCH_PENALTIES = [3, 2, 1]  # distance from 3', last is default

MV_CONC = 100.0
DV_CONC = 2.0
DNA_CONC = 15.0
DNTP_CONC = 0.8
TEMP_C = 65.0
HETERODIMER_DG_THRESHOLD = -2.0
