FROM mcr.microsoft.com/dotnet/core/aspnet:2.2 AS base

FROM mcr.microsoft.com/dotnet/core/sdk:2.2 AS build
#ARG SourceVersion
WORKDIR /src
COPY . .
# RUN sed -i "s/source-version/${SourceVersion}/g" /src/common.props
RUN dotnet restore && dotnet build -c Release --no-restore

FROM build AS publish
WORKDIR /build
RUN dotnet publish /src/src/Core.Private.Call.Web/Core.Private.Call.Web.csproj --no-build -c Release -o /build

FROM base
WORKDIR /app
COPY --from=publish /build .
ENV ConnectionStrings__Default=Server=192.168.0.252;Database=core_private_call;uid=postgres;pwd=postgres; \
    ConnectionStrings__BackgroundJob=192.168.0.252 \
    MessageQueue__HostName=192.168.0.252 \
    MessageQueue__ExchangeName=core.privatecall \
    MessageQueue__QueueName=core.privatecall \
    MessageQueue__VirtualHostName=/ \
    MessageQueue__UserName=guest \
    MessageQueue__Password=guest \
    MessageQueue__ServiceName=rabbitmq-5672 \
    MessageQueue__QueuePerConsumer=true \
    ServiceDiscovery__Registry=http://dev-consul:8500 \
    ServiceDiscovery__ServiceId= \
    ServiceDiscovery__ServiceName=core.privatecall \
    ServiceDiscovery__ServiceTags= \
    AutoMigrationEnabled=true \
    AutoSeedDisabled=false \
    ButterFlyServiceName=butterfly \
    BackgroundJob__Enabled=true \
    BackgroundJob__DashboardEnabled=true \
    BackgroundJob__QueuePollInterval=00:00:15 \
    BackgroundJob__WorkerCount=1 \
    BackgroundJob__UseRedis=true \
    BackgroundJob__RedisPrefix=core.privatecall \
    AXNProviderEndpoint=dyplsapi.aliyuncs.com \
    AXNProviderRegion=cn-hangzhou \
    AXNProviderAccount= \
    AXNProviderPassword= \
    ExceptCityName=哈尔滨 \
    IsRecordingEnabled=true \
    Expiration=2050-01-01 \
    FechRecordVoiceJobDelaySeconds=80000 \
    AutoBindingForBrokerOnDutyStatusChanged=true \
    AllowRestrictedOpreations=false
EXPOSE 80
ENTRYPOINT ["dotnet", "Core.Private.Call.Web.dll"]