# bme547ci
## Unit Testing and Continuous Integration User Guide

The program is designed to recognize and judge whether the input word matches the word "tachycardic" 
even if there is typos in the characters. The filter system can help docter better file and sort the
correct database efficiently.

# To Open tachycardic.py
Run the code, user will be asked to type in  string argument. After typing in the characters there 
will be a output indicating whether your input matches the word "tachycardic"(should be at least 80% 
alike so that it can tolerate 2 typos).
The first line will be the detected result.
The second line will return value of True or False of your input
The third line will show the similarity to the correct spelling

# To run a test file with tachycardic_test.py
Please test the file in virtual environment. You can use anaconda Promp.
After seting and activate virtual environment for test.
run code $ py.test and the result might pop up and should show True and pass as expected since in my test file.

Have fun with it.
