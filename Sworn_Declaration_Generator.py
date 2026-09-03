#Objetivo: pasar información deun excel a un documento PDF
#Autor : Ian Antonio Pérez Liska
#Lenguaje: Python
#versión de python: 3.12
#Procesos falntantes: ninguno
#Historia:
#         inicio: 19/6/2026
#         fin: 22/6/2026

#Entrada: documento excel a pasar y PDF a usar de plantilla
#Proceso: 
#       1. Leer cada fila del excel 
#       2. Ver cuantas columnas tiene
#       3. tomar la información de cada fila
#       4. meter esa información en el PDF
#       5. repetir el proceso hasta que ya no hallan más colunas por leer
#Salida: guardar todos los PDF con la información ingresada


#Librerías
from tkinter import * # interface gráfica
from tkinter import filedialog as f, messagebox as ms # para diálogos de selección de archivos y mensajes
import pandas as pd # para manipulación de datos en Excel
from pypdf import PdfReader, PdfWriter # para manipulación de archivos PDF
import datetime
import time

class App(Tk):
    def __init__(self):
        super().__init__()

        #configuración de la pantalla
        self.geometry('380x150')
        self.title('Declaraciones juradas - Startrack')
        self.config(bg='black')

        #Objetos de la interfaz
        Label(self, text='↓ Elige una opción ↓', bg='black', fg='white', font='arial 12').pack()
        Button(self, text='Generar', command=self.generar,width=20, height=5, bg='lightblue', font='arial 9').pack() # boton para la función de generar
    

    #Funcion para hacer el paso de excel a pdf
    def generar(self):
        current_time = datetime.datetime.fromtimestamp(time.time())
        info_df  = pd.DataFrame()
        
        try:
            ms.showinfo('Información', 'Selecciona el archivo Excel a procesar')
            excel_path = f.askopenfilename(filetypes=[('Excel', '*.xlsm *.xlsx')]) # abrir un diálogo para seleccionar el archivo Excel
            info_df = pd.read_excel(excel_path, sheet_name= "TEMPLATE")
        except:
            ms.showerror('Error', 'No se pudo leer el archivo Excel. Asegúrate de que el archivo tenga una hoja llamada "TEMPLATE".')
            return
        
        try:
            ms.showinfo('Información', "Selecciona el archivo que contiene el formato autorizado por PROVIAL.")
            pdf_template_path = f.askopenfilename(filetypes=[ ('PDF', '*.pdf') ])
            pdf_reader = PdfReader(pdf_template_path)
            
        except:
            ms.showerror('Error', 'Por favor verifica que el archivo que seleccionaste sea un PDF válido.')
            return
        
        try:
            
            ms.showinfo('Aviso', 'Elige la carpeta donde se guardarán los PDFs resultantes')
            ruta = f.askdirectory()
            
            for index, row in info_df.iterrows():
                Writer = PdfWriter()
                Writer.append((pdf_reader))
                
                field_values = {
                    'Certificate_Number' : row['Certificate_Number'],
                    'Address' : row['Address'],
                    'Day' : row['Day'],
                    'Month' : row['Month'],
                    'Year' : row['Year'],
                    'Client_Name' : row['Client_Name'],
                    'Client_Address' : row['Client_Address'],
                    'Client_Email' : row['Client_Email'],
                    'Client_Phone' : row['Client_Phone'],
                    'Vehicle_Circulation_Number' : row['Vehicle_Circulation_Number'],
                    'Vehicle_Correlative' : row['Vehicle_Correlative'],
                    'Vehicle_NIT'   : row['Vehicle_NIT'],
                    'Vehicle_Owner' : row['Vehicle_Owner'],
                    'Client_ID'     : row['Client_ID'],
                    'Vehicle_Use'   : row['Vehicle_Use'],
                    'Vehicle_Plate' : row['Vehicle_Plate'],
                    'Vehicle_Type'  : row['Vehicle_Type'],
                    'Vehicle_Make'  : row['Vehicle_Make'],
                    'Vehicle_Line'  : row['Vehicle_Line'],
                    'Vehicle_Model' : row['Vehicle_Model'],
                    'Vehicle_Chasis' : row['Vehicle_Chasis'],
                    'Vehicle_VIN'    : row['Vehicle_VIN'],
                    'Vehicle_Series' : row['Vehicle_Series'],
                    'Vehicle_Engine' : row['Vehicle_Engine'],
                    'Vehicle_Seats'  : row['Vehicle_Seats'],
                    'Vehicle_Axes'   : row['Vehicle_Axes'],
                    'Vehicle_Cilinders' : row['Vehicle_Cilinders'],
                    'Vehicle_Engine_Volume' : row['Vehicle_Engine_Volume'],
                    'Vehicle_Color' : row['Vehicle_Color'],
                    'Vehicle_Weight' : row['Vehicle_Weight'],
                    'Limiter_Model'  : row['Limiter_Model'],
                    'Limiter_Type'   : row['Limiter_Type'],
                    'Limiter_Maintenance' : row['Limiter_Maintenance'],
                    'Company_Register'    : 'STCPC-SLV-0004-2021',
                    'Company_Name'        : 'GPS Tecnología S.A.',
                    'Company_Register'    : '708711',
                    'Company_Folio'  : '927',
                    'Company_Book'   : '670',
                    'Company_Legal_Representative' : 'JOSÉ MANUEL TOBAR SOLARES',
                    'Company_Rep_Age' : '45 años',
                    'Company_Rep_Civil' : 'Casado',
                    'Company_Rep_Nationality' : 'Guatemalteco',
                    'Company_Rep_Profession'  : 'Perito Contador',
                    'Company_Rep_Register'    : '770534',
                    'Company_Rep_Folio' : '25',
                    'Company_Rep_Book'  : '841',
                    'Company_Address'   : 'vía 4, 1-30 zona 4, Campus Tec 1 oficina 304, Ciudad de Guatemala',
                    'Company_Phone'     : '3195 7694',
                    'Declaration_Address' : 'la Ciudad de Guatemala',
                    'Declaration_Day'  : row['Day'],
                    'Declaration_Month' : row['Month'],
                    'Declaration_Year'  : '2026',
                    'Declaration_Hour'  : current_time.strftime("%H:%M"),
                    'Declaration_Rep_Name'  :  'JOSÉ MANUEL TOBAR SOLARES',
                    'Declaration_Rep_Relation' : 'Representante legal',
                    'Declaration_Company_Name' : 'GPS Tecnología S.A.',
                    'Declaration_Company_Address' : 'vía 4, 1-30 zona 4, Campus Tec 1 oficina 304, Ciudad de Guatemala',
                    'Declaration_Certificate' : row['Certificate_Number'],
                    'Declaration_Minutes' : '3'       
                }
                
                for page in Writer.pages:
                    
                    Writer.update_page_form_field_values(page, field_values)
                    
                with open(f"{ruta}/Declaracion_Jurada_{row['Vehicle_Plate']}.pdf", "wb") as o:
                    Writer.write(o)
            
                current_time += datetime.timedelta(minutes=3)
            
            ms.showinfo('Información', "Se crearon las declaraciones juradas correctamente.")
                
            
        except:
            ms.showerror('Error', 'Ocurrió un error, por favor revisa tus plantillas.')    
        
        
            
            
        


App().mainloop()
