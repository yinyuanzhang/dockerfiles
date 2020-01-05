FROM mcr.microsoft.com/dotnet/core/sdk:2.1

RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -

RUN apt-get update -y \
    && apt-get install -y \
        nodejs \
        zip \
        make \
        python3 \
        python3-pip \
        python3-setuptools \
        groff \
        less \
    && pip3 install --upgrade pip \
    && apt-get clean

RUN npm install nswag redoc-cli serverless -g

RUN dotnet tool install -g Amazon.Lambda.Tools

ENV PATH="/root/.dotnet/tools:${PATH}"

RUN pip3 --no-cache-dir install --upgrade awscli

CMD ["/bin/bash"]