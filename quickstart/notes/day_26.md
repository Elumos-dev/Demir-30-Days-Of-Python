In a real project, move the HTML into files:
1. `templates/analyze.html` holds the form, and the route returns `render_template('analyze.html', words=words)`.
2. `templates/layout.html` holds the shared header and nav. Other pages start with `{% extends 'layout.html' %}` and fill `{% block content %}{% endblock %}`.
3. CSS goes in `static/css/main.css`, linked with `{{ url_for('static', filename='css/main.css') }}`.
4. Heroku has had no free plan since November 2022. Deploy free on Render or PythonAnywhere instead.
