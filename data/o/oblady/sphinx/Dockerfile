FROM python:2.7

MAINTAINER Jean Traullé <jean@oblady.fr>

RUN apt-get update                                                      && \
    apt-get install -y --no-install-recommends openjdk-7-jre graphviz   && \
    apt-get autoremove -y                                               && \
    rm -rf /var/cache/*                                                 && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install 'Sphinx                        == 1.3.6' \
                'alabaster                     == 0.7.7' \
                'sphinx-autobuild              == 0.6.0' \
                'sphinx_bootstrap_theme        == 0.4.9' \
                'sphinx-prompt                 == 1.0.0' \
                'sphinx_rtd_theme              == 0.1.9' \
                'sphinxcontrib-actdiag         == 0.8.5' \
                'sphinxcontrib-blockdiag       == 1.5.5' \
                'sphinxcontrib-nwdiag          == 0.9.5' \
                'sphinxcontrib-plantuml        == 0.7'   \
                'sphinxcontrib-seqdiag         == 0.8.5' \
                'livereload                    == 2.4.1'

ADD plantuml.jar /opt/plantuml.jar

ENV DOC_DIR /doc

VOLUME $DOC_DIR
WORKDIR $DOC_DIR

EXPOSE 8000

CMD sphinx-autobuild -H 0.0.0.0 -p 8000 . _build/html