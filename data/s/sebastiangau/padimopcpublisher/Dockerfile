## MULTISTAGE BUILD DOCKERFILE
# this will do compilation and runtime image building based on docker
# therefore, you do not need to have the .net core SDK installed on your machine

FROM mcr.microsoft.com/dotnet/core/sdk:2.2 AS build-env
# set directory for following RUN, CMD, ENTRY, COPY
# builds the app in the /out folder in the build container
WORKDIR /out

# Copy csproj in build container and restore project dependencies/tools as distinct layers
COPY *.csproj ./
RUN dotnet restore

# copy remaining project files into the build container and run the dotnet compilation command
# the .dll will be copied to the /out dir in the build container
COPY . ./
RUN dotnet publish -c Release -o buildoutput

# Build runtime image
# copy from the /out dir in the build container to the root of the runtime container
FROM mcr.microsoft.com/dotnet/core/runtime:2.2
WORKDIR /
COPY --from=build-env /out/buildoutput .
ENTRYPOINT ["dotnet", "PADimOpcPublisher.dll"]