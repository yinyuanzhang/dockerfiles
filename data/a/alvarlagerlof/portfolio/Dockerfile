# Stage 1 - Build
FROM node:8 as react-build
WORKDIR /app
RUN git clone https://github.com/alvarlagerlof/personal-portfolio.git /app
RUN npm install
RUN npm run build

# Stage 2 - nginx in production
FROM nginx:alpine
COPY --from=react-build /app/build /usr/share/nginx/html
