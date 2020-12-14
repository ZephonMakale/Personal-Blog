from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from quotes import db
from quotes.models import Post, Comment
from quotes.posts.forms import PostForm, CommentForm

posts = Blueprint('posts', __name__)

@posts.route("/post/new", methods = ['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title = form.title.data, content = form.content.data, author = current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created successfully!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title = 'New Post', form = form, legend = 'New Post')

@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@posts.route("/post/<int:post_id>/update", methods = ['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title = 'Update Post', form = form, legend = 'Update Post')

@posts.route("/post/<int:post_id>/delete", methods = ['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))

@posts.route("/comment/<int:id>/comment", methods = ['GET','POST'])
@login_required
def new_comment(id):
    all_comments = Post.query.filter_by(id =id).all()
    postComments = Comment.query.filter_by(post_id = id).all()
    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(post_id=id, comment=comment, user=current_user)
        new_comment.save_comment()
    return render_template('comment.html', all_comments= all_comments, postComment=postComments, form= form)