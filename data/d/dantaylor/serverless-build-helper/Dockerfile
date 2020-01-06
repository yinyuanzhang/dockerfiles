FROM microsoft/dotnet:2.1-sdk
RUN apt-get update -y \
    && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && apt-get install nodejs -y \
    && npm install -g serverless@latest \
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py; python get-pip.py \
    && pip install awscli \
    && dotnet tool install -g dotnet-xunit-to-junit
ENV PATH="$PATH:/root/.dotnet/tools"