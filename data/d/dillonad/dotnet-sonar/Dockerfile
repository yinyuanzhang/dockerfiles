FROM mcr.microsoft.com/dotnet/core/sdk:2.2

RUN apt update
RUN apt install default-jdk -y
RUN dotnet tool install --global dotnet-sonarscanner
RUN echo export PATH=$PATH:/root/.dotnet/tools >> ~/.bashrc
RUN chmod 744 ~/.bashrc 

CMD [ "/bin/bash" ]