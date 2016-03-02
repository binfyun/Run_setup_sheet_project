#!/usr/bin/python

def greetings(): # Define a function that print the desires words/sentences
    print """
Hello David
Hello David and our world
Why am I doing this?
I must be going insane?
Must I keep doing this?"""

name = raw_input('Hi who am I speaking to? ')  # Allowing use to input a name 
while name != 'David':
        name = raw_input('Hi who am I speaking to? ')  # If name is not David then keep asking user for a name
greetings(); # Call the function greetings which containing sentences we want to display on the monitor

    