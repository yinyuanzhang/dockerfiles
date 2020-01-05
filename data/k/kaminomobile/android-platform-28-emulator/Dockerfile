# ====================================================================== #
# Android SDK Docker Image
# ====================================================================== #

# Base image
# ---------------------------------------------------------------------- #
FROM kaminomobile/android-platform-28:latest

# Author
# ---------------------------------------------------------------------- #
LABEL blazsolar "blaz@kamino.si"

USER root

# deps 
RUN apt-get update -y && \
	apt-get install qemu-kvm gosu -y

RUN usermod -aG kvm jenkins

USER jenkins

# install build tools and platform
RUN sdkmanager "emulator" "tools" "system-images;android-28;google_apis;x86"

# Emulator
RUN echo "no" | avdmanager create avd -n emulator_x86_28_google -k "system-images;android-28;google_apis;x86" -c 4096M

COPY --chown=jenkins:jenkins start_emulator.sh /usr/local/bin/start-emulator
