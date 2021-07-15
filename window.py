import tkinter as tk
from tkinter.constants import E, END, LEFT, W
from xlsxwriter import Workbook
from datetime import datetime
import os.path
from combinations import *

# define a variable for the result (can be changed by the 'calculate' function)
num = 0

# define the supportive functions
def make_it_brief(s):
    """Write numbers with more than 7 digits in exponential form"""
    if len(s) > 7:
        new_s = s[:1] + '.' + s[1:3] 
        if  int(s[4]) >= 5:
            new_s += f'{int(s[3]) + 1}' + "*" + f'10^{len(s) - 1}'
        else:
            new_s += f'{int(s[3])}' + "*" + f'10^{len(s) - 1}'
    else:
        new_s = s
    
    return new_s


def calculate():
    """Combinations or Permutations Calculator"""
    global num
    n = n_entry.get()
    k = k_entry.get()
    
    try:
        n = int(n)
    except:
        r = "Παρακαλώ εισάγετε μόνο θετικούς ακέραιους αριθμούς."
    else:
        try:
            k = int(k)
        except:
           r = "Παρακαλώ εισάγετε μόνο θετικούς ακέραιους αριθμούς." 
        else:
            if k > n:
                r = "Πρέπει n ≥ r. Προσπάθησε ξανά."
            else:
                if order_var.get() == 0:
                    num = count_combinations(n, k)
                    r = make_it_brief(str(num))
                
                elif order_var.get() == 1:
                    num = count_permutations(n, k)
                    r = make_it_brief(str(num))
    
    result.delete('1.0', END)
    result.insert(1.0, r)
                

def clear():
    """Clear the entries and the result text."""
    n_entry.delete(0, END)
    k_entry.delete(0, END)
    result.delete('1.0', END)


def to_excel():
    """Save num (the result) in the first cell of an XLSX file, 
    named with the word 'result' followed by the current date and time."""
    
    str_now = datetime.now().strftime(" %m-%d-%Y %Hh%Mm") 
    file_path = os.path.expanduser("~") + '/Desktop/result' + str_now +".xlsx"
    new_wb = Workbook(file_path)
    sheet = new_wb.add_worksheet()
    sheet.write("A1", num)
    new_wb.close()


# desine the window app
root = tk.Tk()
root.geometry("700x700")
root.title("Combinations and Permutations Calculator")

fr = tk.Frame(root)

main_title = tk.Label(fr, text="Combinations and Permutations Calculator", font=('Calibri', 24))
main_title.grid(row=0, column=0, pady=(10, 5), columnspan=2)

sub_title = tk.Label(fr, text="Create r-element groups choosing from a set of  n elements", font=('Calibri', 16))
sub_title.grid(row = 1, column = 0, pady=(5, 10), columnspan=2)

## entries
n_label = tk.Label(fr, text="n = ", font=('Calibri', 18))
n_label.grid(row = 2, column = 0, pady = 5, sticky=E)

n_entry = tk.Entry(fr, font=('Calibri', 18), width=5)
n_entry.grid(row = 2, column = 1, pady = 10, sticky=W)

k_label = tk.Label(fr, text="r = ", font=('Calibri', 18))
k_label.grid(row = 3, column = 0, pady = 10, sticky=E)

k_entry = tk.Entry(fr, font=('Calibri', 18), width=5)
k_entry.grid(row = 3, column = 1, pady = 10, sticky=W)

fr.pack()

# Radio buttons
fr2 = tk.Frame(root)
sub_title = tk.Label(fr2, text="Does order matter in the r-element groups?", font=('Calibri', 16))
sub_title.grid(row = 1, column = 0, pady=(20, 5), columnspan=2)

order_var = tk.IntVar()
order_var.set(1)

order_rbutton1 = tk.Radiobutton(fr2, text="Order matters", font=('Calibri', 14), 
                                variable=order_var, value=1) 
order_rbutton1.grid(row = 2, column = 0, columnspan=2, pady=(5, 0))

order_rbutton2 = tk.Radiobutton(fr2, text="Order doesn't matter", font=('Calibri', 14),
                                variable=order_var, value=0)
order_rbutton2.grid(row = 3, column = 0, columnspan=2, pady=(10, 0))

fr2.pack()

## buttons
fr3 = tk.Frame(root)
btn_calc = tk.Button(fr3, text='Calculate', font=('Calibri', 16), bg='#e6273d', command=calculate)
btn_calc.grid(row = 1, column = 1, pady=(20, 0), padx=(10,100))

btn_clear = tk.Button(fr3, text='Clear', font=('Calibri', 16), bg='#cccccc', command=clear)
btn_clear.grid(row = 1, column = 0, pady=(20, 0), padx=(0,0))

btn_save = tk.Button(fr3, text='Save result', font=('Calibri', 16), bg='#84d9ab', command=to_excel)
btn_save.grid(row = 1, column = 2, pady=(20, 0), padx=(100,0))

fr3.pack()

## text with the result
fr4 = tk.Frame(root)
result = tk.Text(fr4, font=('Calibri', 18))
result.grid(row = 2, column = 0, columnspan=2, pady =(40, 0))

fr4.pack()

root.mainloop()