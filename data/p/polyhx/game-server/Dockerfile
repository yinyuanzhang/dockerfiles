FROM microsoft/dotnet:2-sdk as dotnet-build
WORKDIR /dotnet/LHGames

COPY . .
WORKDIR LHGames/WebSocketAPI
RUN dotnet restore
RUN dotnet publish -c Release -o out

FROM microsoft/dotnet:2-runtime-jessie
WORKDIR /Volumes/LHGames
COPY --from=dotnet-build /dotnet/LHGames/LHGames/WebSocketAPI/out .
COPY --from=dotnet-build /dotnet/LHGames/LHGames/WebSocketAPI/game.conf .
ENTRYPOINT ["dotnet", "WebSocketAPI.dll"]
EXPOSE 4000
