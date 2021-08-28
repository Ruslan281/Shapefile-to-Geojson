## Created by Ruslan Huseynov

import os.path

import sys

try:
    import pkg_resources.py2_warn
    import pkg_resources.markers

except ImportError:
    pass

from fiona import crs
import fiona
import pyproj

from shapely.geometry import Point, Polygon, LineString

from geopandas import read_file

from geopandas import GeoDataFrame

from tkinter import filedialog

import tkinter.messagebox as Mesaj

try:
    import Tkinter as tk

except ImportError:
    import tkinter as tk


try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

root = tk.Tk()

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_compcolor = '#d9d9d9'
_ana1color = '#d9d9d9'
_ana2color = '#ececec'
font9 = "-family {Courier New} -size 8 -weight bold"
style = ttk.Style()
style.theme_use('winnative')
style.configure('.',background=_bgcolor)
style.configure('.',foreground=_fgcolor)
style.configure('.',font="TkDefaultFont")
style.map('.',background=[('selected', _compcolor),
                          ('active',_ana2color)])

root.geometry("602x322+824+279")
root.minsize(148, 1)
root.maxsize(3844, 1055)
root.resizable(False,False)
root.title("New Toplevel")
root.configure(background="#1a1a1a")
root.configure(highlightbackground="#d9d9d9")
root.configure(highlightcolor="black")
root.iconbitmap("db.ico")
root.title("Shapefile to Geojson")


ttt=tk.StringVar()



def Daxil_Et():
    daxil=filedialog.askopenfilename(initialdir="/", title="Shape faylı daxil edin",
                    filetypes=(("Shapefile", "*.shp"),("all files", "*.*")))
    ttt.set(daxil)


def Cevir():
    shape_file = read_file(Entry1.get())
    shape_cevir = shape_file.to_crs(epsg=4326)
    Path = filedialog.asksaveasfilename(initialdir="C:/Users/KTB/Desktop",title="Faylı saxlayacaqınız yeri seçin")


    shape_cevir.to_file(Path+".geojson",driver='GeoJSON')


    Mesaj.showinfo("Məlumat","ShapeFile GeoJson formatına çevrildi")


Button1 = tk.Button(root)
Button1.place(relx=0.133, rely=0.28, height=43, width=444)
Button1.configure(activebackground="#ececec")
Button1.configure(activeforeground="#000000")
Button1.configure(background="#1c3737")
Button1.configure(borderwidth="0")
Button1.configure(compound='center')
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(font="-family {Segoe UI} -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
Button1.configure(foreground="#c0c0c0")
Button1.configure(highlightbackground="#1c3737")
Button1.configure(highlightcolor="black")
Button1.configure(pady="0")
Button1.configure(text='''Shapefile daxil edin''')
Button1.configure(cursor="hand2")
Button1.configure(command=Daxil_Et)

Entry1 = tk.Entry(root)
Entry1.place(relx=0.133, rely=0.093,height=34, relwidth=0.738)
Entry1.configure(background="#c0c0c0")
Entry1.configure(borderwidth="1")
Entry1.configure(disabledforeground="#a3a3a3")
Entry1.configure(font=font9)
Entry1.configure(foreground="#000000")
Entry1.configure(highlightbackground="#d9d9d9")
Entry1.configure(highlightcolor="black")
Entry1.configure(insertbackground="black")
Entry1.configure(selectbackground="blue")
Entry1.configure(selectforeground="white")
Entry1.configure(textvariable=ttt)

TSeparator1 = ttk.Separator(root)
TSeparator1.place(relx=0.133, rely=0.466, relwidth=0.738)
TSeparator2 = ttk.Separator(root)
TSeparator2.place(relx=0.133, rely=0.528, relwidth=0.738)

Button2 = tk.Button(root)
Button2.place(relx=0.133, rely=0.59, height=43, width=444)
Button2.configure(activebackground="#ececec")
Button2.configure(activeforeground="#000000")
Button2.configure(background="#1c3737")
Button2.configure(borderwidth="0")
Button2.configure(disabledforeground="#a3a3a3")
Button2.configure(font="-family {Segoe UI} -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
Button2.configure(foreground="#c0c0c0")
Button2.configure(highlightbackground="#d9d9d9")
Button2.configure(highlightcolor="black")
Button2.configure(pady="0")
Button2.configure(text='''Geojson formatına çevir''')
Button2.configure(cursor="hand2")
Button2.configure(command=Cevir)


root.mainloop()
