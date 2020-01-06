FROM mcr.microsoft.com/dotnet/core/sdk:2.2

RUN apt-get update && \
    apt-get install -y apt-transport-https curl software-properties-common zip

# prepare registry for azure func cli
RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.asc.gpg && \
    mv microsoft.asc.gpg /etc/apt/trusted.gpg.d/ && \
    wget -q https://packages.microsoft.com/config/debian/9/prod.list && \
    mv prod.list /etc/apt/sources.list.d/microsoft-prod.list

# install azure func cli
RUN apt-get update && apt-get install -y azure-functions-core-tools

# install nodejs
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    apt-get install -y nodejs

CMD bash