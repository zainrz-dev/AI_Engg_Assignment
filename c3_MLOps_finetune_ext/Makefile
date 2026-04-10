install:
	pip install -r api/requirements.txt

lint:
	pip install flake8
	flake8 api/

test:
	echo "Add tests here"

build:
	docker build -t neural-ops-api .

run:
	docker run -p 8000:8000 neural-ops-api