# Annotated images

Split folders with files (e.g. images) into train, validation and test folders. 

Keeps the annotation data (if there are any) together with their images.  
Given the input folder in the following format:

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

Gives you this:

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

## Counting occurrences of tags
This package includes functions to count the occurrences of a tag in JSON and XML files.  
They can go through all files in a folder and count the occurrence of each tag on every (annotated) image.

## Install

```bash
pip install annotated-images
```

### Module

```python
import annotated_images

# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
annotated-images.split('input_folder', output="output", seed=1337, ratio=(.8, .1, .1))
```

```python
import annotated_images

# Returns total count of 'tag' found in all json files in 'path'
annotated-images.findTagsJson('path', 'tag')

# Returns total count of 'tag' found in all xml files in 'path'
annotated-images.findTagsXml('path', 'tag')
```

### Ref
this package is forked from https://github.com/jfilter/split-folders
