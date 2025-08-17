# -----------------------------------------------
# Note : These test.py is server based program which has endpoint contain 403 sc
#        If you want testing purpose you can run these in terminal and in another 
#        terminal you have to main.py 
#        How to run => python test.py
# -----------------------------------------------

from flask import Flask, request, abort

app = Flask(__name__)

# Catch all routes
@app.route('/', defaults={'path': ''}, methods=["GET","POST","PUT","DELETE","PATCH","OPTIONS","HEAD","TRACE"])
@app.route('/<path:path>', methods=["GET","POST","PUT","DELETE","PATCH","OPTIONS","HEAD","TRACE"])
def catch_all(path):
    full_path = "/" + path
    method = request.method
    headers = request.headers

    # =========================
    # 1. PATH TRICKS
    # =========================
    bypass_paths = [
        "/secret/", "/SECRET", "/Secret", "/sEcReT",
        "/secret..;/", "/secret%2e%2e%2f", "/secret/./", "/secret//",
        "/secret%20", "/secret%09", "/secret%0d%0a",  # whitespace tricks
        "/%2fsecret", "/.%2fsecret", "/..%2fsecret",
        "/secret;.html", "/secret;.css", "/secret;.json",
        "/secret%2F", "/secret/%2e", "/secret/%2e%2e/",
    ]
    if full_path in bypass_paths:
        return f"Path bypass worked! ({full_path})\n"

    # =========================
    # 2. QUERY STRING TRICKS
    # =========================
    if full_path.startswith("/secret") and (
        request.query_string.decode() in [
             "?", "?anything", "?redirect", "?/", "?%2e", "?..;/", "?foo=bar"
        ]
    ):
        return f"Query bypass worked! ({full_path}{request.query_string.decode()})\n"

    # =========================
    # 3. HEADER TRICKS
    # =========================
    proxy_headers = {
        "X-Original-URL": "/secret",
        "X-Rewrite-URL": "/secret",
        "X-Forwarded-Path": "/secret",
        "X-Forwarded-Url": "/secret",
        "Referer": "/secret"
    }
    for h, v in proxy_headers.items():
        if headers.get(h) == v:
            return f"Header bypass worked! ({h})\n"

    if headers.get("X-Custom-Bypass") == "1":
        return "Custom header bypass worked!\n"

    # =========================
    # 4. METHOD TRICKS
    # =========================
    if full_path.endswith("/secret") and method in ["HEAD","OPTIONS","TRACE"]:
        return f"Method bypass worked! ({method})\n"

    # =========================
    # 5. MIXED EXTENSIONS
    # =========================
    if full_path in ["/secret.php", "/secret.asp", "/secret.json", "/secret.txt/"]:
        return f"Mixed extension bypass worked! ({full_path})\n"

    # =========================
    # DEFAULT RULE
    # =========================
    if full_path == "/secret":
        abort(403)

    abort(404)


if __name__ == "__main__":
    print("🚀 Running HARD 403 bypass practice server on http://127.0.0.1:8080/secret")
    app.run(port=8080, debug=True)
