# Discord Integration
API com o objetivo de permitir que o `basset-bot-rails` possa fazer com que o Basset Bot tome ações, além de notificar mensagens novas.

## Setup

Criar .env (lembre-se de trocar os valores do .env para os valores desejados)

```bash
cp .env{.example,}
```

Criar venv

```bash
python3 -m venv venv
```

Ativar venv(necessário sempre no terminal)

```bash
source venv/bin/activate
```

Instalar dependências

```bash
pip install -r requirements.txt
```

Consertar erro na lib `pafy`

```bash
cp libfix/backend_youtube_dl.py venv/lib/python3.8/site-packages/pafy/backend_youtube_dl.py
```

## Executar (em desenvolvimento)

```bash
flask run
```



