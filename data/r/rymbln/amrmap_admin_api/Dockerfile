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
COPY ["AmrmapAdminApi/AmrmapAdminApi.csproj", "AmrmapAdminApi/"]
COPY ["AmrmapAdminDAL/AmrmapAdminDAL.csproj", "AmrmapAdminDAL/"]
RUN dotnet restore "AmrmapAdminApi/AmrmapAdminApi.csproj"
COPY . .
WORKDIR "/src/AmrmapAdminApi"
RUN dotnet build "AmrmapAdminApi.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "AmrmapAdminApi.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENV ASPNETCORE_ENVIRONMENT=Production
ENTRYPOINT ["dotnet", "AmrmapAdminApi.dll"]