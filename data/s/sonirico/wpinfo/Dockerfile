# Build and install packages
FROM sonirico/wpoke:latest as build-python

RUN apk add --update --no-cache gcc g++ nodejs npm;

# Install Python deps
COPY requirements.lock /build/app/
WORKDIR /build/app
RUN pip install --no-cache-dir -r requirements.lock

# Build static assets
FROM node:10 as build-nodejs
COPY . /build/app/
WORKDIR /build/app/frontend
RUN npm ci && npm run build --production

# Final stage
FROM python:3.7.4-alpine3.10

RUN apk add --update --no-cache libxml2-dev libxslt-dev

WORKDIR /app/

COPY config/ /app/config
COPY wpinfo/ /app/wpinfo
COPY app.py /app/app.py

COPY --from=build-python /usr/local/lib/python3.7/site-packages/ /usr/local/lib/python3.7/site-packages/
COPY --from=build-nodejs /build/app/wpinfo/templates/ /app/wpinfo/templates/
COPY --from=build-nodejs /build/app/wpinfo/static/bundles /app/wpinfo/static/bundles

ENV STATIC_URL ${STATIC_URL:-/static/}
EXPOSE 5000
RUN addgroup -S wpinfo && adduser -S -g wpinfo wpinfo
RUN chown -R wpinfo.wpinfo /app/

ENV PYTHONUNBUFFERED 1
ENV CONFIG "deploy"

ENTRYPOINT [ "python", "app.py" ]
