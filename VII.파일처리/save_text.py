#234
# file = open('file.txt', 'w')
# 
# file.wirte('hello')
# file.write('월드')
# 
# file.close()

#234
# icecream = open("file.txt", 'a', encoding='utf-8')
#
# icecream.write('제니')
# icecream.write('\n')
# icecream.write('셀레나 사랑해')
# icecream.write('\n')
# icecream.close()

#xml
'''
<movie>
    <title>내안의 그놈</title>
    <genre>코미디</genre>
    <rating>5</rating>
</movie>
'''
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement

root = Element('movie')
title = SubElement(root, "title")
title.text = "트랜스포머"
genre = SubElement(root, "genre")
genre.text = "SF"
rating = SubElement(root, "rating")
rating.text = "8"

ET.ElementTree(root).write("movie.xml", encoding="utf-8", xml_declaration=True)
