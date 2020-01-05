FROM mcr.microsoft.com/dotnet/core/runtime:2.1

FROM mcr.microsoft.com/dotnet/core/sdk:3.0
RUN apt-get update && apt-get install -y zip curl
COPY --from=0 /usr/share/dotnet/shared/Microsoft.NETCore.App/ /usr/share/dotnet/shared/Microsoft.NETCore.App/
RUN dotnet help && dotnet --list-runtimes