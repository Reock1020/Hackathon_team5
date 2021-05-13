from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ListTrainer


def training(corpus_list):
    chatbot = ChatBot(**settings.CHATTERBOT)
    trainer = ListTrainer(chatbot)
    trainer.train(corpus_list)