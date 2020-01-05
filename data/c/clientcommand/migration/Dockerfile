FROM  microsoft/dotnet:2.2-sdk AS builder

# Run migrations.
WORKDIR /app
COPY . .

RUN dotnet publish ./src/Migration.App/Migration.App.csproj -c Release -o /out

WORKDIR /out

# To reduce filesize, since we won't be immediately deleting the container.
FROM scratch
FROM microsoft/dotnet:2.2-runtime

WORKDIR /app

COPY --from=builder /out .
COPY ./entrypoint.sh /app/entrypoint.sh

RUN chmod +x ./entrypoint.sh

VOLUME ["/app/db"]

ENTRYPOINT ["./entrypoint.sh"]
