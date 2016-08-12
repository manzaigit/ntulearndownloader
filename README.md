# ntulearndownloader-
just as the name suggests :D

Ever felt frustrated when you have to download your lecture notes so labouriously, clicking the links and pressing ctrl+s for every document one-by-one?
We felt so too and here's a tool to help all of us! :)
All you have to do is to input the URL and download path :D

# Getting started (One time setup)
- Install python (3.5.1)
- Install pip
- Install virtualenv for python
- Run as administrator in windows powershell and run the following command

		cd ntulearndownloader
		Set-ExecutionPolicy bypass # mac ignore this 
		.\dev.ps1  # mac ./dev.sh

# Execute before running application
- Run the following command to activate the virtual environment

		venv\scripts\activate	# mac venv/bin/activate

# Using the application
- Start the application by entering your ntulearn username and password and the application will guide you through

        python main.py -u <username> -p <password>
