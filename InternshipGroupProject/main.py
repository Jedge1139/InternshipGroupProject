import select
import update
import delete
import insert

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview


app = Tk()
frame_search = Frame(app)
frame_search.grid(row=0, column=0)

lbl_search = Label(frame_search, text='Search by Internship',
                   font=('bold', 12), pady=20)
lbl_search.grid(row=0, column=0, sticky=W)
internship_search = StringVar()
internship_search_entry = Entry(frame_search, textvariable=internship_search)
internship_search_entry.grid(row=0, column=1)

lbl_search = Label(frame_search, text='Search by Query',
                   font=('bold', 12), pady=20)
lbl_search.grid(row=1, column=0, sticky=W)
query_search = StringVar()
query_search.set("SELECT * FROM internship where internship_name = 'software developer'")
query_search_entry = Entry(frame_search, textvariable=query_search, width=40)
query_search_entry.grid(row=1, column=1)

frame_fields = Frame(app)
frame_fields.grid(row=1, column=0)

frame_router = Frame(app)
frame_router.grid(row=4, column=0, columnspan=4, rowspan=6, pady=20, padx=20)

columns = ['id', 'Internship Name', 'Internship ID', 'Salary', 'Company']
router_tree_view = Treeview(frame_router, columns=columns, show="headings")
router_tree_view.column("id", width=40)
for col in columns[1:]:
    router_tree_view.column(col, width=120)
    router_tree_view.heading(col, text=col)
router_tree_view.bind('<<TreeviewSelect>>')
router_tree_view.pack(side="left", fill="y")
scrollbar = Scrollbar(frame_router, orient='vertical')
scrollbar.configure(command=router_tree_view.yview)
scrollbar.pack(side="right", fill="y")
router_tree_view.config(yscrollcommand=scrollbar.set)

frame_fields = Frame(app)
frame_fields.grid(row=1, column=0)
# Internship ID
internship_ID_text = StringVar()
internship_ID_label = Label(frame_fields, text='Internship ID', font=('bold', 12))
internship_ID_label.grid(row=0, column=0, sticky=E)
internship_ID_entry = Entry(frame_fields, textvariable=internship_ID_text)
internship_ID_entry.grid(row=0, column=1, sticky=W)
# Internship Name
internship_name_text = StringVar()
internship_name_label = Label(frame_fields, text='Job Title', font=('bold', 12))
internship_name_label.grid(row=0, column=2, sticky=E)
internship_name_entry = Entry(frame_fields, textvariable=internship_name_text)
internship_name_entry.grid(row=0, column=3, sticky=W)
# Company
company_text = StringVar()
company_label = Label(frame_fields, text='Company', font=('bold', 12))
company_label.grid(row=1, column=0, sticky=E)
company_entry = Entry(frame_fields, textvariable=company_text)
company_entry.grid(row=1, column=1, sticky=W)
# Salary
salary_text = StringVar()
salary_label = Label(frame_fields, text='Salary', font=('bold', 12), pady=20)
salary_label.grid(row=1, column=2, sticky=E)
salary_entry = Entry(frame_fields, textvariable=salary_text)
salary_entry.grid(row=1, column=3, sticky=W)


def populate_list(internship_name=''):
    for i in router_tree_view.get_children():
        router_tree_view.delete(i)
    for row in select.db.fetch(internship_name):
        router_tree_view.insert('', 'end', values=row)


def populate_list2(query='select * from INTERNSHIP'):
    for i in router_tree_view.get_children():
        router_tree_view.delete(i)
    for row in select.db.fetch2(query):
        router_tree_view.insert('', 'end', values=row)


def add_internship():
    if internship_name_text.get() == '' or internship_ID_text.get() == '' or company_text.get() == '' or salary_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    insert.db.insert(internship_ID_text.get(), internship_name_text.get(),
                     company_text.get(), salary_text.get())
    clear_text()
    populate_list()


def select_internship(event):
    try:
        global selected_item
        index = router_tree_view.selection()[0]
        selected_item = router_tree_view.item(index)['values']
        internship_ID_entry.delete(0, END)
        internship_ID_entry.insert(END, selected_item[1])
        internship_name_entry.delete(0, END)
        internship_name_entry.insert(END, selected_item[2])
        company_entry.delete(0, END)
        company_entry.insert(END, selected_item[3])
        salary_entry.delete(0, END)
        salary_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def remove_internship():
    delete.db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_internship():
    update.db.update(selected_item[0], internship_ID_text.get(), internship_name_text.get(),
                     company_text.get(), salary_text.get())
    populate_list()


def clear_text():
    internship_name_entry.delete(0, END)
    internship_ID_entry.delete(0, END)
    company_entry.delete(0, END)
    salary_entry.delete(0, END)


def search_internship():
    hostname = internship_search.get()
    populate_list(hostname)


def execute_query():
    query = query_search.get()
    populate_list2(query)


frame_btns = Frame(app)
frame_btns.grid(row=3, column=0)

add_btn = Button(frame_btns, text='Add Internship', width=12, command=add_internship)
add_btn.grid(row=0, column=0, pady=20)

remove_btn = Button(frame_btns, text='Remove internship',
                    width=12, command=remove_internship)
remove_btn.grid(row=0, column=1)

update_btn = Button(frame_btns, text='Update internship',
                    width=12, command=update_internship)
update_btn.grid(row=0, column=2)

clear_btn = Button(frame_btns, text='Clear Input',
                   width=12, command=clear_text)
clear_btn.grid(row=0, column=3)

search_btn = Button(frame_search, text='Search',
                    width=12, command=search_internship)
search_btn.grid(row=0, column=2)

search_query_btn = Button(frame_search, text='Search Query',
                          width=12, command=execute_query)
search_query_btn.grid(row=1, column=2)

app.title('Internship Search')
app.geometry('700x550')

# Start program
app.mainloop()
