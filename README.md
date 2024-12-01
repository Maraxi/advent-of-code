# Solutions for Advent of Code 2023

The script `setup` is called every day to create a new folder as a copy of
the folder `template`.

After the challenge begins the script `download` is used to download the
personal challenge input into the file `input.txt` for the current day.

Some common functions are already implemented for each day:
 * data load: The input file is read automatically split by newlines.
The result is provided in the variable `data`
 * task selection: The main for each day contains the variable config:
   * config == 1: run `solution1` on the data from `sample1.txt`
   * config == 2: run `solution1` on the proper input data `input.txt`
   * config == 3: run `solution2` on `sample2.txt` if it is not empty
     or `sample1.txt` instead
   * config == 4: run `solution2` on `input.txt`

# 2024
See <https://adventofcode.com/2024>.

