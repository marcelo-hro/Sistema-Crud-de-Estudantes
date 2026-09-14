# Projeto Sistema Crud de Estudantes

Repositório dedicado ao desenvolvimento de uma aplicação web , desenvolvida utilizando o framework Django (Python).

---

## Começando

Siga as instruções abaixo para clonar o repositório, preparar o ambiente virtual e executar a aplicação localmente.

### Pré-requisitos

Certifique-se de ter instalado em sua máquina:
- Python (versão 3.10 ou superior)
- Git
- Gerenciador de pacotes pip

---

## Instalação e Execução Local

### 1. Clonar o repositório

Abra o terminal na pasta desejada e clone o projeto:

git clone 

abra a pasta do projeto


### 2. Criar e ativar o ambiente virtual (venv)

É altamente recomendado o uso de um ambiente virtual para isolar as dependências do projeto.

No Linux ou macOS:
python3 -m venv venv
source venv/bin/activate

No Windows (PowerShell):
python -m venv venv
.\venv\Scripts\Activate.ps1

No Windows (Prompt de Comando - CMD):
python -m venv venv
.\venv\Scripts\activate.bat

### 3. Instalar as dependências

Com a venv ativada, instale o Django e os pacotes necessários:

pip install django
pip install pillow

Se houver um arquivo requirements.txt no repositório, execute:
pip install -r requirements.txt

### 4. Executar as migrações do banco de dados

Prepare a base de dados (SQLite por padrão) aplicando as migrações:

python manage.py migrate

(Opcional) Crie uma conta de administrador para acessar o painel:
python manage.py createsuperuser

### 5. Iniciar o servidor de desenvolvimento

Inicie o servidor local:

python manage.py runserver

Após iniciar, acesse no navegador:
- Aplicação: http://127.0.0.1:8000/
- Painel Administrativo: http://127.0.0.1:8000/admin/

---

## Comandos Úteis do Django

- Criar novas migrações: python manage.py makemigrations
- Aplicar migrações: python manage.py migrate
- Criar um novo app: python manage.py startapp <nome_do_app>
- Encerrar o servidor: Ctrl + C no terminal
- Desativar ambiente virtual: deactivate

---

## Licença

Este projeto é desenvolvido para fins de estudo e implementação de ferramentas econômicas e computacionais.
