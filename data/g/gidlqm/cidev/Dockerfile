FROM mcr.microsoft.com/dotnet/core/sdk:2.1-bionic
CMD /bin/bash
RUN apt-get update
RUN apt-get --yes upgrade && apt-get --yes dist-upgrade
RUN apt-get --yes install curl wget
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/google-chrome.list
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee /etc/apt/sources.list.d/msprod.list
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
ENV ACCEPT_EULA=Y
RUN apt-get --yes install lighttpd net-tools w3c-markup-validator mssql-tools unixodbc-dev locales ca-certificates openjdk-11-jre-headless openjdk-11-jre google-chrome-stable apt-transport-https nodejs && \
    npm install -g lighthouse
RUN echo "en_US UTF-8" > /etc/locale.gen && locale-gen en_US.UTF-8 && export LANG=en_US.UTF-8 && export LANGUAGE=en_US:en && export LC_ALL=en_US.UTF-8

ADD https://sideshowbarker.net/nightlies/jar/vnu.jar /opt/

# Setup the locale
RUN locale-gen en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8

# Install mssql-tools
ENV PATH="/opt/mssql-tools/bin/:${PATH}"
