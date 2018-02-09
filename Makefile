init:
		pip install -r requirements.txt

run: clean
		python3 main.py

clean:
		rm -rf **/__pycache__/
