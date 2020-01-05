# ==================================== BASE ====================================
ARG INSTALL_PYTHON_VERSION=${INSTALL_PYTHON_VERSION:-3.7}
FROM python:${INSTALL_PYTHON_VERSION}-slim-stretch AS base
LABEL maintainer="Leonel Atencio<leonela@noritex.com>"

RUN apt-get update
RUN apt-get install -y \
    curl gcc build-essential g++ unixodbc-dev freetds-dev freetds-bin tdsodbc

ARG INSTALL_NODE_VERSION=${INSTALL_NODE_VERSION:-12}
RUN curl -sL https://deb.nodesource.com/setup_${INSTALL_NODE_VERSION}.x | bash -
RUN apt-get install -y \
    nodejs \
    && apt-get -y autoclean

COPY requirements requirements
RUN pip install -r requirements/prod.txt

COPY . /app
COPY package.json package.json22
RUN npm install

COPY supervisord.conf /etc/supervisor/supervisord.conf
COPY supervisord_programs /etc/supervisor/conf.d
COPY odbc/odbc.ini /etc/
COPY odbc/odbcinst.ini /etc/

EXPOSE 5000
EXPOSE 2992
ENTRYPOINT ["/bin/bash", "/app/shell_scripts/supervisord_entrypoint.sh"]
CMD ["-c", "/etc/supervisor/supervisord.conf"]