FROM mcr.microsoft.com/dotnet/core/aspnet:3.0 AS base
COPY ./libwkhtmltox.so /usr/lib/
RUN apt-get update && apt-get install -yq --no-install-recommends libgdiplus \
fontconfig xfonts-utils fonts-wqy-microhei ttf-wqy-microhei fonts-wqy-zenhei \
ttf-wqy-zenhei && apt-get clean && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*
