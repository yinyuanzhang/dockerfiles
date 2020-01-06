FROM mhart/alpine-node:latest

WORKDIR /app
COPY . .

RUN apk add --no-cache wget curl tar

# Install Swagger Combine
RUN npm config set unsafe-perm true
RUN npm install -g swagger-combine

# Install Prism
RUN wget -O /usr/bin/prism https://github.com/stoplightio/prism/releases/download/v0.6.21/prism_linux_amd64
RUN chmod +x /usr/bin/prism

# Combine Swagger Files
RUN swagger-combine swagger.yaml -o /app/combined/swagger.yaml

# Start Prism Mock Server
EXPOSE 4010
CMD ["prism", "run", "--cors", "--list", "--config", "./config.json", "--spec", "/app/combined/swagger.yaml"]
