#!/usr/bin/env python3

import os
from lxml import etree
from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
from flask_nav import Nav
from flask_nav.elements import Navbar, View

nav = Nav()

@nav.navigation()
def mynavbar():
    return Navbar(
        'XML Transform',
    )

app = Flask(__name__)
Bootstrap(app)
nav.init_app(app)

app.config.from_object(__name__)

app.config.update({
  'SECRET_KEY': os.environ.get('XML_TRANSFORM_SECRET_KEY'),
})

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
    form = XmlInputForm()

    if form.validate_on_submit():
        try:
            xml = transform_xml(form.xml.data, form.xsl.data)
        except Exception as e:
            flash('ERROR: {}'.format(str(e)))
            return render_template('form.html',
                                   form=XmlInputForm(),
                                   )

        return render_template('form.html',
                               form=XmlInputForm(),
                               xml=transform_xml(form.xml.data, form.xsl.data))

    return render_template('form.html',
                           form=XmlInputForm(),
                           )
