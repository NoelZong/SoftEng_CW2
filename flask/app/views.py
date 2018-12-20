from flask import render_template, flash, redirect, session, url_for, request, g
from flask_admin.contrib.sqla import ModelView
from flask_wtf.csrf import CsrfProtect
 

from app import app, db, admin
from .models import Note
from .forms import NoteForm

admin.add_view(ModelView(Note, db.session))



@app.route('/note_create', methods=['GET','POST'])
def note_create():
    form = NoteForm()
    flash('Errors="%s"' %
          (form.errors))
    if form.validate_on_submit():
        t = Note(content=form.content.data, date=form.date.data, title=form.title.data)
        db.session.add(t)
        db.session.commit()
        return redirect('/')
    return render_template('create.html',
                           title='Create Note',
                           form=form)

@app.route('/', methods=['GET'])
def root():
    note = Note.query.all()
    return render_template('list.html',
                           title='View All',
                           note=note)

@app.route('/list_false', methods=['GET'])
def list_false():
    note = Note.query.filter(Note.status==False).all()
    return render_template('list.html',
                           title='False Notes',
                           note=note)

@app.route('/list_true', methods=['GET'])
def list_true():
    note = Note.query.filter(Note.status==True).all()
    return render_template('list.html',
                           title='True Notes',
                           note=note)

@app.route('/note_edit/<id>', methods=['GET','POST'])
def note_edit(id):
    note = Note.query.get(id)
    form = NoteForm(obj = note)

    if form.validate_on_submit():
        t = note
        t.title = form.title.data
        t.content = form.content.data
        t.date = form.date.data
        db.session.commit()
        return redirect('/')
    return render_template('edit.html',
                           title='Edit Note',
                           form=form)

@app.route('/note_delete/<id>', methods=['GET'])
def note_delete(id):
    note = Note.query.get(id)
    db.session.delete(note)
    db.session.commit()
    return redirect('/')

@app.route('/note_change_true/<id>', methods=['GET'])
def note_change_true(id):
    note = Note.query.get(id)
    note.status=True
    db.session.commit()
    return redirect('/')

@app.route('/note_change_false/<id>', methods=['GET'])
def note_change_false(id):
    note = Note.query.get(id)
    note.status=False
    db.session.commit()
    return redirect('/')

CsrfProtect(app)
#csrf保护