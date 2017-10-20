from Model.Model import Usuarios, db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime



class Usuario():


    def login(self, email, senha):
        try:
            usuario = db.session.query(Usuarios).filter(Usuarios.email == email).first()
            if email == usuario.email and senha == usuario.senha:
                return usuario
            else:
                return None
        except Exception as e:
            print e
            return None



    def find_by_id(self, id):
        return db.session.query(Usuarios).filter(Usuarios.id == id).first()