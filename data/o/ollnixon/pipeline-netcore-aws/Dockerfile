FROM microsoft/dotnet:2.0.0-sdk

RUN apt-get update \
	&& apt-get install -y jq unzip
    
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" \
    && unzip awscli-bundle.zip \
    && ./awscli-bundle/install -b ~/bin/aws \
    && export PATH=~/bin:$PATH
