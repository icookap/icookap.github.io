# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source/
BUILDDIR      = ../docs/


# Internal variables.
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
SAMPLEOPTS      = -D html_theme=sample


default: html	
view:
	open ../docs/index.html

clean:
	-rm -rf $(BUILDDIR)

html:
	-rm -rf $(BUILDDIR)/*
	$(SPHINXBUILD) -t html -b html $(SOURCEDIR) $(BUILDDIR)
	echo "google.com, pub-1185612784580319, DIRECT, f08c47fec0942fa0" >> $(BUILDDIR)/app-ads.txt

