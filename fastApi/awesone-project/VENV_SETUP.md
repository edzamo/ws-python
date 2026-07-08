# Virtual Environment Setup for FastAPI Project

## Project location

These instructions assume your project root is the folder where your repository lives.

A common convention is to keep the virtual environment inside the project root in a hidden folder named `.venv`.

---

## 1. Create the virtual environment

If you need to create it again for a new project, run this inside the project root:

```bash
cd /path/to/your/project
python -m venv .venv
```

This creates a `.venv` directory inside your project.

> `python -m venv .venv` means:
> - `python`: use the Python interpreter
> - `-m venv`: run the built-in `venv` module
> - `.venv`: create the virtual environment folder named `.venv`

---

## 2. Activate the virtual environment

From the project root, activate the environment using the relative path:

```bash
source .venv/bin/activate
```

If you are in a subfolder, use the relative path to the project root. For example, if you are in `awesone-project` and the environment is in the parent folder:

```bash
source ../.venv/bin/activate
```

Important:
- the script is called `activate`, not `active`
- the environment folder is `.venv`, not `bin`

---

## 3. Verify the environment is active

After activation, check that `python` points to `.venv`:

```bash
which python
```

Expected output should show the `.venv` folder in your project, for example:

```bash
/path/to/your/project/.venv/bin/python
```

If it shows a path outside `.venv`, the environment is not active.

---

## 4. Upgrade pip (recommended)

Once activated, upgrade `pip` inside the virtual environment:

```bash
python -m pip install --upgrade pip
```

If `pip` is missing, use:

```bash
python -m ensurepip --upgrade
```

---

## 5. Ignore the virtual environment in Git

Add a `.gitignore` file inside `.venv` to avoid committing the environment:

```bash
echo "*" > .venv/.gitignore
```

This tells Git to ignore all files inside `.venv`.

---

## 6. Install project packages

Install packages while the environment is active:

```bash
pip install "fastapi[standard]"
```

Or install from `requirements.txt` if you have one:

```bash
pip install -r requirements.txt
```

---

## 7. Deactivate when finished

When you finish work, exit the virtual environment with:

```bash
deactivate
```

---

## Why use a virtual environment?

A virtual environment isolates package dependencies per project.
Without it, global Python packages may conflict between different projects.
Using `.venv` keeps each project independent and prevents version collisions.
