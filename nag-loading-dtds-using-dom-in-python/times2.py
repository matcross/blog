"""
Demonstrates how to expand XML entities using xmllint before a call to
xml.dom.minidom.
"""
import sys, xml.dom.minidom
with open("times_expanded.xml", "w") as cmd_fo:
    import os, subprocess
    subprocess.call("xmllint --loaddtd --noent " +
                    "times.xml",
                    shell=True,
                    stdout=cmd_fo,
                    stderr=sys.stderr,
                    close_fds=(os.name=='posix'),
                    universal_newlines=True)
sys.stdout.write(xml.dom.minidom.parse("times_expanded.xml").toxml())
