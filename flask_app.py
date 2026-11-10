# ---------------------------------------------------------------
# Mon premier site Web avec Flask
# ---------------------------------------------------------------
# Ce fichier reçoit les demandes des navigateurs et fabrique les réponses.

from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Flask, abort, jsonify, redirect, render_template, request

app = Flask(__name__)


@app.get("/")
def accueil():
    return render_template("accueil.html")


@app.get("/presentation")
def presentation():
    return render_template(
        "presentation.html",
        prenom="Alexandre",
        nom="",
        loisirs=["Coder", "Jouer"],
    )


@app.get("/loisirs")
def loisirs():
    return render_template("loisirs.html", loisirs=["Coder", "Jouer"])


@app.get("/bonjour/<prenom>")
def bonjour(prenom):
    # Jinja échappe les données utilisateur pour éviter l'injection HTML.
    return render_template("bonjour.html", prenom=prenom)


@app.get("/calcul")
def calcul():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
    except (TypeError, ValueError):
        abort(400)

    operation = request.args.get("op", "plus")
    if operation == "fois":
        resultat = f"{a} × {b} = {a * b}"
    elif operation == "moins":
        resultat = f"{a} − {b} = {a - b}"
    elif operation == "divise":
        if b == 0:
            abort(400)
        resultat = f"{a} ÷ {b} = {a / b:g}"
    elif operation == "plus":
        resultat = f"{a} + {b} = {a + b}"
    else:
        abort(400)
    return render_template("resultat.html", titre="Calcul", resultat=resultat)


@app.get("/formulaire")
def formulaire():
    return render_template("formulaire.html")


@app.route("/salut", methods=["GET", "POST"])
def salut():
    donnees = request.form if request.method == "POST" else request.args
    prenom = donnees.get("prenom", "inconnu").strip() or "inconnu"
    ville = donnees.get("ville", "nulle part").strip() or "nulle part"
    couleurs_autorisees = {"tomato", "teal", "royalblue"}
    couleur = donnees.get("couleur", "teal")
    if couleur not in couleurs_autorisees:
        couleur = "teal"
    return render_template(
        "salut.html",
        prenom=prenom,
        ville=ville,
        couleur=couleur,
        methode=request.method,
    )


@app.get("/home")
def home():
    return redirect("/")


@app.get("/secret")
def secret():
    abort(403)


@app.errorhandler(403)
def acces_interdit(erreur):
    return render_template("403.html"), 403


@app.errorhandler(404)
def page_introuvable(erreur):
    return render_template("404.html"), 404


@app.get("/moi")
def moi():
    # On ne publie pas l'adresse IP complète dans cette page de démonstration.
    ip = request.headers.get("X-Real-IP", request.remote_addr) or "inconnue"
    ip_masquee = ".".join(ip.split(".")[:-1] + ["x"]) if "." in ip else "masquée"
    return render_template(
        "moi.html",
        ip=ip_masquee,
        navigateur=request.headers.get("User-Agent", "inconnu"),
        langues=request.headers.get("Accept-Language", "non renseignées"),
        entetes=request.headers.items(),
    )


@app.get("/api/heure")
def api_heure():
    maintenant = datetime.now(ZoneInfo("Europe/Paris"))
    return jsonify(
        {
            "heure": maintenant.strftime("%H:%M:%S"),
            "date": maintenant.strftime("%d/%m/%Y"),
            "message": "Bonjour depuis mon API !",
        }
    )


@app.get("/horloge")
def horloge():
    return render_template("horloge.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
