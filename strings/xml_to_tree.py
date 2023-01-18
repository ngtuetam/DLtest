import xml.etree.ElementTree as ET

xml_string = "<root><element>Value1</element><element>Value2</element></root>"

# Parse the XML string
root = ET.fromstring(xml_string)

# Traverse the tree
for element in root:
    print(element.tag, element.text)