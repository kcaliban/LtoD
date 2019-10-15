# LtoD Converter
Converts any L-protein into its mirror-image D-form.

## Dependencies
* python3

## Installation
Simply clone this repository into a directory of your liking
```bash
cd ilikethisdirectory
git clone https://github.com/kcaliban/LtoD.git 
```
## Usage
To convert a whole directory of .PDB files
```bash
python3 LtoD.py infolder outfolder
```

To convert a single .PDB file
```bash
python3 LtoD.py infile outfile
```

## Notes
You can of course also use this tool to convert a D-protein to L, though it is advised against since most L structures are available from the Protein Data Bank.

## License
See LICENSE file
