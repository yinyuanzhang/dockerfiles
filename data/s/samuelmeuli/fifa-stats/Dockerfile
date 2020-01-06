# Build Go app
FROM golang:1.11 AS go-build
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY src src/
RUN go build -o fifa-stats src/main.go

# Build React app
FROM node:11 AS react-build
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn
COPY public public/
COPY src src/
COPY .babelrc webpack.config.js ./
RUN yarn build

# Run app
FROM debian:stretch
WORKDIR /app
COPY --from=go-build /app/fifa-stats ./
COPY --from=react-build /app/dist ./dist/
CMD ["./fifa-stats", "server", "--db", "/app/db/fifa-stats.db", "--port", "80"]
