############################################
# This is his Docker file please enlighten #
############################################
FROM python:latest
MAINTAINER Abdelhak Marouane <amarouane@abdelhak.com>
RUN pip install redis && pip install mockredispy
# I tollaly forgot about ADD but does change there means change here
ADD src/ /src
RUN pip install pytest
# See the workdir mean change to work dir
WORKDIR /src/
RUN touch result.xml
ENTRYPOINT pytest --junitxml=result.xml
