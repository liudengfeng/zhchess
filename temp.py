import xml.etree.ElementTree as ET

tree = ET.parse('data/svgs/bA.svg')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)