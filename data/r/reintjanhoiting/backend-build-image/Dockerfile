FROM microsoft/dotnet:sdk

RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl python build-essential git ca-certificates zip
RUN mkdir /nodejs && curl https://nodejs.org/dist/v10.9.0/node-v10.9.0-linux-x64.tar.gz | tar xvzf - -C /nodejs --strip-components=1

ENV PATH $PATH:/nodejs/bin
