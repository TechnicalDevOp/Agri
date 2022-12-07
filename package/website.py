from flask import Blueprint, render_template

website_print = Blueprint('website', __name__)


@website_print.route('/', methods=['GET', 'POST'])
def home():
    return render_template('website/home.html', title='Home')
