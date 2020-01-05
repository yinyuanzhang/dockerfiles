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
COPY ["AmrCloudAdminApi/AmrCloudAdminApi.csproj", "AmrCloudAdminApi/"]
COPY ["AmrCloudAdminDal/AmrCloudAdminDal/AmrCloudAdminDal.csproj", "AmrCloudAdminDal/AmrCloudAdminDal/"]
RUN dotnet restore "AmrCloudAdminApi/AmrCloudAdminApi.csproj"
COPY . .
WORKDIR "/src/AmrCloudAdminApi"
RUN dotnet build "AmrCloudAdminApi.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "AmrCloudAdminApi.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENV ASPNETCORE_ENVIRONMENT=Production
ENV ASPNETCORE_URLS http://+:5000
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezon
EXPOSE 5000
ENTRYPOINT ["dotnet", "AmrCloudAdminApi.dll"]