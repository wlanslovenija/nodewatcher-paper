DOCUMENT = main.pdf
TEXFILE = $(DOCUMENT:%.pdf=%.tex)
BIBFILE = bibliography/references.bib

all: $(DOCUMENT)

$(DOCUMENT): $(TEXFILE) $(BIBFILE)
	pdflatex -shell-escape -interaction=batchmode "$<"
	bibtex "$(<:%.tex=%.aux)"
	pdflatex -shell-escape -interaction=batchmode "$<"
	pdflatex -shell-escape -interaction=batchmode "$<"

clean:
	rm -f *.dvi *.0 *.log *.mpx *.mp *.aux *.lof *.lot *.toc main.pdf *.ptb *.brf *.bbl *.blg *.out mpxerr.tex *.spl

.PHONY: all clean

.SUFFIXES: .pdf .tex .bib
