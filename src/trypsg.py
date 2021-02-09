import PySimpleGUIQt as sg
import pandas as pd
import sweetviz as sv
from datetime import datetime

sg.theme('dark teal 9')

# sg.theme_previewer()
# Black, DarkTeal9, DarkBlue2, DarkGrey6

ftypes = (('Excel', '*.xls'), ('Excel', '*.xlsx'))

layout = [
    [sg.I('Select File', key='-FILE-'), sg.FileBrowse('Browse', file_types=ftypes)],
    [sg.B('OK', bind_return_key=True), sg.B('Cancel')],
]

window = sg.Window('ml4all', layout, font='Any 14', element_padding=(5, 5))


def on_ok():
    print(values['-FILE-'])
    df = pd.read_excel(values['-FILE-'])

    c = df.select_dtypes(include=['object']).columns
    df[c] = df[c].fillna('NA').apply(str)
    # i = df.select_dtypes(include=['int']).columns
    # df[i] = df[i].fillna(0).apply(int)
    # f = df.select_dtypes(include=['float'])
    # df[f] = df[f].fillna(0.0).apply(float)
    # d = df.select_dtypes(include=['datetime'])
    # df[d] = df[d].fillna(datetime(1900, 1, 1)).apply(datetime)


    my_report = sv.analyze(df)
    my_report.show_html()


while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Cancel'):
        break
    elif event == 'OK':
        on_ok()

print(window.QTApplication)
window.close()
