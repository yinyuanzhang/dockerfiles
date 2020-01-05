FROM node:10.13-alpine AS builder
WORKDIR /app
COPY . .
RUN npm install --silent
RUN npm run build

FROM node:10.13-alpine
RUN npm i --g serve
WORKDIR /app
COPY --from=builder /app/build .
CMD ["serve", "-p", "3000", "-s", "."]
