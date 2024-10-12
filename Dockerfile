
FROM	python:3.12
WORKDIR	/usr/src/app
COPY	requirements.txt	./
RUN	pip install --no-cache-dir -r requirements.txt
COPY	.	.
ENV	WEBHOOK_URL	https://discordapp.com/api/webhooks/1102825994051661824/BF2aYoqrt3opsM1kS1A5cCgKRV3qDEwzjtpQ8mDB5bLb87mUHxiJaIhURu8Se67CjNve
ENV	DEVELOPER_KEY	AIzaSyAcnkyc5TVBk3c9i9hqSrL8s7K8jlFDqQU
CMD	["python","src/main.py"]
