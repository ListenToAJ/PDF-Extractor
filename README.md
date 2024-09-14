# PDF Extractor

This is a simple Python script I made using the pypdf library in order to remove specific pages of a pdf.

## Description

One of my professors gave us our weekly homework in the form of one question per slide, intermittently spaced in between different concepts.  This ended up making accomplishing homework time consuming as anytime I would check the notes, finding the original problem was difficult.  I created this script with the pypdf library to read ina pdf, parse through each slide and look for the existence of some search query, and output a resulting new pdf only containing those pages.

## Getting Started

### Dependencies

* Within the included python env directory, is the pypdf library.  That is all thats needed.

### Installing
  
* Honestly, your best bet would be to copy and paste the Python script.  It's a single file that isn't long.

### Executing program

* The search query included is the one used for my homework, but it can be easily modified.
```
python3 hwExtractor.py "fileToBeShortened.pdf"
```

## Authors

ListenToAJ


## Version History

* 0.1
    * Initial Release

## License

This isn't liscened, come on man it's like 14 lines of code.

## Acknowledgments

* [README-Template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
* [GeeksforGeeks](https://www.geeksforgeeks.org/working-with-pdf-files-in-python/)