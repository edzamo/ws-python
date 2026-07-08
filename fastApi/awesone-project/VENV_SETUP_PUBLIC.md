# FastAPI Virtual Environment Setup (Public Version)

This file explains how to set up a Python virtual environment for your FastAPI project in a public-safe way.
This is intended for the project root where you are actually developing, not a parent folder.

---

## What your project structure should look like

If your working folder is:

```bash
/Users/ezamora/Documents/Personal/github/ws-python/fastApi/awesone-project
```

then `awesone-project` is your project root.

You should create the virtual environment inside that project folder, not in the parent `fastApi` folder.

Ideal structure:

```text
fastApi/
  awesone-project/
    .venv/
    main.py
    VENV_SETUP_PUBLIC.md
    ...
```

---

## 1. Create the virtual environment in the project root

From the project root, run:

```bash
cd /path/to/your/project/awesone-project
python3 -m venv .venv
```

This creates a `.venv` folder inside your current project.

> Use `python3` so the environment is created with the system Python 3 interpreter.

---

## 2. Activate the virtual environment

Always activate the environment before installing packages or running your app.

From the project root:

```bash
source .venv/bin/activate
```

If you are in a subfolder inside the project, use a relative path back to the project root:

```bash
source ../.venv/bin/activate
```

Important:
- the file is `activate`, not `active`
- the environment folder is `.venv`

---

## 3. Install FastAPI

With the virtual environment active, install FastAPI with the recommended extra dependencies:

```bash
pip install "fastapi[standard]"
```

This installation includes Uvicorn and other common dependencies used in FastAPI projects.

---

## 4. Run your FastAPI app

The recommended command is:

```bash
python -m uvicorn main:app --reload
```

This starts your app from `main.py` and reloads automatically when code changes.

> Avoid using `fastapi dev` as your main launch command. `uvicorn` is the standard runner.

---

## 5. Verify the active environment

After activation, check that the `python` command points to the `.venv` folder:

```bash
which python
```

The output should show something like:

```bash
/path/to/your/project/awesone-project/.venv/bin/python
```

If the path points outside `.venv`, the environment is not active.

---

## 6. Fix architecture mismatch issues

If you see an error like:

```text
incompatible architecture (have 'arm64', need 'x86_64')
```

then your Python interpreter and installed package binaries are not built for the same CPU architecture.

To fix it:

1. Remove the old environment:

```bash
rm -rf .venv
```

2. Recreate it:

```bash
python3 -m venv .venv
```

3. Activate and reinstall packages:

```bash
source .venv/bin/activate
pip install --upgrade pip
pip install "fastapi[standard]"
```

---

## 7. Ignore the virtual environment in Git

Add a `.gitignore` file to prevent `.venv` from being committed.

Inside the project root:

```bash
echo ".venv/" > .gitignore
```

You can also add common ignores like:

```text
__pycache__/
*.py[cod]
.DS_Store
.vscode/
.env
```

---

## 8. Deactivate when finished

When you are done working, turn off the virtual environment with:

```bash
deactivate
```

---

## Why this setup is best

- Keeps dependencies isolated inside the project
- Avoids confusing cross-project package problems
- Makes the project portable and safe to share in public repositories
- Prevents leaking personal or machine-specific paths

If you want, I can also help rename the existing `VENV_SETUP.md` file and keep only this public-safe version in your project.
