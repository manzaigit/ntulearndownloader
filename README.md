|python_versions|

# ntulearndownloader-
just as the name suggests :D

Ever felt frustrated when you have to download your lecture notes so labouriously, clicking the links and pressing ctrl+s for every document one-by-one?
We felt so too and here's a tool to help all of us! :)
All you have to do is to input the URL and download path :D

# Project setup for developers
- Install python 3.5.1
- Install pip
- Run as administrator in windows powershell and run the following command

		cd ntulearndownloader
		Set-ExecutionPolicy bypass
		.\dev.ps1
		venv\scripts\activate

# Using the application
- Start the application by entering your ntulearn username and password and the application will guide you through

        python main.py -u <username> -p <password>
