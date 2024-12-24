from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# My App Setup
app = Flask(__name__)
Scss(app)

# Database Setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

# Models
class NewTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=datetime.now().isoformat())
    
    def __repr__(self):
        return f'<Task {self.id}>'

# Routes to Web Pages
@app.route("/")
def index():
    return render_template("index.html")


# Run and Debug
if __name__ in "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)