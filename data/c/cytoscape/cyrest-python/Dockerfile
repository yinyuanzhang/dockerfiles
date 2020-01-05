FROM ipython/scipyserver

MAINTAINER Keiichiro Ono <kono@ucsd.edu>

RUN apt-get install -y git
RUN pip install networkx bokeh requests py2cytoscape biopython

CMD ["/notebook.sh"]