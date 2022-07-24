import datetime
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from models.Berat import Berat

def index():
    berats = Berat.query.order_by(Berat.tanggal.desc()).all()
    args = request.args
    return render_template('index.html', berats=berats, **args)

def show(tgl):
    berat = Berat.query.filter(Berat.tanggal == tgl).first()
    if not berat: return '', 404
    return render_template('show.html', berat=berat)

def add_form():
    args = request.args
    return render_template('form.html', action='add', **args)

def add():
    tanggal = request.form.get('tanggal', None)
    berat_min = request.form.get('berat-min', None)
    berat_max = request.form.get('berat-max', None)
    
    (tanggal, berat_min, berat_max), (messages, valid), _ = validate_form(tanggal, berat_min, berat_max)
    
    if valid['tanggal'] and Berat.query.filter(Berat.tanggal == tanggal).first():
        messages['error_tanggal'] = f'Tanggal sudah terdapat pada database.'
        valid['tanggal'] = False
        
    if not (valid['tanggal'] and valid['berat_min'] and valid['berat_max']):
        return redirect(url_for('berat_bp.add_form', tanggal=tanggal, berat_min=berat_min, berat_max=berat_max, **messages))
    
    berat = Berat(tanggal, berat_min, berat_max)
    db.session.add(berat)
    db.session.commit()
    
    messages['success'] = f'Berhasil menambahkan data dengan tanggal {tanggal}, berat min {berat_min}, berat max {berat_max}.'
    
    return redirect(url_for('berat_bp.index', **messages))

def update_form(tgl):
    args = dict(request.args)
    if 'tanggal' not in args and 'berat_min' not in args and 'berat_max' not in args:
        berat = Berat.query.filter(Berat.tanggal == tgl).first()
        if not berat: return '', 404
        args['tanggal'] = berat.get_tanggal()
        args['berat_min'] = berat.get_berat_min()
        args['berat_max'] = berat.get_berat_max()    
    return render_template('form.html', tgl=tgl, action='update', **args)

def update(tgl):
    tanggal = request.form.get('tanggal', None)
    berat_min = request.form.get('berat-min', None)
    berat_max = request.form.get('berat-max', None)
    
    (tanggal, berat_min, berat_max), (messages, valid), _ = validate_form(tanggal, berat_min, berat_max)
    
    if valid['tanggal'] and Berat.query.filter(Berat.tanggal == tanggal).first() and str(tanggal) != tgl:
        messages['error_tanggal'] = f'Tanggal sudah terdapat pada database.'
        valid['tanggal'] = False
    
    if not (valid['tanggal'] and valid['berat_min'] and valid['berat_max']):
        return redirect(url_for('berat_bp.update_form', tgl=tgl, tanggal=tanggal, berat_min=berat_min, berat_max=berat_max, **messages))
    
    berat = db.session.query(Berat).filter(Berat.tanggal == tgl).first()
    if not berat: return '', 404
    berat.set_tanggal(tanggal)
    berat.set_berat_min(berat_min)
    berat.set_berat_max(berat_max)
    db.session.commit()
    
    messages['success'] = f'Berhasil mengubah data tanggal {tgl} menjadi tanggal {tanggal}, berat min {berat_min}, berat max {berat_max}.'
    
    return redirect(url_for('berat_bp.index', **messages))

def delete():
    tanggal = request.form.get('tanggal', None)
    tanggal, valid = validate_tanggal(tanggal)
    
    if valid and not Berat.query.filter(Berat.tanggal == tanggal).first():
        valid = False
        
    if not valid: return '', 404
    
    berat = db.session.query(Berat).filter(Berat.tanggal == tanggal).first()
    db.session.delete(berat)
    db.session.commit()
    
    messages = dict()
    messages['success'] = f'Berhasil menghapus data pada tanggal {tanggal}'
    
    return redirect(url_for('berat_bp.index', **messages))
    
def validate_tanggal(tanggal):
    try:
        year, month, day = map(int, tanggal.split('-'))
        tanggal = datetime.date(year, month, day)
        status = True
    except:
        status = False
    return tanggal, status

def validate_berat(berat):
    try:
        berat = int(berat)
        status = True
    except:
        status = False
    if status and berat < 0:
        status = False
    return berat, status

def validate_form(tanggal, berat_min, berat_max):
    messages = dict()
    valid = dict()
    
    tanggal, valid['tanggal'] = validate_tanggal(tanggal)
    if not valid['tanggal']: messages['error_tanggal'] = 'Tanggal tidak valid.'
    
    berat_min, valid['berat_min'] = validate_berat(berat_min)
    if not valid['berat_min']: messages['error_berat_min'] = 'Berat min tidak valid.'
    
    berat_max, valid['berat_max'] = validate_berat(berat_max)
    if not valid['berat_max']: messages['error_berat_max'] = 'Berat max tidak valid.'
    
    if valid['berat_min'] and valid['berat_max'] and berat_min > berat_max:
        messages['error_berat_min'] = messages['error_berat_max'] = f'Berat max harus lebih besar atau sama dengan berat min.'
        valid['berat_min'] = valid['berat_max'] = False
    
    status = True
    for _, s in valid.items():
        if not s: status = False
    
    return (tanggal, berat_min, berat_max), (messages, valid), status