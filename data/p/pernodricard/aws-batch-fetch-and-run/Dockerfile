FROM python:3.6-stretch

# apt-get and system utilities
RUN apt-get update \
  && apt-get install -y --allow-unauthenticated awscli curl apt-utils apt-transport-https debconf-utils gcc build-essential g++ git r-base default-jre default-jdk \
  && rm -rf /var/lib/apt/lists/*

# adding custom MS repository
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list

# install SQL Server drivers
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated msodbcsql17=17.1.0.1-1 unixodbc-dev

# install SQL Server tools
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN /bin/bash -c "source ~/.bashrc"

# install SQL Server Python SQL Server connector module - pyodbc
RUN pip install pyodbc virtualenv

ADD fetch_and_run.sh /usr/local/bin/fetch_and_run.sh
RUN chmod 755 /usr/local/bin/fetch_and_run.sh

ENV REQUIREMENTS=''
ENV SCRIPT_PATH=''
ENV SCRIPT_NAME=''
ENV FUNCTION=''
ENV ARGS=''
ENV AWS_ACCESS_KEY_ID=''
ENV AWS_SECRET_ACCESS_KEY=''
ENV ID_RSA_BITBUCKET=''
ENV GIT_URL=''
ENV LANGUAGE=''

WORKDIR /tmp
ENTRYPOINT ["/usr/local/bin/fetch_and_run.sh"]
