#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import re

# notes_regex = re.compile("[a-g]")

# lista-de-notas = "c cis d dis e f fis g gis a ais b"
l = "ees"

with open('teste.ly', 'r') as f:
    p = f.read()
    # n = re.findall(r"\w+is", p)
    # n = re.findall(r"\w+", p)
    n = re.findall(l, p)
    print(n)
