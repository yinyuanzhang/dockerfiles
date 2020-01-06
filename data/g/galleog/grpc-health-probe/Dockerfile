FROM openjdk:8-jre-alpine

RUN apk add --no-cache curl
ARG GRPC_HEALTH_PROBE_VERSION=v0.3.0
RUN curl -L https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/$GRPC_HEALTH_PROBE_VERSION/grpc_health_probe-linux-amd64 -o /bin/grpc_health_probe && \
    chmod +x /bin/grpc_health_probe
