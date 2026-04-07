# Pink Urban Lists

**Listas simples que voc&ecirc; pode compartilhar.**

Um gerenciador de tarefas minimalista — r&aacute;pido, intuitivo e f&aacute;cil de compartilhar. Sem cadastros desnecess&aacute;rios, sem complica&ccedil;&atilde;o.

---

## O que faz

| &nbsp; | &nbsp; |
|---|---|
| &check; | Listas r&aacute;pidas com datas de vencimento |
| 🔄 | Drag &amp; drop para reordenar itens |
| 🔗 | Compartilhe via link &uacute;nico |
| 👁️ | Visualiza&ccedil;&atilde;o separada: pendentes vs conclu&iacute;dos |
| ✏️ | Edi&ccedil;&atilde;o inline — clique e renomeie |
| 🔐 | Login, aprova&ccedil;&atilde;o de usu&aacute;rios e painel admin |
| 🛡️ | Rate limiting, CSP, senhas bcrypt, logs de seguran&ccedil;a |

## Como usar

**1.** Clone e instale:
```bash
git clone https://github.com/mathvelozzo/TODO-List---Pink-Urban.git
cd TODO-List---Pink-Urban
pip install -r requirements.txt
```

**2.** Configure:
```bash
cp .env.example .env
# Edite .env e coloque uma SECRET_KEY forte
```

**3.** Rode:
```bash
py run.py
```

Pronto — `http://127.0.0.1:5000`

> O admin &eacute; criado automaticamente na primeira execu&ccedil;&atilde;o.
> A senha aparece no terminal. Esqueceu? `py reset_admin.py`

## Deploy

O jeito mais r&aacute;pido &eacute; o **Railway** — conecta o GitHub, adiciona as vari&aacute;veis e sobe sozinho via `Procfile`:

| Vari&aacute;vel | Valor |
|---|---|
| `SECRET_KEY` | Sua chave &uacute;nica |
| `DATABASE_URL` | `sqlite:///pink_urban.db` |
| `SESSION_COOKIE_SECURE` | `true` |
| `FLASK_DEBUG` | `false` |

Ou qualquer servidor com Gunicorn:
```bash
gunicorn --bind 0.0.0.0:8000 --workers 4 wsgi:application
```

## Tech

Flask · SQLAlchemy · Flask-Login · Flask-Talisman · Flask-Limiter · Gunicorn · SQLite

Seguran&ccedil;a completa em [SECURITY.md](SECURITY.md)

---

MIT &middot; Pink Urban 2026
