# NOTE: Multi-stage Build

FROM node:10.16-alpine as build

COPY . /build

# Move to /build
WORKDIR /build

# Install requirements and build
RUN npm install && \
    npm run build


FROM node:10.16-alpine

LABEL maintainer="Ryo Ota <nwtgck@gmail.com>"

# Install tini
RUN apk add --no-cache tini

# Install bytenode globally
RUN npm install -g bytenode

# Copy compiled jsc to /app
COPY --from=build /build/dist/index.jsc /app/index.jsc

# Run a server
ENTRYPOINT [ "tini", "--", "bytenode", "/app/index.jsc" ]
