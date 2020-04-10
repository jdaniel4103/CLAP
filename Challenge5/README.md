# Challenge 5: Dunham Expansion from Config File

This challenge will teach the basics of the Dunham expansion and how to read in from a config file.  The script will read in Dunham coefficients from a Config file, plug them into the Dunham Expansion, and produce the transition energy.  For this script, we will use 4 system arguments when calling the script to specify the v, J, v', and J' (the initial and final, vibrational and rotational quantum numbers).

## Dunham Expansion

The [Dunham expansion](https://en.wikipedia.org/wiki/Dunham_expansion) is one of the ways in which one can express the energy levels of a molecule.  The energy level depends on the electronic, vibrational, and rotational state that the molecule is in.  For this script, we will only consider a two-electronic-state system (of course a molecule has more than 2 electronic states, but typically only one electronic transition is probed at a time).

## ConfigParser

The ConfigParser package is very useful for creating configuration files and reading them in.  We use config files in the lab for several things, most visibly to keep track of all our monitoring sensors in the lab.

## Challenge Tasks

1. Read in the values from the included line_config.ini file (note: values are in wavenumbers).  Assume all unlisted coefficients are zero.

2. Using the [Dunham expansion](https://en.wikipedia.org/wiki/Dunham_expansion), solve for the transition energy (in wavenumbers).