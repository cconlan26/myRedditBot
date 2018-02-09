init:
		pip install -r requirements.txt

run: clean
		py -3 main.py

clean:
		rm -rf **/__pycache__/
