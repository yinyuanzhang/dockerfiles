FROM node:11

WORKDIR /app

COPY package.json package.json
COPY package-lock.json package-lock.json
COPY service.js service.js
COPY install.js install.js
COPY build.js build.js
COPY favicons.js favicons.js
COPY icon.png icon.png
COPY feathers-gen-specs.json feathers-gen-specs.json
COPY api api
COPY client client
COPY config/default.json config/default.json
COPY config/production.json config/production.json
COPY public/icons public/icons

# to change this, add feahters-sync and a radis (of mongo if mustab is fixed by then) container
ENV WEB_CONCURRENCY 1
ENV NODE_ENV 'production'
ENV PORT 8080
ENV SITE_PROTOCOL 'https'
ENV SITE_DOMAIN 'domain.com'
ENV ALLOW_DATA_DOWNLOAD 'true'
# options below are off, all, and a comma seperated list of services to migrate
ENV DATA_MIGRATION 'off'
ENV MONGODB_URI 'mongodb://mongo:27017/database'
ENV DEPLOY_VERSION '0.0.1'
# Optional, MailChimp Key
ENV MAIL_CHIMP_KEY 'MAIL_CHIMP_KEY'
# Optional, Twilio ID and Token
ENV AC_TWILIO_ACCOUNT_SID 'AC_TWILIO_ACCOUNT_SID'
ENV TWILIO_AUTH_TOKEN 'TWILIO_AUTH_TOKEN'
# Required, which file system to use ('local' or 'aws', or 'both')
ENV UPLOADS_FILE_SYSTEM 'local'
# Optional, unless file system = 'aws' or 'both'
# Make sure to upload the logo.png and missing.jpg to the bucket
ENV AWS_ENDPOINT 'https://s3.ca-central-1.amazonaws.com'
ENV AWS_ACCESS_KEY_ID 'AWS_ACCESS_KEY_ID'
ENV AWS_ACCESS_KEY_SECRET 'AWS_ACCESS_KEY_SECRET'
ENV AWS_S3_BUCKET 'AWS_S3_BUCKET'
# email provider 'postmark' or 'mailer'
ENV EMAIL_SERVICE_PROVIDER 'EMAIL_SERVICE_PROVIDER'
# PostMarkApp Key
ENV POST_MARK_APP_KEY 'POST_MARK_APP_KEY'
# mailer
ENV MAILER_SMTP_HOST 'MAILER_SMTP_HOST'
ENV MAILER_SMTP_PORT 'MAILER_SMTP_PORT'
ENV MAILER_SMTP_USER 'MAILER_SMTP_USER'
ENV MAILER_SMTP_PASSWORD 'MAILER_SMTP_PASSWORD'

RUN npm install
RUN npm run docker-build
RUN rm -rf client
RUN npm prune --production

CMD ["node", "api/index.js"]
