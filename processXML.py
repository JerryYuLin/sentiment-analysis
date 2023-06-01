import xml.etree.ElementTree as ET
import csv
from opencc import OpenCC

tree = ET.parse("Chinese_phones_training.xml")
root = tree.getroot()

with open("phones_training.csv", "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["text", "label"])
    cc = OpenCC("s2twp")

    for i in root.iter("sentence"):
        opinion = i.find("Opinions")
        polarity = 0
        if opinion != None:
            if opinion.find("Opinion").attrib["polarity"] == "positive":
                polarity = 1
            else:
                polarity = 2
        writer.writerow([cc.convert(i.find("text").text), polarity])
