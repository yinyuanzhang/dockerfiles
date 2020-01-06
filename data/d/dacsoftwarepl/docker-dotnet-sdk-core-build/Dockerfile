# Build image
FROM microsoft/dotnet:2.1-sdk AS builder

LABEL version="1.0"
LABEL owner="DAC Software pl"
LABEL maintainer="pawel.kasperek@dacsoftware.pl"
LABEL organization="dacsoftwarepl"
LABEL description="Image with .NET SDK to build and test "

WORKDIR /app

# This defines the `ARG` inside the build-stage
# that the value is set to what's currently build configuration
ONBUILD ARG BUILD_CONFIGURATION
# If BUILD_CONFIGURATION is set/non-empty, use it, otherwise use a default value
ONBUILD ARG CONFIGURATION=${BUILD_CONFIGURATION:-Release}

# This defines the `ARG` inside the build-stage
# that the value is set to what are NuGet packages reporotories URLs
ONBUILD ARG BUILD_FEED
# If BUILD_FEED is set/non-empty, use it, otherwise use a default value
ONBUILD ARG FEED=${BUILD_FEED:-'--source "https://api.nuget.org/v3/index.json"'}

ONBUILD COPY ./*.sln ./NuGet.config ./*.props-server ./*.props ./*.targets  ./

# Copy the main source project files
ONBUILD COPY src/*/*.csproj ./
ONBUILD RUN for file in $(ls *.csproj); do mkdir -p src/${file%.*}/ && mv $file src/${file%.*}/; done

# Copy the test project files
ONBUILD COPY tests/*/*.csproj ./
ONBUILD RUN for file in $(ls *.csproj); do mkdir -p tests/${file%.*}/ && mv $file tests/${file%.*}/; done

# Restore packages from Nuget and private Nuget repositories
ONBUILD RUN dotnet restore /p:Configuration=${CONFIGURATION} ${FEED}

ONBUILD COPY ./tests ./tests
ONBUILD COPY ./src ./src

# This defines the `ARG` inside the build-stage (it will be executed after `FROM`
# in the child image, so it's a new build-stage). Don't set a default value so that
# the value is set to what's currently set for `BUILD_VERSION`
ONBUILD ARG BUILD_VERSION
# If BUILD_VERSION is set/non-empty, use it, otherwise use a default value
ONBUILD ARG VERSION=${BUILD_VERSION:-1.0.0}

# Build .NET services
ONBUILD RUN dotnet build /p:Version=$VERSION /p:Configuration=$CONFIGURATION

# Test .NET services
ONBUILD RUN find ./tests -name '*.csproj' -print0 | xargs -L1 -0 dotnet test --no-build --no-restore /p:Version=$VERSION /p:Configuration=${CONFIGURATION}