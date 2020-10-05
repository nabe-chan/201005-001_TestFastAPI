from controllers import app, index, admin, register


# FastAPIのルーティング用関数
app.add_api_route("/", index)
app.add_api_route("/admin", admin)
# urls.py
# FastAPIのルーティング用関数
app.add_api_route("/", index)
app.add_api_route("/admin", admin)
app.add_api_route("/register", register, methods=["GET", "POST"])  # new
