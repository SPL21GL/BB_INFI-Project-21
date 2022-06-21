from flask import Blueprint, request, render_template, flash
import sqlalchemy
from werkzeug.utils import redirect

from Forms.add.kategorie import AddKategorie
from Forms.delete.kategorie import DeleteKategorie
from Forms.edit.kategorie import EditKategorie
from model.models import db, Kategorie

kategorie_blueprint = Blueprint('kategorie_blueprint', __name__)


@kategorie_blueprint.route("/kategorie", methods=["GET", "POST"])
def kategorie():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    page = request.args.get('page', 1, type=int)
    kategories = session.query(Kategorie).order_by(Kategorie.KategorieId).paginate(
        page, 10, error_out=False)

    return render_template("/kategorie/kategorie.html", kategories=kategories)


@kategorie_blueprint.route("/kategorie/kategorie_add", methods=["GET", "POST"])
def kategorie_add():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    add_kategorie_form = AddKategorie()

    if request.method == 'POST':
        if add_kategorie_form.validate_on_submit():
            new_kategorie = Kategorie()

            new_kategorie.Kategoriename = add_kategorie_form.Kategoriename.data
            new_kategorie.Preis = add_kategorie_form.Preis.data
            new_kategorie.Videoueberwachung = add_kategorie_form.Videoueberwachung.data
            new_kategorie.Versicherung = add_kategorie_form.Versicherung.data
            new_kategorie.Farbe = add_kategorie_form.Farbe.data

            try:
                db.session.add(new_kategorie)
                db.session.commit()
            except:
                flash("An Exception is raised")
                add_kategorie_form = AddKategorie()
                return render_template("/kategorie/kategorie_add.html", form=add_kategorie_form)

            return redirect("/kategorie")
        else:
            return render_template("kategorie/kategorie_add.html", form=add_kategorie_form)
    else:
        return render_template("kategorie/kategorie_add.html", form=add_kategorie_form)


@kategorie_blueprint.route("/kategorie/kategorie_edit", methods=["GET", "POST"])
def kategories_edit():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    edit_kategorie_form = EditKategorie()

    KategorieId = request.args["KategorieId"]

    kategorie_to_edit = session.query(Kategorie).filter(
        Kategorie.KategorieId == KategorieId).first()

    if request.method == "POST":
        if edit_kategorie_form.validate_on_submit():
            KategorieId = edit_kategorie_form.KategorieId.data
            kategorie_to_edit = db.session.query(Kategorie).filter(
                Kategorie.KategorieId == KategorieId).first()

            kategorie_to_edit.Kategoriename = edit_kategorie_form.Kategoriename.data
            kategorie_to_edit.Preis = edit_kategorie_form.Preis.data
            kategorie_to_edit.Videoueberwachung = edit_kategorie_form.Videoueberwachung.data
            kategorie_to_edit.Versicherung = edit_kategorie_form.Versicherung.data
            kategorie_to_edit.Farbe = edit_kategorie_form.Farbe.data
            db.session.commit()
        return redirect("/kategorie")
    else:
        edit_kategorie_form.KategorieId.data = kategorie_to_edit.KategorieId
        edit_kategorie_form.Kategoriename.data = kategorie_to_edit.Kategoriename
        edit_kategorie_form.Preis.data = kategorie_to_edit.Preis
        edit_kategorie_form.Videoueberwachung.data = kategorie_to_edit.Videoueberwachung
        edit_kategorie_form.Versicherung.data = kategorie_to_edit.Versicherung
        edit_kategorie_form.Farbe.data = kategorie_to_edit.Farbe

        return render_template("kategorie/kategorie_edit.html", form=edit_kategorie_form)


@kategorie_blueprint.route("/kategorie/delete_kategorie", methods=["GET", "POST"])
def kategories_delete():
    delete_kategorie_form = DeleteKategorie()
    if delete_kategorie_form.validate_on_submit():
        KategorieId = delete_kategorie_form.KategorieId.data
        kategorie_to_delete = db.session.query(Kategorie).filter(
            Kategorie.KategorieId == KategorieId)
        kategorie_to_delete.delete()
        db.session.commit()
    return redirect("/kategorie")

