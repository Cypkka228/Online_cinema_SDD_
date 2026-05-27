from app import app, db
from app import views

# ========== МАРШРУТЫ ==========

# Публичные страницы
app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/movie/<int:movie_id>', view_func=views.movie_detail, methods=['POST', 'GET'])
app.add_url_rule('/search', view_func=views.movie_search)
app.add_url_rule('/about', view_func=views.about)
app.add_url_rule('/dmca', view_func=views.dmca)
app.add_url_rule('/contacts', view_func=views.contacts)
app.add_url_rule('/rules', view_func=views.rules)

# API
app.add_url_rule('/api/movies', view_func=views.api_movies)

# Аккаунт
app.add_url_rule('/account/register', view_func=views.user_register, methods=['POST', 'GET'])
app.add_url_rule('/account/login', view_func=views.user_login, methods=['POST', 'GET'])
app.add_url_rule('/account/logout', view_func=views.user_logout)

# Админ — категории
app.add_url_rule('/admin/category/create', view_func=views.admin_category_create, methods=['POST', 'GET'])
app.add_url_rule('/admin/category/list', view_func=views.admin_category_list)
app.add_url_rule('/admin/category/<int:category_id>/update', view_func=views.admin_category_update, methods=['POST', 'GET'])
app.add_url_rule('/admin/category/<int:category_id>/delete', view_func=views.admin_category_delete, methods=['POST', 'GET'])

# Админ — фильмы
app.add_url_rule('/admin/movie/create', view_func=views.admin_movie_create, methods=['POST', 'GET'])
app.add_url_rule('/admin/movie/list', view_func=views.admin_movie_list)
app.add_url_rule('/admin/movie/<int:movie_id>/update', view_func=views.admin_movie_update, methods=['POST', 'GET'])
app.add_url_rule('/admin/movie/<int:movie_id>/delete', view_func=views.admin_movie_delete, methods=['POST', 'GET'])


# ========== ЗАПУСК ==========

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("✅ База данных готова!")
        print("🌐 Запуск на http://127.0.0.1:5002")
    app.run(debug=True, port=5002)
