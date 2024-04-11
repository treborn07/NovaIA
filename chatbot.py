import json
import random
import spacy
from difflib import SequenceMatcher
from textblob import TextBlob
import wikipedia

# Carregar o modelo de linguagem SpaCy
nlp = spacy.load("pt_core_news_sm")

class SimpleChatbot:
    def __init__(self):
        self.data_file = 'conversas.json'
        self.pares = self.carregar_pares()
        self.perguntas_feedback = []

    def carregar_pares(self):
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def salvar_pares(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.pares, file, indent=4)

    def corrigir_ortografia(self, texto):
        return str(TextBlob(texto).correct())

    def similaridade(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

    def encontrar_resposta(self, pergunta):
        max_similaridade = 0  # Inicializa a similaridade máxima encontrada
        resposta_encontrada = None  # Inicializa a resposta encontrada como None
        doc_pergunta = nlp(pergunta)
        
        for par in self.pares:
            doc_par = nlp(par['pergunta'])
            similaridade = doc_pergunta.similarity(doc_par)
            
            if similaridade > max_similaridade:  # Verifica se a similaridade atual é maior que a máxima encontrada
                max_similaridade = similaridade  # Atualiza a similaridade máxima
                resposta_encontrada = par['resposta']  # Atualiza a resposta correspondente
        
        if max_similaridade > 0.7:  # Verifica se a similaridade máxima encontrada é maior que o limite
            return resposta_encontrada  # Retorna a resposta correspondente se a similaridade for alta o suficiente
        else:
            return None  # Retorna None se nenhuma resposta correspondente for encontrada

    def adicionar_par(self, pergunta, resposta):
        novo_par = {'pergunta': pergunta, 'resposta': resposta}
        self.pares.append(novo_par)
        self.salvar_pares()

    def editar_resposta(self):
        pergunta_editar = input("Qual pergunta você deseja editar? ")
        for par in self.pares:
            if self.similaridade(pergunta_editar.lower(), par['pergunta'].lower()) > 0.7:
                nova_resposta = input("Digite a nova resposta: ")
                par['resposta'] = nova_resposta
                self.salvar_pares()
                print("Resposta editada com sucesso!")
                return
        print("Desculpe, não encontrei a pergunta que você deseja editar.")

    def consultar_wikipedia(self, termo):
        try:
            resultado = wikipedia.summary(termo, sentences=2)
            return resultado
        except wikipedia.exceptions.DisambiguationError:
            return "Há várias possíveis correspondências. Por favor, seja mais específico."
        except wikipedia.exceptions.PageError:
            return "Não encontrei informações sobre este tópico."

    def interagir(self):
        print("Olá! Eu sou um chatbot. Vamos conversar!")
        while True:
            pergunta = input("Você: ")
            resposta = self.encontrar_resposta(pergunta)
            if resposta:
                print("ChatBot:", resposta)
            elif 'contar história' in pergunta.lower():
                print("ChatBot:", self.contar_historia_aleatoria())
            elif 'pesquisar' in pergunta.lower():
                termo_pesquisa = pergunta.split(' ', 1)[1]  # Obtém o termo de pesquisa após 'pesquisar '
                print("ChatBot:", self.consultar_wikipedia(termo_pesquisa))
            else:
                print("ChatBot: Desculpe, não sei responder a essa pergunta.")
                if pergunta not in self.perguntas_feedback:
                    feedback = input("Esta resposta foi útil? (sim/não): ").lower()
                    if feedback == "não":
                        nova_resposta = input("Como você gostaria de responder a esta pergunta? ")
                        self.adicionar_par(pergunta, nova_resposta)
                        print("Obrigado pelo seu feedback! A resposta foi atualizada.")
                    self.perguntas_feedback.append(pergunta)

    def contar_historia_aleatoria(self):
        historias = [
            "Era uma vez um reino distante onde vivia um bravo cavaleiro...",
            "Numa floresta encantada, existia um elfo muito curioso...",
            "Numa cidade movimentada, um detetive investigava um misterioso caso..."
        ]
        return random.choice(historias)

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.interagir()
