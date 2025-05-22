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

---

For more, see the code comments and structure. This template is ready for extension and learning!
