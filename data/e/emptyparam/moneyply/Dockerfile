FROM microsoft/dotnet:latest
COPY . /app
WORKDIR /app

RUN ["dotnet", "restore"]
RUN ["dotnet", "build"]

EXPOSE 5050/tcp

ENV ASPNETCORE_URLS http://*5050
ENV ASPNETCORE_ENVIRONMENT docker

ENTRYPOINT ["dotnet", "run", "--server.urls", "http://0.0.0.0:5050"]