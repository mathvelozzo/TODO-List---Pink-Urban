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

## ⚠️ Para producao
- [ ] Ativar SESSION_COOKIE_SECURE = True (requer HTTPS)
- [ ] Rate limiting nas rotas de login/cadastro (Flask-Limiter)
- [ ] CSRF tokens nas rotas AJAX (Flask-WTF)
- [ ] Helmet-like headers (Talisman)
- [ ] Input sanitization adicional no backend
- [ ] Log de tentativas de login falhas
- [ ] Trocar SECRET_KEY para uma chave unica forte
- [ ] Configurar HTTPS (Let's Encrypt)
- [ ] Database migra para PostgreSQL/MySQL

## Como rodar
1. `pip install -r requirements.txt`
2. Configure `.env` com sua SECRET_KEY
3. `python run.py`
4. Acesse `http://127.0.0.1:5000`
