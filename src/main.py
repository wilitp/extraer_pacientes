from getDict import get_dict
from pathlib import Path
import subprocess
from os import listdir
from datetime import date, timedelta
import pandas as pd
from tkinter import filedialog, Tk, Button, messagebox, Label, END, BOTTOM

path_to_dir = ""
output_file = ""

current_selection_prefix = "Selección.: "
def get_label_widget(initial):
    return Label(root,text=initial,height=1, width=60)
def set_input_dir():
    global path_to_dir
    path_to_dir = filedialog.askdirectory(initialdir="/")
    current_folder["text"] = current_selection_prefix + path_to_dir
    if path_to_dir != "":
        select_folder_btn["text"] = "Cambiar carpeta fuente"
    else:
        select_folder_btn["text"] = "Seleccionar carpeta fuente"

def set_output_file():
    global output_file
    output_file = filedialog.askopenfilename(initialdir="/")
    current_file["text"] = current_selection_prefix + output_file
    if output_file != "":
        select_output['text'] = "Cambiar archivo"
    else:
        select_output['text'] = "Seleccionar archivo"


def continue_handler():
    if output_file == "" or path_to_dir == "":
        messagebox.showinfo(message="Please select files first")
        return
    paths = listdir(path_to_dir)

    patient_dicts = []

    for path in paths:
        actual_path = path_to_dir + "/" + path
        my_dict = get_dict(actual_path)
        if my_dict != None:
            patient_dicts.append(my_dict)
        pass

    accident_ids = []
    names = []
    ids = []
    locations = []

    # Lista de aseguradoras de riesgo de trabajo
    arts = []

    appointment_date = date.today() + timedelta(days=-7)
    appointment_dates = []

    for patient_dicts in patient_dicts:
        accident_ids.append(patient_dicts["accident_id"])
        names.append(patient_dicts["patient_name"])
        locations.append(patient_dicts["patient_location"])
        ids.append(patient_dicts["patient_id"])
        arts.append("FEDERACION PATRONAL")
        appointment_dates.append(appointment_date.strftime("%d/%m/%Y"))

    df = pd.DataFrame({
        "ART": arts,
        "FECHA DE AUDITORIA": appointment_dates,
        "NOMBRE Y APELLIDO DEL PACIENTE": names,
        "SINIESTRO": accident_ids,
        "DNI/CUIT/CUIL": ids,
        "LOCALIDAD/PROVINCIA": locations,
    })

    df.to_excel(output_file, index=False)
    success["text"] = "Success!"
    print(str(Path(output_file)))
    subprocess.call(["start", str(Path(output_file))], shell=True)



root = Tk()
root.geometry('500x300')
current_folder = get_label_widget(current_selection_prefix)
current_file = get_label_widget(current_selection_prefix)
select_folder_btn = Button(root, text="Seleccionar carpeta fuente", command=set_input_dir)
select_output = Button(root, text="Seleccionar archivo", command=set_output_file)
continue_button = Button(root, text="Extraer", command=continue_handler)
success = Label(root, fg="green")
greeting = get_label_widget("Ingresá la carpeta con los archivos pdf y después el archivo de salida")


# Render elements
greeting.pack()
current_folder.pack()
select_folder_btn.pack()
current_file.pack()
select_output.pack()
continue_button.pack(side=BOTTOM)
success.pack()

root.mainloop()