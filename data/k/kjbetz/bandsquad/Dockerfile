FROM microsoft/dotnet:2.1.302-sdk-alpine3.7 AS builder

WORKDIR /app

COPY SocialMediaAggregator.csproj .
RUN dotnet restore

COPY . .
RUN dotnet publish -c Release -o published -r linux-musl-x64


FROM microsoft/dotnet:2.1.1-runtime-deps-alpine3.7

WORKDIR /app
COPY --from=builder /app/published . 

ENV ASPNETCORE_ENVIRONMENT Production
EXPOSE 5000
CMD [ "./SocialMediaAggregator" ]
