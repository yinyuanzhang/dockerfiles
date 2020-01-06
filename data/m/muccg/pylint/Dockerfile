#
FROM muccg/python-base:debian8-2.7
MAINTAINER ccg <devops@ccg.murdoch.edu.au>

RUN pip install "flake8==2.4.0"

VOLUME ["/data"]

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD /docker-entrypoint.sh
