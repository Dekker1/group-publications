# Group Publications

This script is intended to output the publications of a group of academics
from Google Scholar. The usage of this script is currently based on
[scholar.py](https://github.com/ckreibich/scholar.py).


## Usage

To use the script call it with a comma separated CSV file where each row
represents one academic as input. Each row of this file consists of a list of
author names, a column for their starting year, and a column for their leaving
year. `current` is the placeholder for the current year. For example see the
following file (`test.csv`):

```
"Jip J. Dekker",2016,current
"A Einstein","Albert Einstein",1800,2000
```

The script can then be called as `./group_publications.py test.csv`. It will
output all publication of author "Jip J. Dekker" from between 2016 and 2018 and
all publications of author "A Einstein" or "Albert Einstein" between 1800 and
2000. The output will be formatted as CSV.

## TODO:

This script should actually look at user pages instead. The results should be
more reliable.
