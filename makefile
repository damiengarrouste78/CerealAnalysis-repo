requirement:
	@echo "requirements installation"
	pip install –r requirement.txt

clean:
	@echo "Cleaning up..."
	rm ./CerealAnalysis/data/output/*
	