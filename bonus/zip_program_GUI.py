import FreeSimpleGUI as sg

label1 = sg.Text("Select File to compress:")
input1 = sg.Input()
chosse_button1 = sg.FileBrowse('Select')


label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
chosse_button2 = sg.FolderBrowse('Select')

compress_button = sg.Button("Compress")

window = sg.Window('File Compressor', layout=[[label1,input1,chosse_button1],
                                              [label2,input2,chosse_button2],
                                              [compress_button]
                                              ])
window.read()
window.close()


