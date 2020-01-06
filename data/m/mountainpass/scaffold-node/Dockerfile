FROM mountainpass/scaffold-node:alpine-latest

ENV TZ Australia/Sydney
ENV DB_SCRIPTS /database

# Import project and gather dependencies
COPY --chown=nodejs:nodejs .npmrc ./
COPY --chown=nodejs:nodejs package*.json ./
RUN npm i --production && npm cache clear --force
COPY --chown=nodejs:nodejs . .
