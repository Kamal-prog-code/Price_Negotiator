FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /PNECBS
ADD . /PNECBS
COPY ./requirements.txt /PNECBS/requirements.txt
USER root
RUN pip3 install -r requirements.txt
COPY . /PNECBS

FROM rasa/rasa-sdk:2.1.3
WORKDIR /PNECBS
COPY ./actions /PNECBS/actions
COPY . /PNECBS

USER 1000


