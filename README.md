# Split Folders

Split folders with files (e.g. images) into train, validation and test folders.

The input folder should have the following format:

```
input/
        img1.jpg
        img1.xml
        img1.json
        img1.*
        img2.jpg
        img2.xml
        img2.json
        img2.*
        ...
    ...
```

In order to give you this:

```
output/
    train/
        img1.jpg
        img1.xml
        img1.json
        img1.*
        ...
    val/
        img2.jpg
        img2.xml
        img2.json
        img2.*
        ...
    test/
        whatever.jpg
        whatever.xml
        whatever.json
        whatever.*
        ...
```
-   Works on any file types.
-   A [seed](https://docs.python.org/3/library/random.html#random.seed) lets you reproduce the splits.

## Install

```bash
pip install split-data
```

### Module

```python
import split-annotated-images

# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
split-annotated-images.ratio('input_folder', output="output", seed=1337, ratio=(.8, .1, .1)) # default values

# Split val/test with a fixed number of items e.g. 100 for each set.
# To only split into training and validation set, use a single number to `fixed`, i.e., `10`.
split-annotated-images.fixed('input_folder', output="output", seed=1337, fixed=(100, 100), oversample=False) # default values
```
