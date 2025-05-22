# Flask Template

A modern Flask starter project with user authentication, API, and modular structure.

## Quick Start

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd Flask_template
   ```

2. **Create a virtual environment and activate it**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**

   - Copy `.env.example` to `.env` and update values as needed.

5. **Run the app**
   ```bash
   flask run
   ```

## Database Migrations

1. **Initialize migrations (first time only):**
   ```bash
   flask db init
   ```
2. **Create a migration after model changes:**
   ```bash
   flask db migrate -m "Describe changes"
   ```
3. **Apply migrations:**
   ```bash
   flask db upgrade
   ```

## Generate requirements.txt

After installing new packages, update requirements:

```bash
pip freeze > requirements.txt
```

## Project Structure & Rules

To keep the codebase clean and consistent, follow these rules:

- **Blueprints:**

  - Place all route logic in `app/views/` using Blueprints (e.g., `main.py`, `auth.py`, `api.py`).
  - Register new Blueprints in `app/__init__.py`.

- **Models:**

  - Define each model in its own file in `app/models/`.
  - Import models in `app/models/__init__.py` for easy access.

- **Forms:**

  - Place all WTForms classes in `app/forms/`.
  - Group related forms in the same file (e.g., `auth.py` for login/register forms).

- **Utilities:**

  - Put helpers, validators, and decorators in `app/utils/`.
  - Use descriptive names and docstrings for all utility functions/classes.

- **Templates:**

  - Use `app/templates/` for HTML files.
  - Inherit from `base.html` for all pages.
  - Group related templates in subfolders (e.g., `auth/`, `errors/`).

- **Static Files:**

  - Store CSS, JS, and images in `app/static/`.
  - Use subfolders like `css/`, `js/`, `img/` for organization.

- **Configuration:**

  - Use `app/config.py` for all settings.
  - Never hardcode secrets; use environment variables and `.env` files.

- **Migrations:**

  - Use Flask-Migrate for all database changes.
  - Never edit migration files manually.

- **General:**
  - Write clear docstrings and comments.
  - Use snake_case for variables/functions, PascalCase for classes.
  - Keep functions short and focused.
  - Test your code before committing.

---

For more, see the code comments and structure. This template is ready for extension and learning!
