FROM mcr.microsoft.com/mssql/server:2017-CU16-ubuntu

RUN wget -O /etc/apt/sources.list.d/mssql-server-2017.list https://packages.microsoft.com/config/ubuntu/16.04/mssql-server-2017.list \
    && export DEBIAN_FRONTEND=noninteractive ACCEPT_EULA=Y \
    && apt-get update \
    && apt-get install -y \
        mssql-server-fts \
        # mssql-server-is \
        # Integration Services is not working in Docker yet
        # https://github.com/Microsoft/mssql-docker/issues/213
    #&& LC_ALL=en_US.UTF-8 ACCEPT_EULA=Y /opt/ssis/bin/ssis-conf -n setup \
    #&& echo 'export PATH="$PATH:/opt/ssis/bin"' >> ~/.bashrc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists

## Locales
# RUN apt-get -y install locales \
#     && locale-gen en_US.UTF-8 \
#     && update-locale LANG=en_US.UTF-8
