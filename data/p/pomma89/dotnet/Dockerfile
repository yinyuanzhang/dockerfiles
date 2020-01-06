FROM mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim

LABEL description="Docker images with .NET Core, based on Debian Linux."
LABEL maintainer="Alessio Parma <alessio.parma@gmail.com>"

# Use ports which do not require root user:
ENV PORT=8080
ENV SSH_PORT=2222
EXPOSE 8080 2222

# Tell ASP.NET to use a different port:
ENV ASPNETCORE_URLS=http://*:8080

# Azure App Service specific variables:
ENV WEBSITE_ROLE_INSTANCE_ID=localRoleInstance
ENV WEBSITE_INSTANCE_ID=localInstance

# Copy SSH configuration:
COPY ssh/sshd_config /etc/ssh/

# Copy init script:
COPY ./bash/aspnet_init.sh /usr/local/sbin/
RUN chmod 500 /usr/local/sbin/aspnet_init.sh

# Custom scripts:
COPY ./bash bash
RUN sh bash/common_setup.sh &&\
    sh bash/aspnet_security.sh &&\
    sh bash/aspnet_ssh.sh &&\
    sh bash/common_gdiplus.sh &&\
    sh bash/common_cleanup.sh &&\
    rm -rf bash
