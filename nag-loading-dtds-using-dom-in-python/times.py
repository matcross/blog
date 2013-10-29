"Demonstrates how XML entities can disappear when using xml.dom.minidom."
import sys, xml.dom.minidom
sys.stdout.write(xml.dom.minidom.parse("times.xml").toxml())
