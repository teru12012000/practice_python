import tkinter
from tkinter import filedialog
from pathlib import Path
import openpyxl

class Application(tkinter.Frame):
  def __init__(self,root=None):
    super().__init__(root,width=300,height=280,
                     borderwidth=1,relief='groove')
    self.root=root
    self.pack()
    self.pack_propagate(0)
    self.create_widgets()
    
  def create_widgets(self):
    quit_btn=tkinter.Button(self)
    quit_btn['text']='閉じる'
    quit_btn['command']=self.root.destroy
    quit_btn.pack(side='bottom')
    
    #テキストボックス
    self.text_box=tkinter.Entry(self)
    self.text_box['width']=10
    self.text_box.pack()
    
    #実行ボタン
    submit_btn=tkinter.Button(self)
    submit_btn['text']='実行'
    submit_btn['command']=self.save_handler
    submit_btn.pack()
    
    #メッセージ出力
    self.message=tkinter.Message(self)
    self.message.pack()
  
  def save_handler(self):
    text=self.text_box.get()
    file_name=tkinter.filedialog.askopenfilename(initialdir='./')
    
    wb=openpyxl.load_workbook(file_name)
    ws=wb.worksheets[0]
    ws['B1'].value=text
    wb.save(file_name)
    self.message['text']='保存完了'



root=tkinter.Tk()
root.title('サプー　アプリ')
root.geometry('400x300')
app=Application(root=root)
root.mainloop()