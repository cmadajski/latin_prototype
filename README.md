# Latin Conjugation Prototype
To help better understand the logic necessay to evaluate user answers for the brute-force-latin project,
I decided to make a python script that models the same behavior we are seeking to create in Javascript.

The goal of this script is to:
1. show the user a latin word that needs to be declined
2. take user declination input in the form of a string
3. compare the user declination string to the proper declination
4. give user feedback on if the declinations were correct/incorrect
5. give user a performance grade based on the number of correct vs incorrect declinations

There are two branches available that have slightly different logic:
1. main - randomizes the order in which words are shown to the user each iteration
2. not_randomized - removes randomization logic so that words are shown in a static order every iteration

This is a very single use case script that I doubt anyone will find any value in besides our team:
- @g-strick
- @cmadajski
- @rpupo7322

Thank you for your time.
