FROM python:3.6
WORKDIR /app
ADD . /app
COPY requirements.txt /app
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m pip install ibm_db

EXPOSE 5000
CMD [ "python", "app.py"]