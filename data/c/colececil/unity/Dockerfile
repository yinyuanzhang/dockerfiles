FROM ubuntu:18.04

# Make installs happen non-interactively
ENV DEBIAN_FRONTEND noninteractive

# Install Unity install-time dependencies
RUN \
    apt-get update && \
    apt-get install -y wget && \
    apt-get install -y yes && \
    apt-get install -y libgtk2.0-0 && \
    apt-get install -y libsoup2.4-1 && \
    apt-get install -y libarchive13

# Set Unity installer URL
# For links to download other versions, see https://forum.unity.com/threads/unity-on-linux-release-notes-and-known-issues.350256/
ENV UNITY_INSTALLER_URL https://beta.unity3d.com/download/10189b18f56e/UnitySetup-2018.2.0f2

# Install Unity
RUN \
    wget ${UNITY_INSTALLER_URL} -O unity-installer && \
    chmod +x ./unity-installer && \
    yes | ./unity-installer --unattended --components=Unity,Windows,Mac --install-location=/opt/unity
ENV UNITY /opt/unity/Editor/Unity

# Install Unity runtime dependencies
RUN \
    apt-get update && \
    apt-get install -y gconf-service && \
    apt-get install -y lib32gcc1 && \
    apt-get install -y lib32stdc++6 && \
    apt-get install -y libasound2 && \
    apt-get install -y libc6 && \
    apt-get install -y libc6-i386 && \
    apt-get install -y libcairo2 && \
    apt-get install -y libcap2 && \
    apt-get install -y libcups2 && \
    apt-get install -y libdbus-1-3 && \
    apt-get install -y libexpat1 && \
    apt-get install -y libfontconfig1 && \
    apt-get install -y libfreetype6 && \
    apt-get install -y libgcc1 && \
    apt-get install -y libgconf-2-4 && \
    apt-get install -y libgdk-pixbuf2.0-0 && \
    apt-get install -y libgl1-mesa-glx && \
    apt-get install -y libglib2.0-0 && \
    apt-get install -y libglu1-mesa && \
    apt-get install -y libgtk-3-0 && \
    apt-get install -y libnspr4 && \
    apt-get install -y libnss3 && \
    apt-get install -y libpango1.0-0 && \
    apt-get install -y libstdc++6 && \
    apt-get install -y libx11-6 && \
    apt-get install -y libxcomposite1 && \
    apt-get install -y libxcursor1 && \
    apt-get install -y libxdamage1 && \
    apt-get install -y libxext6 && \
    apt-get install -y libxfixes3 && \
    apt-get install -y libxi6 && \
    apt-get install -y libxrandr2 && \
    apt-get install -y libxrender1 && \
    apt-get install -y libxtst6 && \
    apt-get install -y zlib1g && \
    apt-get install -y debconf && \
    apt-get install -y npm

# Add unity user
RUN \
    groupadd unity && \
    useradd -m -g unity unity

# Create directory for Unity cache
RUN \ 
    mkdir /home/unity/.cache && \ 
    mkdir /home/unity/.cache/unity3d

# Make sure there are no permissions issues running Unity
RUN chown -R unity:unity /opt/unity

# Switch user and working directory
USER unity
RUN mkdir /home/unity/unity-project
WORKDIR /home/unity/unity-project