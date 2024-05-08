from flask import Flask, flash, render_template, redirect, url_for
from app.config import Config

from app.forms import MessageForm

app = Flask(__name__, static_url_path='', static_folder='static')
app.config.from_object(Config)


@app.route("/index")
@app.route("/", methods=['GET', 'POST'])
def index() -> str:
    form = MessageForm()
    if form.validate_on_submit():
        # TODO: Insert something the messages.
        flash('Message sent.')
        return redirect(url_for('index'))
    else:
        return render_template(
            'index.html',
            title="Khalid Abu Shawarib",
            form=form
        )

@app.route("/cv", methods=['GET'])
def cv():
    print("Hello")
    return redirect(url_for('static', filename='assets/cv.pdf'))


# These two lines are used only while developing.
# In production this code will be run as a module.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
