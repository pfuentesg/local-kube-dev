FROM python:3.9.5-alpine
RUN pip3 install flask
COPY . /app
WORKDIR /app
ENTRYPOINT ["python3"]
CMD ["app.py"]