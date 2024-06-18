from app import app, db

# Инициализация базы данных
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
