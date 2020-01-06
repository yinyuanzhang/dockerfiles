FROM alpine

MAINTAINER tree

RUN apk --no-cache add git python py-setuptools build-base python2-dev vim
RUN git clone https://github.com/b03902043/bbqsql.git /opt/bbqsql
WORKDIR /opt/bbqsql
RUN sed -i -e 's/os.getlogin()/"root"/' bbqsql/menu/bbq_core.py  # avoid os.getlogin() error
RUN python setup.py install

CMD ["/bin/sh"]
