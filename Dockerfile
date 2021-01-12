# parent image
FROM python:3.7-slim

RUN apt-get update && apt-get upgrade -y

ADD requirements.txt requirements.txt
COPY src/ src/

#install python library
RUN python3 -m pip install -r requirements.txt

#make the work directory
WORKDIR /src

#command to run the application
CMD ["python3","-u", "flask_app.py"]