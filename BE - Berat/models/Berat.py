from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Berat(db.Model):
    __tablename__ = 'berats'
    tanggal = db.Column(db.Date, primary_key=True)
    berat_min = db.Column(db.Integer)
    berat_max = db.Column(db.Integer)
    
    def __init__(self, tanggal, berat_min, berat_max):
        self.set_tanggal(tanggal)
        self.set_berat_min(berat_min)
        self.set_berat_max(berat_max)
        
    def get_tanggal(self):
        return str(self.tanggal)
    
    def set_tanggal(self, tanggal):
        self.tanggal = tanggal
    
    def get_berat_min(self):
        return int(self.berat_min)
    
    def set_berat_min(self, berat):
        self.berat_min = int(berat)
    
    def get_berat_max(self):
        return int(self.berat_max)
    
    def set_berat_max(self, berat):
        self.berat_max = int(berat)
    
    def get_perbedaan(self):
        return self.get_berat_max() - self.get_berat_min()
