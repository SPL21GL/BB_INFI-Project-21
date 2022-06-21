from flask import Blueprint, request, render_template, flash
import sqlalchemy
from werkzeug.utils import redirect

from Forms.add.stellplatz import AddStellplatz
from Forms.delete.stellplatz import DeleteStellplatz
from Forms.edit.stellplatz import EditStellplatz
from model.models import db, Stellplatz

stellplatz_blueprint = Blueprint('stellplatz_blueprint', __name__)


@stellplatz_blueprint.route("/stellplatz", methods=["GET", "POST"])
def stellplatz():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    page = request.args.get('page', 1, type=int)
    stellplaetze = session.query(Stellplatz).order_by(Stellplatz.StellplatzId).paginate(
        page, 10, error_out=False)

    return render_template("/stellplatz/stellplatz.html", stellplaetze=stellplaetze)


@stellplatz_blueprint.route("/stellplatz/stellplatz_add", methods=["GET", "POST"])
def stellplatz_add():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    add_stellplatz_form = AddStellplatz()

    if request.method == 'POST':
        if add_stellplatz_form.validate_on_submit():
            new_stellplatz = Stellplatz()

            new_stellplatz.KategorieId = add_stellplatz_form.KategorieId.data
            new_stellplatz.Qualitaet = add_stellplatz_form.Qualitaet.data
            new_stellplatz.Laenge = add_stellplatz_form.Laenge.data
            new_stellplatz.Breite = add_stellplatz_form.Breite.data
            db.session.add(new_stellplatz)
            db.session.commit()

            try:
                db.session.add(new_stellplatz)
                db.session.commit()
            except:
                add_stellplatz_form = AddStellplatz()
                return render_template("/stellplatz/stellplatz_add.html", form=add_stellplatz_form)

            return redirect("/stellplatz")
        else:
            return render_template("stellplatz/stellplatz_add.html", form=add_stellplatz_form)
    else:
        return render_template("stellplatz/stellplatz_add.html", form=add_stellplatz_form)


@stellplatz_blueprint.route("/stellplatz/stellplatz_edit", methods=["GET", "POST"])
def stellplatz_edit():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    edit_stellplatz_form = EditStellplatz()

    StellplatzId = request.args["StellplatzId"]

    stellplatz_to_edit = session.query(Stellplatz).filter(
        Stellplatz.StellplatzId == StellplatzId).first()

    if request.method == "POST":
        if edit_stellplatz_form.validate_on_submit():
            StellplatzId = edit_stellplatz_form.StellplatzId.data
            stellplatz_to_edit = db.session.query(Stellplatz).filter(
                Stellplatz.StellplatzId == StellplatzId).first()

            stellplatz_to_edit.KategorieId = edit_stellplatz_form.KategorieId.data
            stellplatz_to_edit.Qualitaet = edit_stellplatz_form.Qualitaet.data
            stellplatz_to_edit.Laenge = edit_stellplatz_form.Laenge.data
            stellplatz_to_edit.Breite = edit_stellplatz_form.Breite.data
            stellplatz_to_edit.Hoehe = edit_stellplatz_form.Hoehe.data

            db.session.commit()
        return redirect("/stellplatz")
    else:
        edit_stellplatz_form.StellplatzId.data = stellplatz_to_edit.StellplatzId
        edit_stellplatz_form.KategorieId.data = stellplatz_to_edit.KategorieId
        edit_stellplatz_form.Qualitaet.data = stellplatz_to_edit.Qualitaet
        edit_stellplatz_form.Laenge.data = stellplatz_to_edit.Laenge
        edit_stellplatz_form.Breite.data = stellplatz_to_edit.Breite
        edit_stellplatz_form.Hoehe.data = stellplatz_to_edit.Hoehe

        return render_template("stellplatz/stellplatz_edit.html", form=edit_stellplatz_form)


@stellplatz_blueprint.route("/stellplatz/delete_stellplatz", methods=["GET", "POST"])
def stellplatz_delete():
    delete_stellplatz_form = DeleteStellplatz()
    if delete_stellplatz_form.validate_on_submit():
        StellplatzId = delete_stellplatz_form.StellplatzId.data
        stellplatz_to_delete = db.session.query(Stellplatz).filter(
            Stellplatz.StellplatzId == StellplatzId)
        stellplatz_to_delete.delete()
        db.session.commit()
    return redirect("/stellplatz")

