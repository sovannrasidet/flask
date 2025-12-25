# Security Checklist for Production Deployment

## Required Changes

### 1. Environment Variables
- [ ] Set a strong SECRET_KEY (generate with: python -c 'import secrets; print(secrets.token_hex(32))')
- [ ] Set FLASK_ENV=production
- [ ] Use production database (PostgreSQL/MySQL recommended)

### 2. Database Security
- [ ] Replace SQLite with PostgreSQL/MySQL for production
- [ ] Set up database user with limited permissions
- [ ] Enable database backups

### 3. Application Security
- [ ] Remove debug mode (already done in config)
- [ ] Add rate limiting
- [ ] Implement HTTPS
- [ ] Add CSRF protection (Flask-WTF provides this)

### 4. Additional Security
- [ ] Set up logging
- [ ] Add input validation
- [ ] Implement session security
- [ ] Add error handling

## Production Database Setup

### PostgreSQL (Recommended)
```bash
pip install psycopg2-binary
```

Update DATABASE_URL:
```
postgresql://username:password@host:port/database_name
```

### MySQL
```bash
pip install PyMySQL
```

Update DATABASE_URL:
```
mysql+pymysql://username:password@host:port/database_name
```
