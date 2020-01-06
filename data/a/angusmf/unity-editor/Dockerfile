FROM angusmf/unity-install-dependencies

RUN mkdir -p /root/.cache/unity3d && mkdir -p /root/.local/share/unity3d/Unity && mkdir -p /root/.local/share/unity3d/Certificates
RUN mkdir /app

RUN curl -o /app/unity_setup http://beta.unity3d.com/download/292b93d75a2c/UnitySetup-2019.1.0f2
RUN chmod +x /app/unity_setup
RUN mkdir /opt/Unity
RUN mkdir /app/unity_download
RUN printf 'y\n' | /app/unity_setup --unattended --components="Unity" --install-location /opt/Unity --download-location /app/unity_download
RUN rm -rf /app/unity_download