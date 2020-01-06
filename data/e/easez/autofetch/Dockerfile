 FROM mcr.microsoft.com/dotnet/core/sdk AS build-env
WORKDIR /app

# Copy csproj and restore as distinct layers
COPY ./api/*.csproj ./
RUN dotnet restore

# Copy everything else and build
COPY ./api ./
RUN dotnet publish -c Release -o out

# Build runtime image
FROM mcr.microsoft.com/dotnet/core/aspnet:2.2
WORKDIR /app
COPY --from=build-env /app/out .

#Prep api database
COPY ./api/migration_autofetchDB.sqlite /app/migration_autofetchDB.sqlite

#Add nginx and Ember
# Ember must be build ahead of time
RUN apt-get update && apt-get install -y nginx cron
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./cli/dist /var/www/html/

#Install cron job
RUN echo "* * * * * root bash curl -X POST http://localhost:2912/api/autofetch\n" >> /etc/cron.d/autofetchCron
RUN chmod 0644 /etc/cron.d/autofetchCron
RUN crontab /etc/cron.d/autofetchCron

#Copy entrypoint script
COPY ./entrypoint.sh /usr/bin/docker-entrypoint.sh
RUN chmod +x /usr/bin/docker-entrypoint.sh
ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]