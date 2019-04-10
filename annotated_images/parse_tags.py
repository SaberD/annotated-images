import json
import glob
import xml.etree.cElementTree as et

def findKeysJson(node, tag):
    """Find keys in Json object.

    Args:
        node (obj): JSON file object (with open(file) as json_file. json.load(json_file))
        tag  (str): tag to look for

    Returns:
        iterator: list(findKeysJson(node, tag))
    """
    if isinstance(node, list):
        for i in node:
            for x in findKeysJson(i, tag):
                yield x
    elif isinstance(node, dict):
        if tag in node:
            yield node[tag]
        for j in node.values():
            for x in findKeysJson(j, tag):
                yield x
                
def findTagsJson(path, tag):
    """Find tags in all Json files in a folder.

    Args:
        path (str): path to JSON files to look through
        tag  (str): tag to look for

    Returns:
        dict: dict with a count of each value found for the tag
    """
    files = glob.glob(path + "/*.json")
    count = dict()
    for file in files:
        with open(file) as json_file:  
            data = json.load(json_file)
            for label in list(findKeysJson(data, 'label')):
                try:
                    count[label] += 1
                except:
                    count[label] = 1
    return count

def findKeysXml(node, tag):
    """Find keys in XML object.

    Args:
        node (obj): XML file object (node=xml.etree.cElementTree.parse(file))
        tag  (str): tag to look for

    Returns:
        iterator: list(findKeysXml(node, tag))
    """
    for el in node.findall('*'):
        for ch in list(el):
            if ch.tag == tag:
                yield ch.text

def findTagsXml(path, tag):
    """Find tags in all Json files in folder.

    Args:
        path (str): path to XML files to look through
        tag  (str): tag to look for

    Returns:
        dict: dict with a count of each value found for the tag
    """
    files = glob.glob(path+"/*.xml")
    count = dict()
    
    for file in files:
        tree=et.parse(file)
        for label in list(findKeysXml(tree, tag)):
            try:
                count[label] += 1
            except:
                count[label] = 1
    return count