# AluGotTalent

AluGotTalent is a platform designed for learners to showcase their talents, connect with sponsors, and participate in various competitions. It is especially geared toward students and sponsors within the ALU (African Leadership University) community, providing a digital space to manage talent profiles, competitions, and success stories.

## Features

- **User Authentication:** Allows users to create accounts as students, sponsors, or admins. Login and registration are handled securely.
- **Talent Showcase:** Students can upload and share their talents (including video links), categorize them, and provide descriptions.
- **Competitions:** The platform manages and displays ongoing and upcoming competitions. Admins can add, update, or remove competitions.
- **Success Stories:** A dedicated section to highlight achievements and outstanding performances among talents.
- **Sponsor Management:** Admins can register, manage company profiles, and see the list of talents they have sponsored.
- **Search and Filtering:** Users can search for talents or competitions by category or specific keywords.
- **Admin Dashboard:** Provides KPIs on active competitions, sponsors, and success stories, plus quick actions to manage platform content.

## Screenshots

> _To be added by repository maintainers (suggested: screenshots of talent list, competitions page, admin dashboard, profile management)._

## Technologies Used

- **Frontend:** HTML, Bootstrap 5
- **Backend:** Flask (Python)
- **Templating:** Jinja2 (for dynamic content in HTML templates)
- **Database:** SQLite (default), Flask-Migrate for dynamic database migrations (supports PostgreSQL/MySQL/other SQL databases)
- **Other:** JavaScript for client-side interactions

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/aziza20-ux/AluGotTalent.git
cd AluGotTalent
```

### 2. Create and activate a virtual environment (optional, but recommended)

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install Python dependencies

The project uses `Flask`, `Flask-Migrate`, and possibly other packages listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present, install the basics:

```bash
pip install flask flask_sqlalchemy flask_migrate
```

### 4. Database Setup and Migration

By default, SQLite is used (for other options, adjust the `SQLALCHEMY_DATABASE_URI` in your config).

**Initialize migration environment:**
```bash
flask db init
```

**Generate migration (creates tables, etc):**
```bash
flask db migrate -m "Initial migration."
```

**Apply migration (create/update your database schema):**
```bash
flask db upgrade
```

_Repeat `migrate` and `upgrade` whenever you change models._

#### Using PostgreSQL/MySQL instead of SQLite:

1. Change the `SQLALCHEMY_DATABASE_URI` in your configuration file (example for PostgreSQL):
   ```
   postgresql://username:password@localhost/your_db
   ```
2. Ensure you have the appropriate drivers installed:
   ```bash
   pip install psycopg2           # for PostgreSQL
   pip install mysqlclient        # for MySQL
   ```

### 5. Run the development server

```bash
export FLASK_APP=App
flask run
```
> On Windows use `set FLASK_APP=App`

Open `http://localhost:5000` in your browser.

## Folder Structure

- `App/templates/` – HTML templates for all user-facing and admin pages (login, register, profile, competitions, etc.).
- `App/static/` – Static files such as CSS, JS, and images.

## Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request

## License

_This project currently does not specify a license. Please refer to the repository or contact a maintainer for more information._

---

© copyright reserved by AluGotTalent

**More info:** [AluGotTalent on GitHub](https://github.com/aziza20-ux/AluGotTalent)

> _Note: This README was generated based on available project files. [View code search results for details](https://github.com/search?q=repo%3Aaziza20-ux%2FAluGotTalent+AluGotTalent&type=code)._
