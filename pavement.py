from paver.easy import *
from paver.setuputils import setup
from os import listdir
from os.path import isfile, join
import shutil
from jinja2 import Template, Environment, FileSystemLoader
import os
from weasyprint import HTML
from markdown2 import markdown_path
import locale
import datetime

HTMLFOLD='html/'
TMPFOLD='tmp/'
TMPFILE='tmp/arc.tmp'
PDFOUT = 'arc.pdf'
HTMLOUT = 'html/index.html'
WORKDIR = os.path.dirname(os.path.abspath(__file__))
# chose between styles, based on
# https://github.com/kxxoling/markdown2pdf/tree/master/markdown2pdf/themes
# valid styles = github/mou/ghostwriter/solarized-dark
STYLECSS = "css/github.css"
PAGECSS = "css/report.css"
#for l in locale.locale_alias:
#    try:
#        locale.setlocale(locale.LC_TIME, l)
#    except locale.Error: # the doc says setlocale should throw this on failure
#        pass
#    else:
#        print(l)
#loc = locale.setlocale(locale.LC_TIME, 'de_de')
templateVars = { "title" : "project name",
                 "version" : "V1",
                 "status" : "{ENTWURF/FREIGEGEBEN/...}",
                 "date": datetime.date.today(),
                 "watermark": "ENTWURF/VERAULICH",
                 "locale": "de",
                 "locale_long": "de_de"
                 }
def makePDF():
    html = markdown_path(TMPFILE, extras=["metadata", "tables", "footnotes"])
    relhtml = HTML(string=html, base_url=WORKDIR+"/"+HTMLFOLD)
    HTML(string=html, base_url=WORKDIR+"/"+TMPFOLD).write_pdf(PDFOUT, stylesheets=[PAGECSS, STYLECSS])

def makeHTML():
    html =""
    with open("res/htmlhead.tmpl") as infile:
        for line in infile:
            html+=line
    body = markdown_path(TMPFILE, extras=["metadata", "tables", "footnotes"])
    html += body
    with open("res/htmlfooter.tmpl") as infile:
        for line in infile:
            html+=line

    with open(HTMLOUT, 'w') as outfile:
        for line in html:
                outfile.write(line)
    jinja(HTMLOUT)  #a second time, needed.


@task
def init():
    clean()

@task
def clean():
    try:
        shutil.rmtree(TMPFOLD)
    except:
        # lets just assume the files were not present
        pass
    try:
        shutil.rmtree(HTMLFOLD)
    except:
        # lets just assume the files were not present
        pass
    try:
        os.remove(PDFOUT)
    except:
        # lets just assume the files were not present
        pass

def merge():
    pass

def write(this, to):
    with open(to, "w") as outfile:
        for line in this:
            outfile.write(line)

def jinja(this):
    # replace jinja variables
    j2_env = Environment(loader=FileSystemLoader(WORKDIR), trim_blocks=False)
    varedmd = j2_env.get_template(this).render(templateVars)
    os.remove(this)
    write(varedmd, this)

@task
def docs():
    if os.path.isfile(TMPFILE):
        clean()

    allfiles = listdir("md/")
    filenames = list()
    for f in allfiles:
        afile = "md/"+ f
        if isfile(afile):
            extension = os.path.splitext(afile)[1][1:]
            if extension == "md":
                filenames.append(afile)
    filenames.sort()

    shutil.copytree('md/images', TMPFOLD+"images")
    shutil.copytree('md/images', HTMLFOLD+"images")
    shutil.copy(STYLECSS, HTMLFOLD+"/style.css")
    shutil.copy(PAGECSS, HTMLFOLD+"/report.css")
    #merge documents to one
    with open(TMPFILE, 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)

    jinja(TMPFILE)
    makePDF()
    makeHTML()
