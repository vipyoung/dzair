from flask import Flask, render_template, Response, redirect, url_for, request, session, abort
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user


app = Flask(__name__)

# config
app.config.update(
	DEBUG=True,
	SECRET_KEY='secret_xxx'
)

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):
	def __init__(self, name):
		self.id = name
		self.name = str(name)
		self.password = self.name + "_secret"

	def __repr__(self):
		return "%s/%s" % (self.name, self.password)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/twitter')
#@login_required
def twitter():
	return render_template('twitter.html')



@app.route('/lab')
def lab():
	return render_template('lab.html')

@app.route('/pricing')
def pricing():
	return render_template('pricing.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')


# somewhere to login
@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if password == "qarta" and username == "qcri":
			user = User(username)
			print user
			login_user(user)

			next = request.args.get('next')
			print next
			return redirect(next or url_for('index', _scheme="https"))
		else:
			return abort(401)
	else:
		return render_template('login.html')


# somewhere to logout
@app.route("/logout")
@login_required
def logout():
	logout_user()
	return render_template('index.html')


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
	return Response('<p>Login failed</p>')


# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
	return User(userid)
