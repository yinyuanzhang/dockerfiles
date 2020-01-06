FROM mcr.microsoft.com/dotnet/core/sdk:3.0

COPY ./PFDSystem/ ./source/
RUN dotnet publish ./source/PFDSystem.csproj -c Release -o ./build/

WORKDIR ./build/

ENTRYPOINT dotnet PFDSystem.dll

