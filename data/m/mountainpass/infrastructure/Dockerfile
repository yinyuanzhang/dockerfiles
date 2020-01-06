FROM mountainpass/scaffold-node:alpine-latest

ENV TZ Australia/Sydney

HEALTHCHECK --interval=5s --timeout=5s --start-period=5s --retries=10 CMD ./healthcheck.js http://127.0.0.1:80

# Import project and gather dependencies
COPY --chown=nodejs:nodejs .npmrc ./
COPY --chown=nodejs:nodejs package*.json ./
RUN npm i --production && npm cache clear --force
COPY --chown=nodejs:nodejs . .
