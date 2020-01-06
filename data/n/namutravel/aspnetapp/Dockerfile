FROM microsoft/dotnet:2.2-sdk AS build
WORKDIR /app



# copy csproj and restore as distinct layers
COPY *.sln .
COPY aspnetapp/*.csproj ./aspnetapp/
RUN dotnet restore

# copy everything else and build app
COPY aspnetapp/. ./aspnetapp/
WORKDIR /app/aspnetapp
RUN dotnet publish -c Release -o out


FROM microsoft/dotnet:2.2-aspnetcore-runtime AS runtime
WORKDIR /app
COPY --from=build /app/aspnetapp/out ./
ENTRYPOINT ["dotnet", "aspnetapp.dll"]
EXPOSE 2525




# FROM ubuntu:16.04

# Install dependencies
# RUN apt-get update
# RUN apt-get -y install apache2

# Install apache and write hello world message
# RUN echo 'Hello World!' > /var/www/html/index.html

# Configure apache
# RUN echo '. /etc/apache2/envvars' > /root/run_apache.sh
# RUN echo 'mkdir -p /var/run/apache2' >> /root/run_apache.sh
# RUN echo 'mkdir -p /var/lock/apache2' >> /root/run_apache.sh
# RUN echo '/usr/sbin/apache2 -D FOREGROUND' >> /root/run_apache.sh
# RUN chmod 755 /root/run_apache.sh



# CMD /root/run_apache.sh
