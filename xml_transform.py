#!/usr/bin/env python3

from lxml import etree
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

from flask_wtf import Form
from wtforms import StringField, TextField, TextAreaField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update({
  'SECRET_KEY': '6KI2Iei1iUkWxcNaeNkZjhuYiBTDGmX/j1bJRgj9zts',
})

app.config.from_envvar('XML_TRANSFORM', silent=True)

class XmlInputForm(Form):
      xml = TextAreaField('XML', validators=[DataRequired()])
      xsl = TextAreaField('XSL', validators=[DataRequired()])

def transform_xml(xml, xsl):
    dom = etree.fromstring(xml)
    xslt = etree.fromstring(xsl)
    transform = etree.XSLT(xslt)
    newdom = transform(dom)

    return etree.tostring(newdom,
                          pretty_print=True,
                          encoding='UTF-8',
                          xml_declaration=True).decode('UTF-8')

@app.route('/xml-transform', methods=['GET', 'POST'])
def index():
    return render_template('form.html', form=XmlInputForm())

@app.route('/submit-xml', methods=['GET', 'POST'])
def transform():
    form = XmlInputForm()
    if form.validate_on_submit():
        return render_template('results.html', xml=transform_xml(form.xml.data, form.xsl.data))

    return 'fail'
