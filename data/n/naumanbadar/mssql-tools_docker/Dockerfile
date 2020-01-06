FROM naumanbadar/base:1.0

ENV ACCEPT_EULA=Y

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
&& curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee /etc/apt/sources.list.d/msprod.list \
&& apt-get update \
&& apt-get install -y mssql-tools \
&& echo "export PATH=$PATH:/opt/mssql-tools/bin" >> /root/.bashrc
