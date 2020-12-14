from flask import render_template, request, Blueprint
from quotes.requests import get_random_quotes
from quotes.models import Post
from flask_login import login_required




main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page = page, per_page=5)
    return render_template('home.html', posts = posts)

@main.route("/blogs")
def blogs():
    quotes = get_random_quotes()
    return render_template('blogs.html', title = 'About', quotes= quotes)

