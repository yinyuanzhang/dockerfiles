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
COPY ["SpecialistApp/SpecialistApp.csproj", "SpecialistApp/"]
COPY ["SpecialistDAL/DAL.csproj", "SpecialistDAL/"]
RUN dotnet restore "SpecialistApp/SpecialistApp.csproj"
COPY . .
WORKDIR "/src/SpecialistApp"
RUN dotnet build "SpecialistApp.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "SpecialistApp.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENV ASPNETCORE_ENVIRONMENT=Production
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezon
ENTRYPOINT ["dotnet", "SpecialistApp.dll"]