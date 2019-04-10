import json
import glob
import xml.etree.cElementTree as et

def findKeysJson(node, tag):
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
    for el in node.findall('*'):
        for ch in list(el):
            if ch.tag == tag:
                yield ch.text

def findTagsXml(path, tag):
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