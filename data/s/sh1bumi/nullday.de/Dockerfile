FROM debian:buster-slim AS build
# Set Hugo Version
ENV HUGO_VERSION=0.59.1
# Copy hugo project into container
COPY . /app
# Get Hugo and Caddy
ADD https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz /tmp/
ADD https://github.com/caddyserver/caddy/releases/download/v2.0.0-beta9/caddy2_beta9_linux_amd64 /tmp/
# Install Hugo and Caddy
RUN tar -xf /tmp/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz -C /usr/bin/
RUN install -Dm755 /tmp/caddy2_beta9_linux_amd64 /usr/local/bin/caddy
# Generate static website
RUN hugo --minify --source=/app/

# Use Alpine as small base image for release container
FROM scratch AS release
# Copy all necessary things from build to release container
COPY --from=build /app/public /app/public
COPY --from=build /usr/local/bin/caddy /usr/local/bin/caddy
# Use user 9999 here and an unrestricted port
USER 9999:9999
EXPOSE 8080
# Call caddy when the container is started and serve the hugo project
ENTRYPOINT ["/usr/local/bin/caddy"]
CMD ["file-server", "-root", "/app/public/", "-listen", "0.0.0.0:8080"]
