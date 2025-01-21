# Projeto API Pokémon 💛

Este repositório contém um projeto de aplicação web que consome a [API oficial de Pokémon](https://pokeapi.co/api/v2/), permitindo aos usuários acessar informações detalhadas sobre Pokémon. O projeto foi desenvolvido utilizando Flask, um microframework Python leve e eficiente para criação de aplicações web modernas.

---

## Objetivo 🏆

Desenvolver uma aplicação web que facilite o acesso às informações dos Pokémon, permitindo aos usuários realizar buscas específicas por nome ou ID. O projeto também tem como objetivo demonstrar habilidades no uso de frameworks Python e no consumo de APIs RESTful.

---

## Ferramentas Utilizadas 🛠️

- **Python**: Versão 3.12.1 - linguagem de programação utilizada para a lógica do backend.
- **Flask**: Microframework Python que proporciona um desenvolvimento web rápido e eficiente, com suporte a templates e extensões.
- **Requests**: Biblioteca Python utilizada para realizar requisições HTTP para a API de Pokémon.
- **HTML/CSS**: Para estruturação e estilização da interface do usuário.

---

## Configuração do Ambiente ⚙️

### Pré-requisitos

1. Certifique-se de ter o Python 3.12.1 instalado em sua máquina.
2. Instale um gerenciador de pacotes, como `pip` (já incluso em versões recentes do Python).
3. Clone este repositório localmente para iniciar.

### Clonando o repositório

```bash
# Clone o repositório do GitHub
$ git clone https://github.com/sabrinnesousa/ApiPokemon.git

# Navegue até o diretório do projeto
$ cd ApiPokemon
```

### Instalando dependências

Crie e ative um ambiente virtual para manter as dependências organizadas:

```bash
# Crie um ambiente virtual
$ python -m venv venv

# Ative o ambiente virtual
# No Windows:
$ venv\Scripts\activate
# No Linux/Mac:
$ source venv/bin/activate

# Instale as dependências do projeto
$ pip install -r requirements.txt
```

### Executando o projeto

Com o ambiente configurado, inicie o servidor Flask:

```bash
$ flask run

# O servidor será iniciado em http://127.0.0.1:5000
```

---

## Estrutura de Arquivos 📁

```plaintext
ApiPokemon/
├── static/            # Arquivos estáticos (CSS, JS, imagens)
├── templates/         # Arquivos HTML (templates do Flask)
├── app.py             # Código principal do Flask
├── requirements.txt   # Lista de dependências do projeto
└── README.md          # Documentação do projeto
```

---

## Resultado Final 🌟

Após configurar e executar o projeto, você poderá acessar a aplicação no navegador e buscar informações sobre qualquer Pokémon disponível na [PokeAPI](https://pokeapi.co/). O design responsivo e a interação simples tornam a experiência do usuário prática e intuitiva. 🚀

### Captura de Tela da Interface Inicial


---

## Contribuição 🤝

Fique à vontade para abrir issues ou enviar pull requests com melhorias, correções de bugs ou novas funcionalidades. Vamos construir algo incrível juntos!

---

[Link para o Repositório GitHub](https://github.com/sabrinnesousa/ApiPokemon)
