FROM mcr.microsoft.com/dotnet/core/runtime:2.1-stretch-slim AS base
#FROM mcr.microsoft.com/dotnet/core/runtime:3.0-buster-slim AS base
WORKDIR /app
RUN apt-get update && apt-get -f install && apt-get -y install dumb-init locales wget gnupg2 apt-utils apt-transport-https --fix-missing
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \	
    && apt-get update\
    && apt-get install -y google-chrome-unstable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst ttf-freefont \
      --no-install-recommends \
	  --fix-missing \
    && rm -rf /var/lib/apt/lists/*
ENV PUPPETEER_EXECUTABLE_PATH "/usr/bin/google-chrome-unstable"
ENV PROXY_ENABLE {$PROXY_ENABLE}
ENV PROXY_SERVER {$PROXY_SERVER}
ENV PROXY_USER {$PROXY_USER}
ENV PROXY_PASS {$PROXY_PASS}
ENV PROXY_PORT {$PROXY_PORT}
ENV PROXY_SWITCH {$PROXY_SWITCH}
ENV TASK_FILE {$TASK_FILE}
ENV TASK_IP_SWITCH {$TASK_IP_SWITCH}
#RUN localedef -c -f UTF-8 -i zh_CN zh_CN.utf8
#ENV LANG zh_CN.utf8

FROM mcr.microsoft.com/dotnet/core/sdk:2.1-stretch AS build
#FROM mcr.microsoft.com/dotnet/core/sdk:3.0-buster AS build
WORKDIR /src
COPY BGS/BGS.csproj BGS/
RUN dotnet restore BGS/BGS.csproj
COPY . .
WORKDIR /src/BGS
RUN dotnet build BGS.csproj -c Release -o /app

FROM build AS publish
RUN dotnet publish BGS.csproj -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD dotnet BGS.dll ${params}