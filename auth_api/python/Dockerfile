FROM python:3-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENV FLASK_APP=api.py
EXPOSE 8000
ENTRYPOINT ["python"]
CMD [ "api.py"]

# Add your instructions to dockerize the application
# App must run on port 8000
