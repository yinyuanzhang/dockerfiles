# Stage 1: The development stage:
FROM microsoft/dotnet:sdk AS development

ENV HOME=/app NUGET_PACKAGES=/usr/nuget/packages

WORKDIR /app

COPY ./MvcMovie.csproj /app/

# If I where to include another executable not available
# on apt-get... I can copy it from an existing image!
# COPY --from=icalialabs/wkhtmltopdf:latest /bin/wkhtmltopdf /bin/wkhtmltopdf

RUN dotnet restore

# Stage 2: The Builder stage:
# This is the stage where the app code gets compiled.
FROM development AS builder

COPY . /app/

RUN dotnet publish --configuration Release

# Stage 3: The deployable stage:
FROM microsoft/dotnet:runtime AS deployable

COPY --from=builder /app/bin/Release/netcoreapp2.0/publish /app

# If I where to include another executable not available
# on apt-get... I can copy it from an existing image!
# COPY --from=icalialabs/wkhtmltopdf:latest /bin/wkhtmltopdf /bin/wkhtmltopdf

WORKDIR /app

CMD ["dotnet", "MvcMovie.dll"]
