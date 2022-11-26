from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

FALAS_SETTINGS=[
    # Antes de executar o trainer mude o diretorio abaixo:

    "C:\\Users\\ecarl\\OneDrive\\Documentos\\Projetos Em python\\Greta Chatbot\\falas\\cumprimentos.json",
    "C:\\Users\\ecarl\\OneDrive\\Documentos\\Projetos Em python\\Greta Chatbot\\falas\\doacao.json"
    ]

def initialize():
    global bot
    global trainer

    bot = ChatBot("Greta")
    trainer = ListTrainer(bot)

def load_conversations():
    falas =[]

    for setting_file in FALAS_SETTINGS:
        with open(setting_file, 'r',encoding="utf-8") as file:
            configuracao_falas = json.load(file)
            falas.append(configuracao_falas["conversations"])

            file.close()
    

    return falas;


def treinar_bot(falas):
    global trainer

    for falas in falas:
        for message_response in falas:
            messages = message_response["messages"]
            response = message_response["response"]

            print("Treinando o robô para responder a:'",messages, "' Com a resposta'",response,"'")
            for message in messages:
                trainer.train([message,response])


if __name__ == "__main__":
    initialize()
    conversa = load_conversations()
    if conversa:
        treinar_bot(conversa)