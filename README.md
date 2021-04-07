# Speech to Text
### Michail Samaritakis

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This project based on a Python core is a simple speech to text converter. It utilizes Google's cloud services to translate your words into text or record them.
* There are future plans to make a C# based GUI.

## Installation

**OS X & Linux:** 
sudo apt-get install python3-tk

**Windows:** 
pip install tk

*Python must be installed for this program to compile and run.*

### Usage Example

To create the .exe file you need to install the module PyInstaller, for
Windows: pip install pyinstaller, for MAC OS it comes pre-installed. 
After opening a terminal at the desired location, proceed to 
executing the commands below: 
  pyinstaller --onefile speech_to_text.py

To run the .exe just double click it, a terminal will open, when a message appears
simply speak into the microphone, after you are done, the text version of what 
you just said will appear. 
Afterwards, two messages will appear, asking whether you want to save the text
or the recording of your voice. In case you click yes and name the files
you will be able to find either a .txt file or .mp3, or both 
at the location where your .exe file is. 




This text you see here is *actually- written in Markdown! To get a feel
for Markdown's syntax, type some text into the left window and
watch the results in the right.

#### License 

MIT .
