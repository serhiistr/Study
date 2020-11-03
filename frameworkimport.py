from bottle import route, run

@route("/first-page")
def first_page():
    return "<H1 align='centre'>Питон через браузер!</H1>"

run(host="localhost", port=8080, debug=True)