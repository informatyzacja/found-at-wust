# backend

Setup:

```sh
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Run the development server:

```sh
pnpm dev
```

or

```sh
uvicorn main:app --reload
```
