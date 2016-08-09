#!/usr/bin/env python3

from lxml import etree

def transform_xml(xml, xsl):
    dom = etree.fromstring(xml)
    xslt = etree.fromstring(xsl)
    transform = etree.XSLT(xslt)
    newdom = transform(dom)
    return etree.tostring(newdom, pretty_print=True)

# def transform_xml(xml, xsl):
#     dom = etree.parse('/Users/james/Desktop/bepress.xml')
#     xslt = etree.parse('/Users/james/Desktop/transform1.xsl')
#     transform = etree.XSLT(xslt)
#     newdom = transform(dom)
#     newdom.write('/Users/james/Desktop/test_out.xml', pretty_print=True)
#     return etree.tostring(newdom, pretty_print=True)




if __name__ == '__main__':
    with open('/Users/james/Desktop/bepress.xml', 'r') as xml:
        with open('/Users/james/Desktop/transform1.xsl', 'r') as xsl:
            print(transform_xml(xml.read(), xsl.read()))
