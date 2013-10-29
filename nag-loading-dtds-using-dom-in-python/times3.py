"Demonstrates how to expand XML entities using lxml instead of xml.dom.minidom."
import sys
from lxml import etree
sys.stdout.write(
    etree.tostring(
        etree.parse("times.xml", parser=etree.XMLParser(load_dtd=True)))
    + '\n')
