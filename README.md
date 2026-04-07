# Pink Urban Lists

> Listas simples que você pode compartilhar.

Um gerenciador de tarefas minimalista e colaborativo, pensado para ser rápido, intuitivo e fácil de compartilhar. Inspirado na simplicidade do [Flask.io](https://flask.io), com a identidade visual da **Pink Urban**.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-E91E8C?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1-000?logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-E91E8C)

</div>

---

## ✨ Funcionalidades

- **Criação rápida** — crie listas em segundos, sem friccao
- **Datas de vencimento** — defina "hoje", "amanha", "proxima semana" ou escolha no calendario
- **Indicadores visuais** — itens atrasados em vermelho, itens de hoje em destaque rosa
- **Vistas separadas** — itens pendentes e concluidos em secoes distintas
- **Edicao inline** — clique no nome do item para renomear (Enter salva, Esc cancela)
- **Drag & Drop** — reordene itens arrastando e soltando
- **Compartilhamento por link** — copie a URL e qualquer pessoa acessa a lista
- **Configuracoes do usuario** — altere sua senha a qualquer momento pelo dropdown do perfil
- **Sistema de aprovacao** — novos usuarios precisam de aprovacao do admin
- **Painel administrativo** — aprove/rejeite usuarios, veja metricas
- **Design smooth** — transicoes suaves, hover animations, feedback visual em cada acao
- **Seguranca avancada** — rate limiting, CSP, HSTS e headers de seguranca via Talisman
- **Totalmente responsivo** — funciona em desktop, tablet e mobile

## 🚀 Quick Start

### Requisitos

- Python 3.10+

### Instalacao local

```bash
# Clone o repositorio
git clone https://github.com/mathvelozzo/TODO-List---Pink-Urban.git
cd TODO-List---Pink-Urban

# Crie um ambiente virtual (recomendado)
py -m venv venv
venv\Scripts\activate

# Instale as dependencias
py -m pip install -r requirements.txt

# Configure as variaveis de ambiente
copy .env.example .env
# Edite .env e altere o SECRET_KEY

# Rode o aplicativo
py run.py
```

Acesse **http://127.0.0.1:5000**

### Primeiro Acesso Admin

Na primeira execucao, um usuario admin criado automaticamente. A senha e exibida no console:

```
Admin criado! Senha: xyz123abc — ALTERE NO PRIMEIRO ACESSO!
```

Faça login como `admin` e a senha exibida para acessar o painel administrativo.

### 🔐 Reset da Senha Admin

Se esqueceu a senha do admin:

```bash
py reset_admin.py
```

## 📱 Como Usar

### Criando sua primeira lista

1. Cadastre-se na pagina principal
2. Clique em **"+ Criar Nova Lista"**
3. Digite o titulo e confirme
4. Clique em **"Abrir"** na lista criada

### Adicionando itens com data

1. Dentro da lista, digite o nome do item
2. Clique no icone de calendario para abrir o seletor
3. Escolha uma data rapida (**Hoje**, **Amanha**, **Prox. Semana**) ou selecione no calendario
4. Clique em **"+ Adicionar"**

### Definindo/alterando datas de itens existentes

1. Clique na data exibida ao lado de qualquer item (mesmo "Sem data")
2. Escolha no calendario ou use botoes rapidos
3. Clique em **"Confirmar"** (ou **"Limpar"** para remover)

### Editando nome do item

1. Clique no texto de qualquer item
2. O campo de texto aparece inline
3. Pressione **Enter** para salvar ou **Esc** para cancelar

### Reordenando itens

Arraste e solte os itens — a nova ordem e salva automaticamente.

### Compartilhando

1. Na pagina da lista, clique em **"Copiar Link"**
2. Envie o link para qualquer pessoa
3. Quem receber pode visualizar a lista

### Alterando sua senha

1. Clique no seu avatar/nome no topo da pagina
2. Selecione **Configuracoes**
3. Preencha a senha atual e a nova senha

## 🏗️ Estrutura do Projeto

```
.
├── run.py                  # Entry point (desenvolvimento)
├── wsgi.py                 # WSGI entry point (producao)
├── app.py                  # Flask app factory + configuracoes
├── models.py               # Modelos: User, TodoList, ListItem
├── main.py                 # Rotas publicas + API CRUD de listas/itens
├── auth.py                 # Login, cadastro, logout e settings
├── admin.py                # Painel administrativo
├── reset_admin.py          # Script para reset de senha admin
├── requirements.txt        # Dependencias Python
├── Procfile                # Configuracao para Railway/Heroku
├── .env.example            # Exemplo de variaveis de ambiente
├── SECURITY.md             # Checklist de seguranca
├── README.md               # Este arquivo
├── static/
│   ├── css/style.css       # Estilos completos (tema Pink Urban)
│   └── js/main.js          # JS utilitario
└── templates/
    ├── base.html           # Layout base
    ├── index.html          # Pagina principal (hero, features, social proof)
    ├── settings.html       # Configuracoes do usuario
    ├── login.html          # Tela de login
    ├── register.html       # Tela de cadastro
    ├── view_list.html      # Visualizacao de lista
    └── admin/
        ├── base.html       # Layout do admin
        ├── dashboard.html  # Painel admin
        └── users.html      # Lista de usuarios
```

## 🔒 Seguranca

- Senhas armazenadas com **bcrypt** (via werkzeug)
- Rotas protegidas com `@login_required` e `@admin_required`
- **Ownership validation** — usuarios so editam proprias listas
- **Rate limiting** — Flask-Limiter (10 req/min login, 5 req/min cadastro)
- **CSP e headers de seguranca** — Flask-Talisman (X-Frame, HSTS, X-Content-Type)
- Cookies de sessao com `HttpOnly` e `SameSite=Lax`
- **Input sanitization** — html.escape e regex para username
- **Login logging** — tentativas falhas registradas em log
- `.env` no `.gitignore` — secrets nunca vao pro repositorio

Veja o checklist completo em [SECURITY.md](SECURITY.md).

## 🚀 Deploy em Producao

### Railway

1. Conecte o repositorio no [Railway](https://railway.app)
2. Na aba **Variables**, adicione:

| Variable | Valor |
|---|---|
| `SECRET_KEY` | (gerar com `python -c "import secrets; print(secrets.token_hex(32))"`) |
| `DATABASE_URL` | `sqlite:///pink_urban.db` |
| `SESSION_COOKIE_SECURE` | `true` |
| `FLASK_DEBUG` | `false` |

3. Deploy automatico via `Procfile` (Gunicorn)

### Outros servidores

```bash
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:8000 --workers 4 wsgi:application
```

Use Nginx como reverse proxy na frente do Gunicorn e configure HTTPS com Let's Encrypt.

## 🎨 Design

O tema **Pink Urban** usa uma paleta rosa vibrante com animacoes suaves:

| Elemento | Cor |
|----------|-----|
| Primária | `#E91E8C` |
| Hover | `#D4167D` |
| Fundo | `#F8FAFC` |
| Sucesso | `#22C55E` |
| Alerta | `#F59E0B` |
| Erro | `#EF4444` |

Todas as transicoes usam `cubic-bezier(0.4, 0, 0.2, 1)` para movimento natural.

## 📄 Licenca

MIT

---

Feito com 💗 por **Pink Urban**
