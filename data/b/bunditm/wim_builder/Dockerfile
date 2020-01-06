FROM node:8.15 as builder

RUN mkdir -p /app && chown -R node:node /app
WORKDIR /app
COPY package*.json /app/
USER node
RUN cd /app && npm install
COPY --chown=node:node . .
# CMD ["npm","run","build", "serveProd"]
RUN cd /app && npm run build --serveProd

# Build a small nginx image with static website
FROM nginx:alpine
RUN rm -rf /usr/share/nginx/html/*
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]