from chatterbot import ChatBot
from difflib import SequenceMatcher

ACCEPTANCE = 0.70

def compara_mensagem(message, candidate_message):
    similarity = 0.0

    if message.text and candidate_message.text:
        message_text = message.text
        candidate_text = candidate_message.text

        similarity = SequenceMatcher(
            None,
            message_text,
            candidate_text
        )
        similarity = round(similarity.ratio(),2)
        if similarity < ACCEPTANCE:
            similarity = 0.0


    return similarity

def seleciona_resposta(message, lista_resposta, storage=None):
    response = lista_resposta[0]


    return response


def ola_greta():
    bot = ChatBot("Greta",
        read_only=True,
        statement_comparison_function=compara_mensagem,
        response_selection_method=seleciona_resposta,
        logic_adapters=[
            {
                "import_path":"chatterbot.logic.BestMatch",
            }
        ])

    while True:
        chat_input = input("Voce:",)
        response = bot.get_response(chat_input)

        if response.confidence > 0.0:
            print("Greta:",response.text)
        else:
            print("Não entendi")
            print("nao estendi, gostaria de um fazer uma doção ou gostaria de informações")

if __name__ == "__main__":
    ola_greta()



