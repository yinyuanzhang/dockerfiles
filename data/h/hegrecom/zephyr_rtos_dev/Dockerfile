FROM hegrecom/zephyr_rtos_dev:default

# Install Zephyr-SDK
RUN wget https://github.com/zephyrproject-rtos/meta-zephyr-sdk/releases/download/0.9.5/zephyr-sdk-0.9.5-setup.run
RUN sh zephyr-sdk-0.9.5-setup.run
RUN echo "export ZEPHYR_TOOLCHAIN_VARIANT=zephyr\nexport ZEPHYR_SDK_INSTALL_DIR=/opt/zephyr-sdk" >> $HOME/.zephyrrc

# Configure Development Environments
RUN curl --request GET --header 'PRIVATE-TOKEN: oXdfZrNyWDEM1kB7HkmY' \
'https://gitlab.com/api/v4/projects/9451060/repository/files/development_settings.sh/raw?ref=master' \
| bash
