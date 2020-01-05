FROM sgrio/java-oracle:jdk_8

RUN apt-get update && apt-get install -y build-essential zip pciutils git ca-certificates
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && apt-get install -y nodejs
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get install -y yarn

RUN useradd tizen -m -U
USER tizen
RUN cd /home/tizen && curl -sS http://download.tizen.org/sdk/Installer/tizen-studio_1.2/web-cli_Tizen_Studio_1.2_ubuntu-64.bin > web-cli_Tizen_Studio_1.2_ubuntu-64.bin \
    && chmod +x web-cli_Tizen_Studio_1.2_ubuntu-64.bin
RUN cd /home/tizen && ./web-cli_Tizen_Studio_1.2_ubuntu-64.bin --accept-license /home/tizen/tizen-studio

ENV PATH="/home/tizen/tizen-studio/package-manager:/home/tizen/tizen-studio/tools/ide/bin:${PATH}"
RUN package-manager-cli.bin install NativeCLI
