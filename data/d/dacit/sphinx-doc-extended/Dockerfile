FROM jonatkinson/python-poetry:3.7

RUN apt-get update && apt-get install pandoc -y

# Install base python deps
RUN pip install 'ipython == 7.5.0'\
                'torch == 1.1.0'\
                'numpy == 1.16'
# Install official sphinx stuff
RUN pip install 'sphinx == 2.1.2'\
                'sphinxcontrib-apidoc == 0.3.0'\
                'sphinxcontrib-bibtex == 0.4.2'
# Install third party pdeps
RUN pip install 'better-apidoc == 0.3.1'\
                'sphinx-materialdesign-theme == 0.1.11'\
                'recommonmark == 0.5.0'\
                'nbsphinx == 0.4.2'\
                'nbsphinx-link == 1.2.0'
