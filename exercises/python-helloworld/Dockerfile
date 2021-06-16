FROM python:3.8
LABEL maintainer="Ali Belachkar"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# Command to run on container start
CMD [ "python", "app.py" ]
