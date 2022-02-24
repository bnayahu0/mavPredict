Hi everyone!

this zip includes:
3 .py files
1 .pkl file
1 screenshot

pkl file - this is the AI model (exported by joblib library)
py file - run the main file, it will call the others
screenshot - this is api call example by postman

wish you luck :)

Amihay

I run it with python 3.10. I think older versions should work too.
to install dependencies, run:

pip install -r requirments.txt
and then just:
python main.py

to build the container, run 
docker build -t amihaypredic:1.0.1 .

and then 
docker run -p 5000:5000 amihaypredic:1.0.1
