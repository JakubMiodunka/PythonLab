#!/bin/env python3
import argparse
import os
import xml.dom.minidom as minidom

"""
    TESTING RESULTS:
        Source file content:
            <note>
              <to>Tove</to>
              <from>Jani</from>
              <heading>Reminder</heading>
              <body>Don't forget me this weekend!</body>
            </note>

        Destination file content (aditonal XML header will be added):
            <?xml version="1.0" ?><note>
            <receiver>Tove</receiver>
            <sender>Jani</sender>
            <header>Reminder</header>
            <message>Don't forget me this weekend!</message>
            </note>
"""

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

    dest_basename = os.path.dirname(args.dest)
    if dest_basename:   # In case destination file is placed in cwd
        assert os.path.exists(dest_basename), "Path to destination file does not exist"
    assert args.dest.endswith(".xml"), "Destination is not *.xml file"

    # Creating conversion config
    conversion_config = {"to": "receiver",      # Structure {<tag existing in source file: str>: <tag that will replace previously given tag in dest file: str>}
                         "from": "sender",
                         "heading": "header",
                         "body": "note",
                         "note": "message"}

    # Parsing *.xml file to 'Document' type object
    xml_tree = minidom.parse(args.source)

    # Extracting root element 
    root = xml_tree.documentElement

    # Editing tags
    for _from, to in conversion_config.items():
        # Extracting all places with specyfied tag
        elements = root.getElementsByTagName(_from)

        # Editing tags
        for element in elements:
            element.tagName = to

    # Saving changes to destination file using 'Document' type object build-in method
    with open(args.dest, "w") as destination_file:
        xml_tree.writexml(destination_file)