import xml.dom.minidom as minidom


xml_file = open('currency.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
N_Code = []
C_Code = []

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'NumCode':
                if child.firstChild.nodeType == 3:
                    N_Code.append(child.firstChild.data)
            if child.tagName == 'CharCode':
                if child.firstChild.nodeType == 3:
                    C_Code.append(child.firstChild.data)


print(N_Code)
print(C_Code)

xml_file.close()