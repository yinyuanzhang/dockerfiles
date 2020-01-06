FROM node:lts

# Install git
# RUN printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y git

# Install arma dependencies
RUN apt-get install -y lib32stdc++6

# Cleanup apt files
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Create application folder
RUN mkdir /app

# Create application user
RUN useradd -u 123 -U -s /bin/false arma && usermod -G users arma

# Download Arma Server Web Manager (Steam Workshop Branch)
RUN git clone -b feature/steam-workshop-mods-status --single-branch https://github.com/Dahlgren/arma-server-web-admin.git /app

# Install node dependencies for the application
WORKDIR /app
# RUN git reset --hard 56d12d5
RUN npm install

# Copy start application script
COPY start.sh /app/

# Start application
CMD ./start.sh

# Declare application port
EXPOSE 3000
