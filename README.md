# NovaIA
Chatbot 2.0
ChatBot

O ChatBot é um assistente virtual simples desenvolvido em Python que utiliza as bibliotecas SpaCy, difflib, TextBlob e Wikipedia para processamento de linguagem natural e busca de informações na Wikipedia. Este projeto permite aos usuários interagirem com o ChatBot, fazendo perguntas e recebendo respostas com base em um conjunto de pares de perguntas e respostas pré-definidos, além de fornecer funcionalidades como pesquisa na Wikipedia e contação de histórias.
Pré-requisitos

Para executar o ChatBot, é necessário ter Python instalado em seu sistema. Além disso, você precisará instalar as seguintes bibliotecas Python:

    Spacy: Biblioteca para processamento de linguagem natural.
    difflib: Biblioteca para cálculo de similaridade entre strings.
    TextBlob: Biblioteca para correção ortográfica e análise de texto.
    Wikipedia: Biblioteca para acessar informações da Wikipedia.

Instalação

    Clone o repositório:

    bash

git clone https://github.com/seu-usuario/chatbot.git

Navegue até o diretório do projeto:

bash

cd chatbot

Instale as dependências:

bash

    pip install -r requirements.txt

    Certifique-se de ter permissões de administrador ou utilize um ambiente virtual Python para evitar conflitos com pacotes instalados globalmente.

Como usar

    Execute o aplicativo:

    bash

    python chatbot.py

    Digite uma pergunta na caixa de entrada.

    Pressione Enter para enviar a pergunta.

    Aguarde a resposta do ChatBot na saída do console.

Funcionalidades

    Carregar pares de perguntas e respostas: O ChatBot carrega pares de perguntas e respostas de um arquivo JSON pré-definido.
    Correção ortográfica: O ChatBot corrige erros ortográficos nas perguntas digitadas pelo usuário.
    Resposta baseada na similaridade: O ChatBot encontra a resposta mais adequada com base na similaridade entre a pergunta do usuário e as perguntas armazenadas.
    Pesquisa na Wikipedia: O ChatBot é capaz de buscar informações na Wikipedia quando solicitado pelo usuário.
    Contação de histórias: O ChatBot pode contar histórias aleatórias quando solicitado pelo usuário.
    Feedback do usuário: O ChatBot solicita feedback ao usuário para determinar se a resposta foi útil ou não. Se a resposta não for útil, o usuário pode fornecer uma resposta alternativa.

Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue para reportar bugs ou solicitar novos recursos. Se desejar contribuir com código, siga estas etapas:

    Fork do repositório
    Crie uma branch para sua feature (git checkout -b feature/MinhaFeature)
    Faça commit das suas alterações (git commit -am 'Adiciona nova feature')
    Faça push para a branch (git push origin feature/MinhaFeature)
    Abra um Pull Request

Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
