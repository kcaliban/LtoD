#!/usr/bin/python3
""" Converts a PDB file in L to its D counterpart by inversing the
    x coordinate

    Copyright 2019 Fabian Krause
"""

import sys, os

def replstring(string, i, j, repl):
    """
    Replace everything in string between and including indices i and j with repl
    >>> replstring("abc", 0, 0, "c")
    'cbc'
    >>> replstring("abc def LOL jkl", 8, 10, "ghi")
    'abc def ghi jkl'
    """
    # Convert to list since strings are immutable
    strlist = list(string)
    # Delete characters between given indices
    for k in range(j - i + 1):
        del strlist[i] # i instead of k, since deleting an element makes list smaller

    # Insert new chars
    for l in range(len(repl)):
        strlist = strlist[:i + l] + [repl[l]] + strlist[i + l:]
    return "".join(strlist)

def convert(infile, outfile):
    with open(infile, "r") as old:
        # Iterate through lines
        oldlines = [line for line in old]
        # Open new file
        new = open(outfile, "w")
        for line in oldlines:
            newl = line
            # Only manipulate lines starting with ATOM or HETATM
            if (line[0:4] == "ATOM" or line[0:6] == "HETATM"):
                # Inverse X Coordinate
                x = - (float) (line[31 - 1 : 31 - 1 + 8])

                # + 7 instead of + 8 because stringrepl replaces
                # also chars at the indices
                newl = replstring(newl, 31 - 1, 31 - 1 + 7,
                                  ("%.3f" % x).rjust(8))
            new.write(newl)

        new.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 LtoD.py infolder outfolder"
                "\n       python3 LtoD.py infile outfile")
        sys.exit()

    if len(sys.argv) == 3:
        inp = sys.argv[1]
        outp = sys.argv[2]
        root, ext = os.path.splitext(inp)
        perc = 0
        i = 0
        if ext == ".pdb":
            convert(inp, outp)
        else:
            for (dirpath, dirnames, filenames) in os.walk(inp):
                leng = float(len(filenames))
                for fil in filenames:
                    i += 1
                    convert(os.path.join(dirpath, fil), os.path.join(outp,
                                os.path.basename(fil)[:-4] + "_D" + ".pdb"))
                    perc = int(i / leng * 100)
                    print(str(perc) + "%")
