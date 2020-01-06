FROM microsoft/dotnet:2.2-sdk AS build
COPY . .
WORKDIR /src/Nymezide.VkStreamers.WebApi
RUN dotnet restore
RUN dotnet build --no-restore -c release /nowarn:CS1591

FROM build AS publish
RUN dotnet publish --no-restore -c Release -o /app

# Build runtime image
FROM microsoft/dotnet:2.2-aspnetcore-runtime as base
WORKDIR /app
EXPOSE 80

FROM base AS final
WORKDIR /app
COPY --from=publish /app .

# Assembly name is the same as the project name
ENTRYPOINT ["dotnet", "Nymezide.VkStreamers.WebApi.dll"]