# Mini IT Project for MMU
Mini IT Project for MMU by Harris, Laxman, Dullah, and Kuben. This is the main repo for all the mini IT project code. This project is written entirely in Python.

## Style Guide
This project uses Black to format code.

### Module Structure
Modules are designed in the form of Tkinter child classes. Each class should be stored in its own code file. No additional code should be present outside the class, except for commented-out test code.

### Variable Access
Internal variables used inside classes that are not meant for public-facing access should follow the naming convention of `_variableName` to denote private variables or functions.

### Type Information & Documentation
All classes must have a docstring following the Google style guide as well as type hinting via the typing module. Public class methods must also have a docstring in the same format but type information is optional.

## How to Contribute
Fork this repo, make your changes, and submit a pull request when you think it's ready. If you are in charge of multiple functions, please do your work in seperate branches and file seperate pull requests. This will make things much easier.

## Dependencies
If you've used any external libraries, please ship a `requirements.txt` file in your respective pull requests.
