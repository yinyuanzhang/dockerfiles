# ---- Sources ----
FROM node:carbon AS base
WORKDIR /app
COPY package*.json /app/

# ---- Dependencies ----
FROM base AS dependencies
RUN npm install

# ---- Build ----
FROM dependencies AS build  
COPY src /app/src/
COPY public /app/public/
RUN npm run build

# --- Release with Alpine
FROM nginx:alpine AS release
COPY --from=build /app/build /usr/share/nginx/html/
