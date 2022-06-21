from flask import Blueprint, request, render_template, flash
import sqlalchemy
from werkzeug.utils import redirect

from Forms.add.autos import AddAuto
from Forms.delete.autos import DeleteAuto
from Forms.edit.autos import EditAuto
from model.models import db, Auto

autos_blueprint = Blueprint('autos_blueprint', __name__)


@autos_blueprint.route("/autos", methods=["GET", "POST"])
def autos():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    page = request.args.get('page', 1, type=int)
    autos = session.query(Auto).order_by(Auto.AutoId).paginate(
        page, 10, error_out=False)

    return render_template("/autos/autos.html", autos=autos)


@autos_blueprint.route("/autos/autos_add", methods=["GET", "POST"])
def autos_add():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    add_autos_form = AddAuto()

    if request.method == 'POST':
        if add_autos_form.validate_on_submit():
            new_auto = Auto()

            new_auto.Kategorie = add_autos_form.Kategorie.data
            new_auto.Kennzeichen = add_autos_form.Kennzeichen.data
            new_auto.Laenge = add_autos_form.Laenge.data
            new_auto.Breite = add_autos_form.Breite.data
            new_auto.Hoehe = add_autos_form.Hoehe.data

            try:
                db.session.add(new_auto)
                db.session.commit()
            except:
                flash("An Exception is raised")
                add_autos_form = AddAuto()
                return render_template("/autos/auto_add.html", form=add_autos_form)

            return redirect("/autos")
        else:
            return render_template("autos/auto_add.html", form=add_autos_form)
    else:
        return render_template("autos/auto_add.html", form=add_autos_form)


@autos_blueprint.route("/autos/auto_edit", methods=["GET", "POST"])
def autos_edit():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    edit_auto_form = EditAuto()

    AutoId = request.args["AutoId"]

    auto_to_edit = session.query(Auto).filter(
        Auto.AutoId == AutoId).first()

    if request.method == "POST":
        if edit_auto_form.validate_on_submit():
            AutoId = edit_auto_form.AutoId.data
            auto_to_edit = db.session.query(Auto).filter(
                Auto.AutoId == AutoId).first()

            auto_to_edit.Kategorie = edit_auto_form.Kategorie.data
            auto_to_edit.Kennzeichen = edit_auto_form.Kennzeichen.data
            auto_to_edit.Laenge = edit_auto_form.Laenge.data
            auto_to_edit.Breite = edit_auto_form.Breite.data
            auto_to_edit.Hoehe = edit_auto_form.Hoehe.data
            db.session.commit()
        return redirect("/autos")
    else:
        edit_auto_form.AutoId.data = auto_to_edit.AutoId
        edit_auto_form.Kategorie.data = auto_to_edit.Kategorie
        edit_auto_form.Kennzeichen.data = auto_to_edit.Kennzeichen
        edit_auto_form.Laenge.data = auto_to_edit.Laenge
        edit_auto_form.Breite.data = auto_to_edit.Breite
        edit_auto_form.Hoehe.data = auto_to_edit.Hoehe

        return render_template("autos/auto_edit.html", form=edit_auto_form)


@autos_blueprint.route("/autos/delete_auto", methods=["GET", "POST"])
def autos_delete():
    delete_auto_form = DeleteAuto()
    if delete_auto_form.validate_on_submit():
        AutoId = delete_auto_form.AutoId.data
        auto_to_delete = db.session.query(Auto).filter(
            Auto.AutoId == AutoId)
        auto_to_delete.delete()
        db.session.commit()
    return redirect("/autos")

