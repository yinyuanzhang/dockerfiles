FROM microsoft/aspnetcore:2.0

EXPOSE 80/tcp

ENV RUN_DLL="MyApp.dll"

WORKDIR /app

ENTRYPOINT ["dotnet", $RUN_DLL]
