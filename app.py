from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
#home page
def home_view():
  return render_template('home.html')
@app.route("/about")
#about page
def about_view():
  return render_template('about.html')
@app.route("/blog")
#blog list_page
def blog_list():
  return render_template('blog.html')
@app.route("/portfolio")
# project portfolio list
def portfolio_list():
  return render_template('portfolio.html')
@app.route("/contact")
#contact page
def contact_us():
  return render_template('contact.html')
if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)