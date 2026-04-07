# Security Checklist - Pink Urban Lists

## ✅ Implementado
- [x] Senhas com hash bcrypt (werkzeug.security)
- [x] Flask-Login com @login_required em rotas protegidas
- [x] SQLAlchemy parameterized queries (anti SQL injection)
- [x] .env no .gitignore
- [x] Admin random password generation on first run
- [x] Session cookies com HttpOnly e SameSite
- [x] Ownership check nas APIs (donos so podem editar proprias listas)
- [x] HTML escaping no frontend (escapeHtml)
- [x] Rate limiting — Flask-Limiter (10/min login, 5/min cadastro)
- [x] Security headers — Flask-Talisman (CSP, X-Frame-Options, X-Content-Type-Options, HSTS)
- [x] Input sanitization com html.escape nas rotas de auth
- [x] Username validation regex (apenas chars seguros)
- [x] Failed login logging (logger integrado)
- [x] SESSION_COOKIE_SECURE configuravel via env var
- [x] SECRET_KEY forte gerada via secrets.token_hex(32)
- [x] WSGI entry point (wsgi.py) para Gunicorn

## ⚠️ Para producao (depende do ambiente)
- [ ] Configurar HTTPS (Let's Encrypt)
- [ ] Mudar SESSION_COOKIE_SECURE=true no .env
- [ ] Mudar FORCE_HTTPS=true no .env
- [ ] Database migra para PostgreSQL/MySQL

## Como rodar localmente
1. `pip install -r requirements.txt`
2. Configure `.env` com sua SECRET_KEY
3. `python run.py`
4. Acesse `http://127.0.0.1:5000`

## Como rodar em producao (Gunicorn)
1. `pip install -r requirements.txt`
2. Configure `.env` (SESSION_COOKIE_SECURE=true, FORCE_HTTPS=true)
3. `gunicorn --bind 0.0.0.0:8000 --workers 4 wsgi:application`
4. Use Nginx como reverse proxy na frente do Gunicorn
