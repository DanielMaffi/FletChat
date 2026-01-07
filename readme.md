# 🚀 FletChat

FletChat é um **aplicativo de chat em tempo real** desenvolvido em **Python**, utilizando o framework **Flet**. O projeto foi criado com foco em **aprendizado prático**, organização de código e construção de interfaces interativas, sendo ideal para **portfólio no GitHub**.

Este projeto demonstra conceitos importantes como comunicação entre usuários, atualização de interface em tempo real e boas práticas iniciais em aplicações Python.

---

## 🖼️ Prints da Aplicação

> Exemplos de telas do **FletChat** em execução:

### Tela Inicial
![Tela Inicial](./prints/tela_inicial.png)

### Entrada no Chat
![Entrada no Chat](./prints/entrada_chat.png)

### Chat em Funcionamento
![Chat em Funcionamento](./prints/chat_funcionando.png)

> 📌 **Observação:** Crie uma pasta chamada `prints` na raiz do projeto e adicione as imagens com os nomes indicados acima.

---

## ✨ Funcionalidades

- Entrada de usuários com nome personalizado
- Chat em tempo real entre múltiplos usuários
- Mensagens automáticas de boas-vindas
- Exibição de data e hora em cada mensagem
- Interface simples, limpa e funcional
- Execução via navegador (Web)

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Flet
- PubSub (Flet)
- Datetime

---

## 📦 Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`.

Para instalar tudo de uma vez, execute:

```bash
pip install -r requirements.txt
```

- **Python 3**
- **Flet** (UI e PubSub)
- **Datetime** (data e hora das mensagens)
- **Programação orientada a eventos**

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/fletchat.git
```

2. Acesse a pasta do projeto:

```bash
cd fletchat
```

3. Instale as dependências:

```bash
pip install flet
```

---

## ▶️ Como Executar

Execute o arquivo principal:

```bash
python FletChat.py
```

O aplicativo será aberto automaticamente no navegador.

---

## 🧠 Arquitetura e Funcionamento

- O usuário informa seu nome ao iniciar o chat
- Uma mensagem de boas-vindas é enviada automaticamente
- As mensagens são distribuídas em tempo real usando `page.pubsub`
- Cada mensagem contém:
  - Data
  - Hora
  - Nome do usuário
  - Conteúdo digitado

O código foi estruturado de forma simples e didática, facilitando a leitura e manutenção.

---

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido para:

- Praticar **Python aplicado a interfaces gráficas**
- Aprender **comunicação em tempo real**
- Explorar o framework **Flet**
- Servir como **projeto de portfólio** para vagas iniciais em desenvolvimento

---

## 🔮 Possíveis Melhorias Futuras

- Sistema de salas de chat
- Autenticação de usuários
- Persistência de mensagens
- Interface responsiva para mobile
- Deploy em nuvem

---

## 📄 Licença

Este projeto é livre para uso educacional e aprendizado.
