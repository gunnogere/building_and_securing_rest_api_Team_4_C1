import argparse
import json
import xml.etree.ElementTree as ET
from pathlib import Path


def parse_sms_xml(xml_path: Path) -> list[dict[str, str]]:
    root = ET.parse(xml_path).getroot()
    return [sms.attrib.copy() for sms in root.findall("sms")]


def main() -> None:
    default_input = Path(__file__).with_name("modified_sms_v2-1.xml")
    default_output = Path(__file__).with_name("sms_records.json")

    parser = argparse.ArgumentParser(description="Convert an SMS XML backup to JSON.")
    parser.add_argument("xml_file", nargs="?", type=Path, default=default_input)
    parser.add_argument("--output", type=Path, default=default_output)
    args = parser.parse_args()

    records = parse_sms_xml(args.xml_file)
    args.output.write_text(
        json.dumps(records, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Converted {len(records)} SMS records to {args.output}")


if __name__ == "__main__":
    main()