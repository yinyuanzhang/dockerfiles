FROM mcr.microsoft.com/dotnet/core/aspnet:2.2 AS base
RUN useradd -u 555 dockerapp\
    && mkdir /home/dockerapp\
    && mkdir /home/dockerapp/app \
    && mkdir /home/dockerapp/data \
    && mkdir /home/dockerapp/cashe \
    && chown -R dockerapp:dockerapp /home/dockerapp  \
    && addgroup dockerapp staff
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/core/sdk:2.2 AS build
WORKDIR /src
COPY ["AidaWebApi/AidaWebApi.csproj", "AidaWebApi/"]
COPY ["AidaDAL/AidaDAL/AidaDAL.csproj", "AidaDAL/AidaDAL/"]
RUN dotnet restore "AidaWebApi/AidaWebApi.csproj"
COPY . .
WORKDIR "/src/AidaWebApi"
RUN dotnet build "AidaWebApi.csproj" -c Release --runtime ubuntu.14.04-x64 -o /app

FROM build AS publish
RUN dotnet publish "AidaWebApi.csproj" -c Release --runtime ubuntu.14.04-x64 -o /app

FROM base AS final
RUN apt-get update && apt-get install -y --no-install-recommends zlib1g fontconfig libfreetype6 libx11-6 libxext6 libxrender1
RUN apt-get install -y apt-utils
RUN apt-get install -y libgdiplus
RUN ln -s /usr/lib/libgdiplus.so /usr/lib/gdiplus.dll
RUN apt-get install -y libc6-dev
WORKDIR /app
COPY --from=publish /app .
ENV ASPNETCORE_ENVIRONMENT=Production
RUN chmod 555 libwkhtmltox.so
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezon
ENTRYPOINT ["dotnet", "AidaWebApi.dll"]