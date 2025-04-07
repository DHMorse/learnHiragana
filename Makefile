build:
	nuitka --onefile --standalone --remove-output --output-dir=dist --output-filename=learnHiragana src/main.py

run:
	./dist/learnHiragana

dev:
	python src/main.py

test:
	python -m pytest tests

clean:
	rm -rf dist
	rm -rf build
	rm -rf build.log
	rm -rf nuitka-crash-report.xml 

rebuild:
	make clean
	make build
