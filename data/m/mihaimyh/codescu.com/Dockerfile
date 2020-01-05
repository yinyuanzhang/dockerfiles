FROM mcr.microsoft.com/dotnet/core/sdk:3.0-buster AS build
WORKDIR /src
COPY ["Codescu.Com.Wasm/Codescu.Com.Wasm.csproj", "Codescu.Com.Wasm/"]
RUN dotnet restore "Codescu.Com.Wasm/Codescu.Com.Wasm.csproj"
COPY . .

RUN dotnet build "Codescu.Com.Wasm/Codescu.Com.Wasm.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Codescu.Com.Wasm/Codescu.Com.Wasm.csproj" -c Release -o /app/publish

FROM nginx:alpine AS final
WORKDIR /usr/share/nginx/html
COPY --from=publish /app/publish/Codescu.Com.Wasm/dist .
COPY ["Codescu.Com.Wasm/nginx.conf", "/etc/nginx/nginx.conf"]