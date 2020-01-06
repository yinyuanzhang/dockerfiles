# Installs E-Cell3 with IPython Notebook
# Another Docker container should build from this one to get services like the notebook

FROM naito/ecell3-ipython

MAINTAINER Yasuhiro Naito <ynaito@e-cell.org>

EXPOSE 8888

ADD notebook.sh /
RUN chmod u+x /notebook.sh

CMD ["/notebook.sh"]
