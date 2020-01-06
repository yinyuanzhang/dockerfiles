FROM microsoft/dotnet:latest
COPY . /app
WORKDIR /app

RUN ["dotnet", "restore"]
RUN ["dotnet", "build"]

EXPOSE 8000/tcp

ENV ASPNETCORE_URLS http://*8000
ENV ASPNETCORE_ENVIRONMENT docker

ENTRYPOINT ["dotnet", "run", "--server.urls", "http://0.0.0.0:8000"]