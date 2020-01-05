FROM wlniao/dotnet:deps2.0
MAINTAINER WlniaoStudio <wlniao@qq.com>

ADD ngrok /usr/bin/ngrok
RUN curl -SL https://dotnetcli.blob.core.windows.net/dotnet/Runtime/2.2.0/dotnet-runtime-2.2.0-linux-x64.tar.gz --output dotnet.tar.gz \
    && mkdir -p /usr/share/dotnet \
    && tar -zxf dotnet.tar.gz -C /usr/share/dotnet \
    && rm dotnet.tar.gz \
    && ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet \
	&& chmod 777 /usr/bin/ngrok

ONBUILD COPY . /wln
ONBUILD WORKDIR /wln