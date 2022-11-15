#!/bin/env python3
import argparse
import os
import xml.sax

"""
    TESTING RESULTS:
        Source file content:
            <note>
              <to>Tove</to>
              <from>Jani</from>
              <heading>Reminder</heading>
              <body>Don't forget me this weekend!</body>
            </note>

        Destination file content:
            <message>
              <receiver>Tove</receiver>
              <sender>Jani</sender>
              <header>Reminder</header>
              <note>Don't forget me this weekend!</note>
            </message>
"""


class CustomHandler(xml.sax.ContentHandler):

    def __init__(self, conversion_config: dict) -> None:
        super().__init__()
        self.dest_file_content = ""
        self.conversion_config = conversion_config

    def startElement(self, name, attrs):
        if name in self.conversion_config:
            self.dest_file_content += f"<{self.conversion_config[name]}>"
        else:
            self.dest_file_content += f"<{name}>"

    def characters(self, content):
        self.dest_file_content += f"{content}"

    def endElement(self, name):
        if name in self.conversion_config:
            self.dest_file_content += f"</{self.conversion_config[name]}>"
        else:
            self.dest_file_content += f"</{name}>"


if __name__ == "__main__":
    # Parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="Path to *.xml file that needs to be changed")
    parser.add_argument("dest", help="Where modified *.xml file will be saved")
    args = parser.parse_args()

    # Arguments validation
    assert os.path.exists(args.source), "Given source file does not exist"
    assert os.path.isfile(args.source), "Given source is not a file"
    assert args.source.endswith(".xml"), "Given source is not *.xml file"

    dest_dirname = os.path.dirname(args.dest)
    if dest_dirname:   # In case destination file is placed in cwd
        assert os.path.exists(dest_dirname), "Path to destination file does not exist"
    assert args.dest.endswith(".xml"), "Destination is not *.xml file"

    # Creating conversion config
    conversion_config = {"to": "receiver",      # Structure {<tag existing in source file: str>: <tag that will replace previously given tag in dest file: str>}
                         "from": "sender",
                         "heading": "header",
                         "body": "note",
                         "note": "message"}

    # Parsing source *.xml file and converting it accordingly to conversion_config
    handler = CustomHandler(conversion_config)
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(args.source)

    # Creating new file and writting its content
    # As SAX is not able to edit *.xml files directly creating file and writting to it will be done in traditional way
    with open(args.dest, "w") as dest_file:
        dest_file.write(handler.dest_file_content)