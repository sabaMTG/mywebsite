from flask import Flask, render_template, redirect, url_for, flash
from forms import BlogPostForm

app = Flask(__name__)
app.secret_key = 'your_secret_key'

posts = []

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    form = BlogPostForm()
    if form.validate_on_submit():
        post = {
            'title': form.title.data,
            'content': form.content.data
        }
        posts.append(post)
        flash("Post created successfully!", "success")
        return redirect(url_for('view_posts'))
    return render_template('create_post.html', form=form)

@app.route('/posts')
def view_posts():
    return render_template('view_posts.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)