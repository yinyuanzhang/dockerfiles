FROM ubuntu:18.04

# In Teilen angelehnt an https://github.com/javibm/UnityDocker/blob/master/Dockerfile

ENV unityURL=https://beta.unity3d.com/download/79b540374219/UnitySetup-2017.4.2f2
ENV unitySetupName=unitySetup
ENV unityComponents="Unity,Android"
ENV unityInstallDir=/usr/local/Unity
ENV unityDownloadDir=/tmp/unity
ENV androidSdkFile=tools_r25.2.5-linux.zip

# This is necessary for unity
ENV ANDROID_SDK_ROOT=/usr/local/androidSdk/

# Download necessary packages for unity3d
RUN apt-get update -qq; \
  apt-get install -qq -y \
  busybox-static \
  gconf-service \
  lib32gcc1 \
  lib32stdc++6 \
  libasound2 \
  libc6 \
  libc6-i386 \
  libcairo2 \
  libcap2 \
  libcups2 \
  libdbus-1-3 \
  libexpat1 \
  libfontconfig1 \
  libfreetype6 \
  libgcc1 \
  libgconf-2-4 \
  libgdk-pixbuf2.0-0 \
  libgl1-mesa-glx \
  libglib2.0-0 \
  libglu1-mesa \
  libgtk2.0-0 \
  libnspr4 \
  libnss3 \
  libpango1.0-0 \
  libstdc++6 \
  libsoup2.4-1 \
  libx11-6 \
  libxcomposite1 \
  libxcursor1 \
  libxdamage1 \
  libxext6 \
  libxfixes3 \
  libxi6 \
  libxrandr2 \
  libxrender1 \
  libxtst6 \
  lib32z1 \
  zlib1g \
  debconf \
  npm \
  nano \
  openjdk-8-jdk \
  screen \
  unzip \
  xdg-utils \
  lsb-release \
  libpq5 \
  xvfb \
  wget \
  libarchive13 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# old libgstreamer for libARWrapper
RUN wget http://de.archive.ubuntu.com/ubuntu/pool/universe/g/gstreamer0.10/libgstreamer0.10-0_0.10.36-1.5ubuntu1_amd64.deb; \
   dpkg -i libgstreamer0.10-0_0.10.36-1.5ubuntu1_amd64.deb; \
   rm libgstreamer0.10-0_0.10.36-1.5ubuntu1_amd64.deb;

  
# ADD unity3d to system
RUN wget -nv ${unityURL} -O ${unitySetupName} \
  && chmod +x ${unitySetupName} \
  && yes | ./${unitySetupName} --unattended --components=${unityComponents} --install-location ${unityInstallDir} --download-location ${unityDownloadDir} \
  && rm ${unitySetupName};
  
# Prepare directories for unity3d:
RUN mkdir -p $HOME/.local/share/unity3d/Unity; \
  mkdir -p $HOME/.cache/unity3d;

# Install Androidsdk with build tools for android-25:
RUN mkdir -p $ANDROID_SDK_ROOT; \
  wget -nv https://dl.google.com/android/repository/${androidSdkFile}; \
  unzip ${androidSdkFile} -d $ANDROID_SDK_ROOT; \
  ( sleep 5 && while [ 1 ]; do sleep 1; echo y; done ) \
  | $ANDROID_SDK_ROOT/tools/android update sdk --no-ui --all --filter tool,platform-tool,android-25,build-tools-27.0.3; \
  rm ${androidSdkFile};

# Clean up (inkl. unity download tmp)
RUN rm -rf /tmp/* /var/tmp/*

