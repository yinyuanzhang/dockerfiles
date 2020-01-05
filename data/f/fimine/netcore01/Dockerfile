FROM microsoft/aspnetcore:1.0.1
ARG source
WORKDIR /app
EXPOSE 8080
ENV ASPNETCORE_URLS http://*:8080
COPY out .
ENTRYPOINT ["dotnet", "ASPNETCORECORE.dll"]
