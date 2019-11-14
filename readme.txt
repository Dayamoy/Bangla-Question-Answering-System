## Bangla Question Answering System for Admission Helpline in Bangladesh
Mainly we collected data from various fb group in this project. That was our main challange. 
Then for testing, we build a chatbot. Actually it was very naive. We use a module called chatterbot in python.

These modules are used to quickly train ChatterBot to respond to various inputs in different languages. Although much of ChatterBot is designed 
to be language independent, it is still useful to have these training sets available to prime a fresh database and make the variety of responses 
that a bot can yield much more diverse.

For instructions on how to use these data sets, please refer to the project documentation.

All training data contained within this corpus is user contributed.

Chatterbot is a very flexible and dynamic chatbot that you easily can create your own training data and structure.

Create or copy an existing .yml/txt file and put that file in a existing or a new directory you created under chatterbot_corpus\data\<NEW DIRECTORY> 
Edit that file with any text editor that you like to work with.

In previous we collected our data in csv format. But in this courpus question answer must be read  from one file. First line was the question then second line
 was the answer of previous question.Then third line was another question and then next line was its' answer. so the yml/txt file should contain
question then answer this format. for converting this file csv to txt we run a python code which was attached to this project named csv_to_txt.py.
Our main code of chatbot is attached in this project also named chatbot_code.py .

This chatterbot project is also attached to this project .you can also find it https://github.com/gunthercox/chatterbot-corpus. and you also can
read about this module in this link https://chatterbot.readthedocs.io/en/stable/tutorial.html . 