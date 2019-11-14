from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import codecs


bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir ('C:/Users/asus\Desktop\chatterbot-corpus-master\chatterbot_corpus\data\Bangla/'):
	data = codecs.open('C:/Users/asus\Desktop\chatterbot-corpus-master\chatterbot_corpus\data\Bangla/' + files, 'r' , encoding='utf-8').readlines()
	bot.train(data)

while True:
	message = input ('You: ', )
	if message.strip() != 'বাই':
		reply = bot.get_response(message)
		print('Admission_Helpline:',reply)
	if message.strip() == 'বাই':
		print('Admission_Helpline: bye')
		break