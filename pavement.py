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
import re


# customize the following attributes
# chose between styles, based on
# https://github.com/kxxoling/markdown2pdf/tree/master/markdown2pdf/themes
# valid styles = github/mou/ghostwriter/solarized-dark
STYLECSS = "css/github.css"
templateVars = { "title" : "project name",
                 "version" : "V1",
                 "status" : "{ENTWURF/FREIGEGEBEN/...}",
                 "date": datetime.date.today(),
                 "watermark": "ENTWURF/VERTRAULICH",
                 "headline": "Architekturdokumentation project name V1",
                 "locale": "de",
                 "locale_long": "de_de"
                 }
# do not touch this
PAGECSS = "css/report.css"
WORKDIR = os.path.dirname(os.path.abspath(__file__))
TMPCSS = "tmp/report.css"
HTMLFOLD='html/'
TMPFOLD='tmp/'
TMPFILE='tmp/arc.tmp'
PDFOUT = 'arc.pdf'
HTMLOUT = 'html/index.html'
MDFOLD = "md/"
PATTERNS=[(re.compile(r'((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)'),r'\1')]
#https://github.com/trentm/python-markdown2/wiki/Extras
MDEXTRAS = ["metadata", "tables", "footnotes", "fenced-code-blocks", 'cuddled-lists', 'header-ids', 'link-patterns']

def makePDF():
    html = markdown_path(TMPFILE, extras=MDEXTRAS, link_patterns=PATTERNS)
    relhtml = HTML(string=html, base_url=WORKDIR+"/"+HTMLFOLD)
    HTML(string=html, base_url=WORKDIR+"/"+TMPFOLD).write_pdf(PDFOUT, stylesheets=[TMPCSS, STYLECSS])

def makeHTML():
    html =""
    with open("res/htmlhead.tmpl") as infile:
        for line in infile:
            html+=line
    body = markdown_path(TMPFILE, extras=MDEXTRAS, link_patterns=PATTERNS)
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

    ## find all md files within folder md
    allfiles = listdir(MDFOLD)
    filenames = list()
    for f in allfiles:
        afile = MDFOLD + f
        if isfile(afile):
            extension = os.path.splitext(afile)[1][1:]
            if extension == "md":
                filenames.append(afile)
    filenames.sort()

    # copy temporary ressources to tmp
    shutil.copytree(MDFOLD+'images', TMPFOLD+"images")
    shutil.copy(PAGECSS, TMPFOLD+"/report.css")
    jinja(TMPCSS)

    # copy ressources to html
    shutil.copytree(MDFOLD+'/images', HTMLFOLD+"images")
    shutil.copy(STYLECSS, HTMLFOLD+"/style.css")
    shutil.copy(PAGECSS, HTMLFOLD+"/report.css")
    jinja(HTMLFOLD+"/report.css")

    # merge all md documents to one
    with open(TMPFILE, 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
    jinja(TMPFILE)

    makePDF()
    makeHTML()
