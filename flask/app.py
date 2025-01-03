# from flask import Flask, jsonify, render_template, request, redirect, url_for, session
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_sqlalchemy import SQLAlchemy


# app = Flask(__name__)

# app.secret_key = "your secret key"
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///users.db'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(120), nullable=False)


# @app.route('/')
# def home():
#     if 'username' in session:
#         return f"Hello, {session['username']}! <br> <a href='/logout'>Logout</a>"
#     return "<a href='/login'>Login</a> or <a href='/register'>Register</a>"


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == "POST":
#         username = request.form['username']
#         password = request.form['password']

#         if User.query.filter_by(username=username).first():
#             return redirect(url_for('register'))
        
#         hashed_password = generate_password_hash(password, method="pbkdf2:sha256")

#         new_user = User(username=username, password=hashed_password)

#         db.session.add(new_user)
#         db.session.commit()
#         return redirect(url_for('login'))
#     return render_template("register.html")

# @app.route('/login', methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form['username']
#         password = request.form['password']

#         user = User.query.filter_by(username=username).first()
#         if user and check_password_hash(user.password, password):
#             session['username'] = user.username
#             return redirect(url_for('home'))
#         else:
#             return "Invalid username or password"
    
#     return render_template("login.html")


# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     return redirect(url_for('home'))

# if __name__=='__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)












# გააკეთე create_blog(), edit_blog() და delete_blog() ფუნქციების იმპლემენტაცია !!!
# --------------------------------------------------------------------------------

from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "your secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///blog.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Routes
@app.route('/')
def home():
    if 'username' in session:
        blogs = Blog.query.all()
        return render_template("blogs.html", blogs=blogs)
    return "<a href='/login'>Login</a> or <a href='/register'>Register</a>"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if User.query.filter_by(username=username).first():
            return "Username already exists"

        hashed_password = generate_password_hash(password, method="pbkdf2:sha256")

        new_user = User(username=username, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['username'] = user.username
            session['user_id'] = user.id
            return redirect(url_for('home'))
        else:
            return "Invalid username or password"

    return render_template("login.html")

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_id', None)
    return redirect(url_for('home'))

@app.route('/create', methods=['GET', 'POST'])
def create_blog():
    ... # Todo!

@app.route('/edit/<int:blog_id>', methods=['GET', 'POST'])
def edit_blog(blog_id):
    ... # Todo!

@app.route('/delete/<int:blog_id>', methods=['POST'])
def delete_blog(blog_id):
    ... # Todo!

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)






    

# სვაგერის დოცუმენტაციის დაგენერირებაზე მორგებული კოდი !!!!!
# ----------------------------------------------------------

# from flask import Flask, request, session
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_sqlalchemy import SQLAlchemy
# from flask_restx import Api, Resource, fields

# app = Flask(__name__)

# # Configuration
# app.secret_key = "your secret key"
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///blog.db'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)
# api = Api(app, doc='/docs', title="Simple Blog API", description="API documentation for the simple blog")

# # Models
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(120), nullable=False)

# class Blog(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(150), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# # API Models
# user_model = api.model('User', {
#     'username': fields.String(required=True, description="Username"),
#     'password': fields.String(required=True, description="Password")
# })

# blog_model = api.model('Blog', {
#     'title': fields.String(required=True, description="Blog title"),
#     'content': fields.String(required=True, description="Blog content")
# })

# # Routes
# @api.route('/register')
# class Register(Resource):
#     @api.expect(user_model)
#     @api.response(201, 'User created successfully')
#     @api.response(400, 'User already exists')
#     def post(self):
#         """Register a new user"""
#         data = request.json
#         if User.query.filter_by(username=data['username']).first():
#             return {"message": "User already exists"}, 400
        
#         hashed_password = generate_password_hash(data['password'], method="pbkdf2:sha256")
#         new_user = User(username=data['username'], password=hashed_password)
        
#         db.session.add(new_user)
#         db.session.commit()
#         return {"message": "User created successfully"}, 201

# @api.route('/login')
# class Login(Resource):
#     @api.expect(user_model)
#     @api.response(200, 'Login successful')
#     @api.response(401, 'Invalid username or password')
#     def post(self):
#         """Authenticate user"""
#         data = request.json
#         user = User.query.filter_by(username=data['username']).first()
#         if user and check_password_hash(user.password, data['password']):
#             session['username'] = user.username
#             session['user_id'] = user.id
#             return {"message": "Login successful"}, 200
#         return {"message": "Invalid username or password"}, 401

# @api.route('/blogs')
# class Blogs(Resource):
#     @api.response(200, 'Success')
#     def get(self):
#         """Get all blogs"""
#         if 'username' not in session:
#             return {"message": "Unauthorized access"}, 401
        
#         blogs = Blog.query.all()
#         return [{"id": blog.id, "title": blog.title, "content": blog.content, "author_id": blog.author_id} for blog in blogs], 200

#     @api.expect(blog_model)
#     @api.response(201, 'Blog created successfully')
#     def post(self):
#         """Create a new blog"""
#         if 'username' not in session:
#             return {"message": "Unauthorized access"}, 401
        
#         data = request.json
#         new_blog = Blog(title=data['title'], content=data['content'], author_id=session['user_id'])
#         db.session.add(new_blog)
#         db.session.commit()
#         return {"message": "Blog created successfully"}, 201

# @api.route('/blogs/<int:blog_id>')
# class BlogDetails(Resource):
#     @api.response(200, 'Success')
#     @api.response(404, 'Blog not found')
#     def get(self, blog_id):
#         """Get a single blog by ID"""
#         blog = Blog.query.get_or_404(blog_id)
#         return {"id": blog.id, "title": blog.title, "content": blog.content, "author_id": blog.author_id}, 200

#     @api.expect(blog_model)
#     @api.response(200, 'Blog updated successfully')
#     @api.response(403, 'Unauthorized')
#     def put(self, blog_id):
#         """Update a blog"""
#         if 'username' not in session:
#             return {"message": "Unauthorized access"}, 401
        
#         blog = Blog.query.get_or_404(blog_id)
#         if blog.author_id != session['user_id']:
#             return {"message": "Unauthorized"}, 403
        
#         data = request.json
#         blog.title = data['title']
#         blog.content = data['content']
#         db.session.commit()
#         return {"message": "Blog updated successfully"}, 200

#     @api.response(200, 'Blog deleted successfully')
#     @api.response(403, 'Unauthorized')
#     def delete(self, blog_id):
#         """Delete a blog"""
#         if 'username' not in session:
#             return {"message": "Unauthorized access"}, 401
        
#         blog = Blog.query.get_or_404(blog_id)
#         if blog.author_id != session['user_id']:
#             return {"message": "Unauthorized"}, 403
        
#         db.session.delete(blog)
#         db.session.commit()
#         return {"message": "Blog deleted successfully"}, 200

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)
