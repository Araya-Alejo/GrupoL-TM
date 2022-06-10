import subprocess

def abrirPDF():
    path = 'TyC\AlquilaYa_TerminosyCondiciones.pdf'
    subprocess.Popen([path], shell=True)
