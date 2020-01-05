FROM postgres

ENV POSTGRES_PASSWORD=arcadia
ENV POSTGRES_USER=arcadia
ENV POSTGRES_DB=arcadia
ENV DOTNET_CLI_TELEMETRY_OPTOUT 1
ENV ASPNETCORE_ENVIRONMENT Development

RUN apt-get update && apt-get install -y wget supervisor
RUN apt-get upgrade -y
RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.asc.gpg
RUN mv microsoft.asc.gpg /etc/apt/trusted.gpg.d/
RUN wget -q https://packages.microsoft.com/config/debian/9/prod.list
RUN mv prod.list /etc/apt/sources.list.d/microsoft-prod.list
RUN apt-get install -y apt-transport-https
RUN apt-get update
RUN apt-get install -y dotnet-sdk-2.2
RUN apt-get upgrade -y

RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY ./src /app
WORKDIR /app/DesktopSettings

RUN dotnet restore
RUN dotnet build

EXPOSE 5000
EXPOSE 5001

CMD ["/usr/bin/supervisord"]