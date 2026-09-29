import json
import xml.etree.ElementTree as ET
from pathlib import Path


def parse_sms_xml(xml_path):
    # Read the XML file and find the root element.
    root = ET.parse(xml_path).getroot()

    records = []
    for sms in root.findall("sms"):
        # Each SMS message stores its details as XML attributes.
        records.append(dict(sms.attrib))

    return records


def main():
    # Keep the input and output files in the same folder as this script.
    folder = Path(__file__).parent
    xml_file = folder / "modified_sms_v2-1.xml"
    json_file = folder / "sms_records.json"

    records = parse_sms_xml(xml_file)

    # Save the SMS dictionaries as a readable JSON list.
    with json_file.open("w", encoding="utf-8") as output_file:
        json.dump(records, output_file, indent=2, ensure_ascii=False)

    print(f"Converted {len(records)} SMS records to {json_file}")


if __name__ == "__main__":
    main()