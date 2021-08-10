FROM python:3.8-slim  

COPY . /app 

WORKDIR /app 

RUN pip install -u flask 

ENV FLASK_APP=flask_app.py 

CMD ["flask", "run", "--host=0.0.0.0", "--port:5000"] 