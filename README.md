<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-E91E8C?logo=python&logoColor=white&style=for-the-badge" alt="Python">
  <img src="https://img.shields.io/badge/Flask-3.1-000?logo=flask&logoColor=white&style=for-the-badge" alt="Flask">
  <img src="https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white&style=for-the-badge" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white&style=for-the-badge" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black&style=for-the-badge" alt="JavaScript">
  <img src="https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white&style=for-the-badge" alt="SQLite">
</p>

<h1 align="center">Pink Urban Lists</h1>

<p align="center">
  <em>Listas simples que voc&ecirc; pode compartilhar.</em>
</p>

<p align="center">Gerenciador de tarefas minimalista, r&aacute;pido e bonito — feito para equipes e pessoas que valorizam simplicidade.</p>

---

## Table de Conteúdo

- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Quick Start](#quick-start)
- [Guia de Uso](#guia-de-uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Seguran&ccedil;a](#seguran&ccedil;a)
- [Deploy](#deploy)
- [Licen&ccedil;a](#licen&ccedil;a)

---

## Funcionalidades

### &check; Cria&ccedil;&atilde;o R&aacute;pida de Listas
Crie listas em segundos com um &uacute;nico clique. Sem formul&aacute;rios longos ou etapas desnecess&aacute;rias. Cada lista ganha um link &uacute;nico automaticamente.

### &check; Datas de Vencimento
Defina "hoje", "amanh&atilde;", "pr&oacute;xima semana" ou escolha no calendario. Itens atrasados ficam vermelhos, itens do dia ganham destaque rosa. Clique na data de qualquer item para alterar depois.

### &check; Drag &amp; Drop
Reordene seus itens arrastando e soltando — a nova ordem &eacute; salva automaticamente no servidor.

### &check; Edi&ccedil;&atilde;o Inline
Clique no nome de qualquer item para renomear. Pressione **Enter** para salvar ou **Esc** para cancelar. Sem modais, sem recarregar.

### &check; Vistas Separadas
Itens pendentes e conclu&iacute;dos em se&ccedil;&otilde;es distintas. Visualize o que falta fazer e o que j&aacute; foi completado.

### &check; Compartilhamento por Link
Um clique copia a URL. Envie para qualquer pessoa — quem receber pode visualizar a lista sem precisar de conta.

### &check; Sistema de Login e Aprova&ccedil;&atilde;o
Novos usu&aacute;rios se cadastram e aguardam aprova&ccedil;&atilde;o do administrador. Controle total sobre quem acessa o sistema.

### &check; Painel Administrativo
Aprove ou rejeite cadastros pendentes. Veja todos os usu&aacute;rios, promova para admin, visualize todas as listas da plataforma.

### &check; Altera&ccedil;&atilde;o de Senha
Clique no seu avatar na barra superior → **Configura&ccedil;&otilde;es** → altere sua senha a qualquer momento, com valida&ccedil;&atilde;o da senha atual.

### &check; Design Responsivo e Suave
Transi&ccedil;&otilde;es com `cubic-bezier`, hover animations, feedback visual. Funciona perfeitamente em desktop, tablet e celular.

---

## Tecnologias

| Camada | Tecnologia |
|---|---|
| **Backend** | Python 3.10+, Flask 3.1, Blueprint Architecture |
| **Database** | SQLite (SQLAlchemy ORM), migr&aacute;vel para PostgreSQL/MySQL |
| **Autentica&ccedil;&atilde;o** | Flask-Login, Werkzeug bcrypt (hash de senhas) |
| **Seguran&ccedil;a** | Flask-Talisman (CSP, HSTS, HPKP), Flask-Limiter (rate limiting) |
| **Frontend** | HTML5, CSS3 (Custom Properties, Animations), Vanilla JS |
| **Drag & Drop** | HTML5 Native Drag & Drop API |
| **Produ&ccedil;&atilde;o** | Gunicorn WSGI Server (4 workers), Procfile |
| **Deploy** | Railway, Render, Heroku, ou servidor pr&oacute;prio |

---

## Quick Start

### Requisitos

- Python 3.10 ou superior
- pip instalado

### Passos

```bash
# 1. Clone o reposit&oacute;rio
git clone https://github.com/mathvelozzo/TODO-List---Pink-Urban.git
cd TODO-List---Pink-Urban

# 2. Instale as depend&ecirc;ncias
pip install -r requirements.txt

# 3. Configure as vari&aacute;veis de ambiente
cp .env.example .env
# Edite .env e coloque uma SECRET_KEY forte

# 4. Rode a aplica&ccedil;&atilde;o
py run.py
```

Acesse **http://127.0.0.1:5000** no navegador.

### Primeiro Acesso

Na primeira execu&ccedil;&atilde;o, um usu&aacute;rio admin &eacute; criado automaticamente. A senha aparece no terminal:

```
Admin criado! Senha: abc123xyz — ALTERE NO PRIMEIRO ACESSO!
```

Esqueceu a senha? Rode `py reset_admin.py`.

---

## Guia de Uso

### Criando sua primeira lista

1. Cadastre-se na p&aacute;gina principal
2. Clique em **"Criar Nova Lista"**
3. Diga qual &eacute; o t&iacute;tulo e confirme
4. Clique em **"Abrir"** na lista criada

### Adicionando itens com data

1. Dentro da lista, digite o nome do item
2. Clique no &iacute;cone de calend&aacute;rio para abrir o seletor
3. Escolha: **Hoje**, **Amanh&atilde;**, **Pr&oacute;x. Semana** ou selecione a data
4. Clique em **"+ Adicionar"**

### Alterando datas de itens existentes

1. Clique na data ao lado do item (mesmo "Sem data")
2. Escolha uma nova data no calend&aacute;rio
3. Clique em **"Confirmar"** ou **"Limpar"**

### Reordenando itens

Segure e arraste qualquer item pendente — solte na posi&ccedil;&atilde;o desejada. A ordem &eacute; salva no servidor.

### Compartilhando

Na p&aacute;gina da lista, clique em **"Copiar Link"** — a URL vai para a &aacute;rea de transfer&ecirc;ncia.

### Alterando sua senha

1. Clique no seu avatar no topo da p&aacute;gina
2. Selecione **"Configura&ccedil;&otilde;es"**
3. Digite a senha atual, a nova senha e confirme

---

## Estrutura do Projeto

```
pink-urban-lists/
├── run.py                  # Entry point (desenvolvimento)
├── wsgi.py                 # WSGI entry point (produ&ccedil;&atilde;o)
├── app.py                  # Flask app factory + configura&ccedil;&otilde;es + seguran&ccedil;a
├── models.py               # Modelos: User, TodoList, ListItem
├── main.py                 # Rotas p&uacute;blicas + API CRUD de listas/itens
├── auth.py                 # Login, cadastro, logout, configura&ccedil;&otilde;es
├── admin.py                # Painel administrativo (aprovacoes, usuarios)
├── reset_admin.py          # Script para reset de senha do admin
├── requirements.txt        # Depend&ecirc;ncias Python
├── Procfile                # Configura&ccedil;&atilde;o para Railway/Heroku
├── .env.example            # Exemplo de vari&aacute;veis de ambiente
├── SECURITY.md             # Checklist completo de seguran&ccedil;a
│
├── static/
│   ├── css/
│   │   └── style.css       # Tema Pink Urban (anima&ccedil;&otilde;es, vari&aacute;veis CSS)
│   └── js/
│       └── main.js         # Utilit&aacute;rios JavaScript globais
│
└── templates/
    ├── base.html           # Layout base (navbar, flash messages, footer)
    ├── index.html          # Landing page (hero, features, social proof)
    ├── settings.html       # P&aacute;gina de configura&ccedil;&otilde;es (trocar senha)
    ├── login.html          # Tela de login
    ├── register.html       # Tela de cadastro
    ├── view_list.html      # Visualiza&ccedil;&atilde;o de lista (itens, drag, datas)
    └── admin/
        ├── base.html       # Layout do painel admin
        ├── dashboard.html  # Dashboard (usuarios pendentes, metricas)
        └── users.html      # Lista completa de usu&aacute;rios
```

---

## Seguran&ccedil;a

O projeto passou por um security review completo. Aqui est&aacute; o que foi implementado:

| Recurso | Descri&ccedil;&atilde;o |
|---|---|
| **bcrypt** | Senhas com hash forte via Werkzeug |
| **Rate Limiting** | 10 req/min no login, 5 req/min no cadastro |
| **CSP + Headers** | Flask-Talisman: X-Frame, HSTS, X-Content-Type |
| **Cookies Seguros** | HttpOnly, SameSite=Lax, Secure (em produ&ccedil;&atilde;o) |
| **Ownership Validation** | Usu&aacute;rios s&oacute; editam pr&oacute;prias listas |
| **Input Validation** | Regex no username, limites de tamanho |
| **Logging** | Tentativas de login falhas e trocas de senha |
| **Secret Key** | Exigida via env var (erro se ausente em produ&ccedil;&atilde;o) |

Veja o checklist completo em [SECURITY.md](SECURITY.md).

---

## Deploy

### Railway (Recomendado)

1. Acesse [railway.app](https://railway.app) → **New Project** → **Deploy from GitHub**
2. Selecione `TODO-List---Pink-Urban`
3. Adicione as vari&aacute;veis na aba **Variables**:

| Vari&aacute;vel | Valor |
|---|---|
| `SECRET_KEY` | (gerar com `python -c "import secrets; print(secrets.token_hex(32))"`) |
| `DATABASE_URL` | `sqlite:///pink_urban.db` |
| `SESSION_COOKIE_SECURE` | `true` |
| `FLASK_DEBUG` | `false` |

4. Deploy autom&aacute;tico via `Procfile` (Gunicorn)

### Servidor Pr&oacute;prio

```bash
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:8000 --workers 4 wsgi:application
```

Recomendado: coloque Nginx como reverse proxy na frente do Gunicorn e configure HTTPS com Let's Encrypt.

---

## Licen&ccedil;a

MIT — fa&ccedil;a o que quiser com esse c&oacute;digo.

---

<p align="center">Feito com carinho pela equipe <strong>Pink Urban</strong></p>
