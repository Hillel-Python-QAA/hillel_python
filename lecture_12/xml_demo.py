import xml.etree.ElementTree as ET


# Завантаження XML-файлу
tree = ET.parse("data.xml")
root = tree.getroot()

# Читання та виведення даних з елементів XML-документу
for child in root:
    print(child.tag, child.attrib)
    for subchild in child:
        print(subchild.tag, subchild.text)

# Write to a file

# Створення кореневого елемента
root = ET.Element("data")

# Створення під-елементів та додавання їх до кореневого елемента
child1 = ET.SubElement(root, "child1")
child1.text = "Data 1"
child2 = ET.SubElement(root, "child2")
child2.text = "Data 2"

# Запис у XML-файл
tree = ET.ElementTree(root)
tree.write("output.xml")


# Finding in xml
# Завантаження XML-файлу
tree = ET.parse("data2.xml")
root = tree.getroot()

# Пошук елементу bbo у timingExbytes для кожної групи
for group in root.findall("group"):
    timing_exbytes = group.find("timingExbytes")
    if timing_exbytes is not None:
        bbo = timing_exbytes.find("bbo")
        if bbo is not None:
            print(f"Group: {group.find('name').text}, bbo: {bbo.text}")
        else:
            print(f"Group: {group.find('name').text}, bbo: Не знайдено")
