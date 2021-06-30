#244 xml load
import xml.etree.ElementTree as ET
file = open('movie.xml', encoding ='utf-8')

data = file.read()

file.close()

tree = ET.ElementTree(ET.fromstring(data))
root = tree.getroot()
# print(root.tag)
for child in root:
    print(f'tag: {child.tag}, text: {child.text}')