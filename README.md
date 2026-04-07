# Pink Urban Lists

> Listas simples que você pode compartilhar.

Um gerenciador de tarefas minimalista e colaborativo, pensado para ser rápido, intuitivo e fácil de compartilhar. Inspirado na simplicidade do [Flask.io](https://flask.io), com a identidade visual da **Pink Urban**.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-E91E8C?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1-000?logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-E91E8C)

</div>

---

## ✨ Funcionalidades

- **Criação rápida** — crie listas em segundos, sem friccao
- **Datas de vencimento** — defina "hoje", "amanha", "proxima semana" ou escolha no calendario
- **Indicadores visuais** — itens atrasados em vermelho, itens de hoje em destaque rosa
- **Compartilhamento por link** — copie a URL e qualquer pessoa acessa a lista
- **Sistema de aprovacao** — novos usuarios precisam de aprovacao do admin
- **Painel administrativo** — aprove/rejeite usuarios, veja metricas
- **Design smooth** — transicoes suaves, hover animations, feedback visual em cada acao
- **Totalmente responsivo** — funciona em desktop, tablet e mobile

## 🚀 Quick Start

### Requisitos

- Python 3.11+

### Instalacao

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

Na primeira execucao, um usuario admin e criado automaticamente. A senha e exibida no console:

```
[!] Admin criado. Senha: xyz123abc — ALTERE NO PRIMEIRO ACESSO!
```

Faça login como `admin` e a senha exibida para acessar o painel administrativo.

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

1. Clique na data exibida ao lado de qualquer item
2. Escolha uma nova data no calendario
3. Clique em **"Confirmar"**

### Compartilhando

1. Na pagina da lista, clique em **"Copiar Link"**
2. Envie o link para qualquer pessoa
3. Quem receber pode visualizar a lista

## 🏗️ Estrutura do Projeto

```
.
├── run.py                  # Entry point (nao rode debug em producao)
├── app.py                  # Flask app factory + configuracoes
├── models.py               # Modelos: User, TodoList, ListItem
├── main.py                 # Rotas publicas + API CRUD de listas/itens
├── auth.py                 # Login, cadastro e logout
├── admin.py                # Painel administrativo
├── requirements.txt        # Dependencias Python
├── .env.example            # Exemplo de variaveis de ambiente
├── SECURITY.md             # Checklist de seguranca
├── README.md               # Este arquivo
├── static/
│   ├── css/style.css       # Estilos completos (tema Pink Urban)
│   └── js/main.js          # JS utilitario
└── templates/
    ├── base.html           # Layout base
    ├── index.html          # Pagina principal
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
- Cookies de sessao com `HttpOnly` e `SameSite=Lax`
- Senha admin gerada aleatoriamente na primeira execucao
- `.env` no `.gitignore` — secrets nunca vao pro repositorio

Veja o checklist completo em [SECURITY.md](SECURITY.md).

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

## 🛣️ Próximos Passos

- [ ] Rate limiting nas rotas de autenticacao
- [ ] CSRF tokens nas requicoes AJAX
- [ ] HTTPS em producao
- [ ] Migracao para PostgreSQL
- [ ] WebSockets para atualizacao em tempo real
- [ ] Listas compartilhadas (multi-dono)
- [ ] Categorias e tags
- [ ] Drag & drop para reordenar itens

## 📄 Licenca

MIT

---

Feito com 💗 por **Pink Urban**
