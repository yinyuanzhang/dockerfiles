FROM kojiromike/docker-gentoo-build-base
RUN ["emerge", "uwsgi"]
WORKDIR /srv
EXPOSE 80
ENTRYPOINT ["uwsgi_python36"]
CMD ["--http", ":80", "--wsgi-file", "example.py"]
COPY example.py .
