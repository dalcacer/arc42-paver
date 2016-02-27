# arc42-paver
Paver project template for architecture documentation based on the arc42 template (s. [arc42.de](http://arc42.de)).
Inspired by [arc42-gradle](https://github.com/p-goetz/arc42-gradle) and [arc42-maven](https://github.com/p-goetz/arc42-maven).

# Purpose
This paver project template contains pre-filled markdown files to document
software architecture based on the arc42 template. The markdown files can then be transformed to a HTML site with markdown2, eventually this html is transformed to a PDF file by means of weasyprint.

This project allows you to take advantage of version control (e.g. git), the use of the easy, and beloved markdown notation and the use of the markdown editor in your favor. Also, a continuous reporting should be possible by means of build systems.

# Notice
* Not ready for prime time, yet.
* Template has been adapted, slightly.
* `###### ` 6th heading is reserved as a little hack for page breaks.

# Usage
* Mac OS X make sure [homebrew](http://brew.sh) is installed and setup.
* Mac OS X make sure XCode is up-to-date `xcode-select --install`
* Mac OS X `brew install cairo pango gdk-pixbuf libxml2 libxslt libffi`
*  `virtualenv --system-site-packages -p python3 .env`
* `source .env/bin/activate`
* `pip install -r requirements.txt`
* `paver docs`

# TODO
* apply jinja on report.css (e.g. for head/footline).
* style HTML generation.
* consider multipage HTML generation.
