# Day 26: Flask web app   (pip install flask)
# Run: python quickstart/day_26.py   then open http://127.0.0.1:5000/analyze
from flask import Flask, render_template_string, request

app = Flask(__name__)

PAGE = '''
<form method="post">
  <textarea name="content"></textarea>
  <button>Analyze</button>
</form>
{% if words is not none %}<p>{{ words }} words</p>{% endif %}
'''


@app.route('/')                                  # URL -> function
def home():
    return 'Home page'


@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    words = None
    if request.method == 'POST':                 # form was submitted
        content = request.form['content']        # matches <textarea name="content">
        words = len(content.split())
    return render_template_string(PAGE, words=words)


if __name__ == '__main__':
    app.run(debug=True)                          # debug=True reloads when you save
