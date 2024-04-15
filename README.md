# debt_simplifier
Playground for testing

Debt Simplifier's goal is to minimize the amount of required money transfers between many debtors and creditors. (E.g. Person A owes person B $20, person B owes person C $20, and person C owes person A $10. Then it is sufficient for person A to pay person C $10 and no additional transfers are needed.)

algorithm.py contains a class called "Calculator" that takes a nx3 matrix. Each row should contain two names (debter, credtior) and a number (debt amount).
Program then returns a matrix with reduced amount of transfers.

server.py contains a script that allows for starting a development server.
[Flask](https://flask.palletsprojects.com/en/3.0.x/installation/#python-version) must be installed in order to use server.py

server.py, algorithm.py and templates must be in the same path to work properly.



Dockerfile is here for me for future use of Docker and nginx to further experiment with the web-app.

tkinter.py was written as an attempt to create a basic app using the main algorithm.

# TODO
-adding unit tests
-cleaning the code
-attempt to make a properly working website 
