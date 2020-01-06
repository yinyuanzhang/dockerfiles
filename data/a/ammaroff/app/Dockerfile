FROM microsoft/dotnet:latest
# Create directory for the app source code
RUN mkdir -p /usr/src/warda
WORKDIR /usr/src/warda
# Copy the source and restore dependencies
COPY . /usr/src/warda
RUN dotnet restore
#RUN dotnet run
# Expose the port and start the app
EXPOSE 5000
CMD [ "dotnet", "run" ]
# nothing

