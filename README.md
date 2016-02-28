# arc42-paver
Paver project template for architecture documentation based on the arc42 template (s. [arc42.de](http://arc42.de)).
Inspired by [arc42-gradle](https://github.com/p-goetz/arc42-gradle),  [arc42-maven](https://github.com/p-goetz/arc42-maven) and [template-arc42](https://github.com/falkoschumann/template-arc42).

# Purpose
This paver project template contains pre-filled markdown files to document
software architecture based on the arc42 template. The markdown files can be
transformed to a single-paged HTML site with markdown2. Eventually, this html is
transformed to a PDF file by means of weasyprint.

This project allows you to take advantage of version control (e.g. git),
the use of the easy, and beloved markdown notation and the use of the markdown
editor you prefer. Also, continuous reporting should be possible by means
of external build systems.

# Notice
* Not ready for prime time, yet.
* ~~arc42 template has been adapted, slightly.~~
* `###### ` 6th heading is reserved as a little hack for page breaks.
* ~~template is written in `de`, translation should be no problem, though.~~
* template is available at [arc42.github.io](http://arc42.github.io)

# Usage
* Mac OS X make sure [homebrew](http://brew.sh) is installed and setup.
* Mac OS X make sure XCode is up-to-date `xcode-select --install`
* Mac OS X `brew install cairo pango gdk-pixbuf libxml2 libxslt libffi`
*  `virtualenv --system-site-packages -p python3 .env`
* `source .env/bin/activate`
* `pip install -r requirements.txt`
* `paver docs`

# Known Issues
* markdown formatting stuff. (e.g. quotes/code in PDF, multiline table entries, ...). This needs to be sort out in progress, contribution is very welcome.
* ~~internal links to `h1` elements have an offset of one page.~~

# TODO
* ~~apply jinja on report.css (e.g. for head/footline).~~
* style HTML generation.
* consider multipage HTML generation. Various pages provide a clearer browsing experience, when deployed.
* automatic TOC creation, or at least there should be a choice.
* V1? provide example.pdf.
* V1?+ plantuml integration, maybe?
* V1?+ [nomnom](https://github.com/skanaar/nomnoml) integration, maybe?
* V1?+ [umpel](http://cruise.eecs.uottawa.ca/umpleonline/download_eclipse_umple_plugin.shtml) integration, maybe?
* V1?+ logo(s) on cover page. Everyone loves logos!
* V1?+ render git log as history.
* V1?+ better traceability, e.g. by means of jinja or link_patterns.
