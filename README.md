## cisc3140

To use this program:
Make sure you have Python (version 3.7 or higher) installed on your computer.
Download the repository into a new directory. 
Inside that directory, install a python virtual environment with the following command in Terminal:


```
$> Python3 -m venv venv
```

After you have installed the vertual environment, use the following command to activate it:

```
$> source venv/bin/activate
```

The next step is to install the necessary items listed in the requirements.txt file. For example:

```
(venv)$> pip install flask
(venv)$> pip install Flask-WTF
(venv)$> pip install requests
```

You can also install them directly from the file:
```
(venv)$> pip install -r requirements.txt
```

You are almost ready to launch this program!
Throw the following command into terminal to tell flask where the main program file is:
```
(venv)$> export FLASK_APP=cisc3140.py
```
You're done! All you need to do now is run the program:
```
(venv)$> flask run
```
and open up your localhost on your browser. 

Enjoy!