from flask import Flask, render_template, redirect, request
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
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=datetime.now().isoformat())
    
    def __repr__(self):
        return f'<Task {self.id}>'

# Routes to Web Pages
# Home Page
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        current_task = request.form['content']
        new_task = NewTask(content=current_task)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return "There was an issue adding your task"
# List all current tasks
    else:
        tasks = NewTask.query.order_by(NewTask.created_at).all()
        return render_template("index.html", tasks=tasks)



# Update a task
@app.route("/update", methods=['GET', 'POST'])
def update():
    return render_template("update.html")

# Delete a task
@app.route("/delete", methods=['GET', 'POST'])
def delete():
    return render_template("delete.html")


# Run and Debug
if __name__ in "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)