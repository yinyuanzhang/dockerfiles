
FROM c3h3/oblas-py278-scipy-base

RUN pip install ipython pyzmq jinja2 tornado
RUN mkdir ipynbs

WORKDIR ipynbs
CMD ipython notebook --no-browser --ip=0.0.0.0 --port 8888

