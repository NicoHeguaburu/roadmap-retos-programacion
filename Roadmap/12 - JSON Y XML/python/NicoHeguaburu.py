import json
import xml.etree.ElementTree as xml
import os

name = "Nicolas Heguaburu"
age = 22
birth_date = "12:07:2002"
programming_lenguages = ["Python", "Javascript", "Typescript"]


data = {
    "name" : name,
    "age" : age,
    "birth_date" : birth_date,
    "programming_lenguages" : programming_lenguages
}

#xml

file_xml = "file.xml"
file_json = "file.json"

def save_xml():
    
    root = xml.Element("data")

    for key, value in data.items():
        child = xml.SubElement(root, key)
        child.text = str(value)

    tree = xml.ElementTree(root)
    tree.write(file_xml)

save_xml() 

with open (file_xml, "r") as xml_data:
    print(xml_data.read())

os.remove(file_xml)

#json

def save_json():
    with open(file_json, "w") as file:
        json.dump(data, file, indent = 4)

save_json()

with open(file_json, "r") as file:
    print(file.read())

os.remove(file_json)

save_xml()
save_json()

class Data:

    def __init__(self, name, age, birth_date, programming_lenguages):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_lenguages = programming_lenguages

    def __str__(self):
        return f"Data(name={self.name}, age={self.age}, birth_date={self.birth_date}, programming_lenguages={self.programming_lenguages})"



with open(file_xml, "r") as xml_data:

    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.find("age").text
    birth_date = root.find("birth_date").text
    programming_lenguages = root.find("programming_lenguages").text

    data_class_xml = Data(name, age, birth_date, programming_lenguages)
    print(data_class_xml)
    print(data_class_xml.name)

os.remove(file_xml)



with open(file_json, "r") as json_data:
    data = json.load(json_data)
    print(data)
    name = data["name"]
    age = data["age"]
    birth_date = data["birth_date"]
    programming_lenguages = data["programming_lenguages"]

    data_class_json = Data(name, age, birth_date, programming_lenguages)
    print(data_class_json)
    print(data_class_json.programming_lenguages)

os.remove(file_json)