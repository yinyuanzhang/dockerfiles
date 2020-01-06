FROM mcr.microsoft.com/dotnet/core/sdk:3.1.100-preview1-buster AS build
WORKDIR /src
COPY ["BlazeDesk.Web.Wasm/BlazeDesk.Web.Wasm.csproj", "BlazeDesk.Web.Wasm/"]
COPY ["BlazeDesk.Web.UI.Lib/BlazeDesk.Web.UI.Lib.csproj", "BlazeDesk.Web.UI.Lib/"]
RUN dotnet restore "BlazeDesk.Web.Wasm/BlazeDesk.Web.Wasm.csproj"
COPY . .

RUN dotnet build "BlazeDesk.Web.Wasm/BlazeDesk.Web.Wasm.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "BlazeDesk.Web.Wasm/BlazeDesk.Web.Wasm.csproj" -c Release -o /app/publish

FROM nginx:alpine AS final
WORKDIR /usr/share/nginx/html
COPY --from=publish /app/publish/BlazeDesk.Web.Wasm/dist .
COPY --from=publish /app/publish/wwwroot .
COPY ["BlazeDesk.Web.Wasm/nginx.conf", "/etc/nginx/nginx.conf"]