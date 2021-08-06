from tkinter import *
from tkinter import ttk,messagebox
from datetime import datetime
import csv
from tkinter.font import Font

root=Tk()
root.title('Daily expense by Deceimo_ V.0.1')

w = 780
h = 550

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')
root.iconbitmap('main.ico')

#Build menu
menuBar=Menu(root)
root.config(menu=menuBar)

#Create menu item
fileMenu=Menu(menuBar,tearoff=False)
menuBar.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='Import CSV')
fileMenu.add_command(label='Exit',command=root.quit)

def usage():
	messagebox.showinfo('Usage','There are 2 tabs in this program')

helpMenu=Menu(menuBar,tearoff=False)
menuBar.add_cascade(label='Help',menu=helpMenu)
helpMenu.add_command(label='Usage',command=usage)


def credit():
	messagebox.showinfo('Credit','Editor: Nattapong Saengarunvong\nDonate me with this ID: 63070503415')

creditMenu=Menu(menuBar,tearoff=False)
menuBar.add_cascade(label='Credit',menu=creditMenu)
creditMenu.add_command(label='About editor',command=credit)





#Define variable
font1=(None,20)
v_menu=StringVar()
v_cost=StringVar()
v_amount=StringVar()
v_result=StringVar()
v_result.set('Result')
v_locate=IntVar()
v_locate.set(0)

month=  {'01':'มกราคม',
		'02':'กุมภาพันธ์',
		'03':'มีนาคม',
		'04':'เมษายน',
		'05':'พฤษภาคม',
		'06':'มิถุนายน',
		'07':'กรกฏาคม',
		'08':'สิงหาคม',
		'09':'กันยายน',
		'10':'ตุลาคม',
		'11':'พฤศจิกายน',
		'12':'ธันวาคม'}

day=   {'Mon':'วันจันทร์',
		'Tue':'วันอังคาร',
		'Wed':'วันพุธ',
		'Thu':'วันพฤหัสบดี',
		'Fri':'วันศุกร์',
		'Sat':'วันเสาร์',
		'Sun':'วันอาทิตย์'}

def save(event=None):
	#Get data
	menu=v_menu.get()
	cost=v_cost.get()
	amount=v_amount.get()

	if(len(menu) == 0):
		E1.focus()
		v_result.set('Please insert correct/all data')
		print('Please insert correct/all data')
		messagebox.showwarning('ERROR','Please insert correct/all data')
	else:
		try:
			cost=float(cost)
			amount=int(amount)
			total=cost*amount
			cost=f'{cost:,.2f}'
			amount=f'{amount:,}'
			total=f'{total:,.2f}'
			dDay=datetime.now().strftime('%a')
			dMonth=datetime.now().strftime('%m')
			dYear=int(datetime.now().strftime('%Y')) + 543
			time=datetime.now().strftime(f"{day[dDay]}/%d/{month[dMonth]}/{dYear}, %H:%M:%S")

			transaction_id=datetime.now().strftime('%Y%m%d%H%M%f')

			#Clear data in entry space
			v_menu.set('')
			v_cost.set('')
			v_amount.set('')

			print(f'At:           {time}')        
			print(f'Menu:         {menu}')
			print(f'Cost:         {cost}')
			print(f'Amount:       {amount}')
			print(f'Total cost:   {total}')

			#Write data in excel
			f=open('expense.csv','a',encoding='utf-8',newline='')
			writer=csv.writer(f)
			writer.writerow([transaction_id,time,menu,cost,amount,total])
			f.close()

			#Update data in tree view
			update_table()

			E1.focus()
			v_locate.set(0)
			text=f'At time {time}\n{"Menu:":<15}{menu:>20}\n{"Cost:":<15}{cost:>20}\n{"Amount:":<15}{amount:>20}\n{"Total cost:":<15}{total:>20}'
			v_result.set(text)
		except:
			v_result.set('Please insert correct/all data')
			print('Please insert correct/all data')
			messagebox.showwarning('ERROR','Please insert correct/all data')
			E1.focus()


def up(event=None):
	locate=v_locate.get()-1
	v_locate.set(locate)

	if((locate<0) or (locate>2)):
		v_locate.set(2)
		E3.focus()
	else:
		if(locate==0):
			E1.focus()
		elif(locate==1):
			E2.focus()
		else:
			E3.focus()

def down(event=None):
	locate=v_locate.get()+1
	v_locate.set(locate)

	if((locate<0) or (locate>2)):
		v_locate.set(0)
		E1.focus()
	else:
		if(locate==0):
			E1.focus()
		elif(locate==1):
			E2.focus()
		else:
			E3.focus()


#Making tab
tab=ttk.Notebook(root)

T1=Frame(tab)
T2=Frame(tab)

tab.pack(fill=BOTH,expand=1)

icon1=PhotoImage(file='plus.png').subsample(20)
icon2=PhotoImage(file='list.png').subsample(20)

tab.add(T1,text='Add expense',image=icon1,compound='top')
tab.add(T2,text='Expense list',image=icon2,compound='top')


##########################################################################

#Tab1
#Making UI for inserting menu
F1=Frame(T1)
F1.pack()

P1=PhotoImage(file='cart.png').subsample(8)
pic1=ttk.Label(F1,image=P1)
pic1.pack()

L1=ttk.Label(F1,text='Menu',font=font1)
L1.pack()
E1=ttk.Entry(F1,textvariable=v_menu,font=font1)
E1.pack()

L2=ttk.Label(F1,text='Cost(Baht)',font=font1)
L2.pack()
E2=ttk.Entry(F1,textvariable=v_cost,font=font1)
E2.pack()

L3=ttk.Label(F1,text='Amount',font=font1)
L3.pack()
E3=ttk.Entry(F1,textvariable=v_amount,font=font1)
E3.pack()

icon3=PhotoImage(file='save.png').subsample(18)
B1=ttk.Button(F1,text='Save',image=icon3,compound='top',command=save)
B1.pack(ipadx=10,ipady=5,padx=10,pady=12)

L4=ttk.Label(F1,textvariable=v_result,font=(None,10),foreground='green')
L4.pack()

E1.focus()

root.bind('<Return>',save)
root.bind('<Up>',up)
root.bind('<Down>',down)

########################################################################



#Tab2
#Making tree view
header = ['Transaction ID','Date','Menu','Cost','Amount','Total']
width = [140,210,150,90,80,90]
tree = ttk.Treeview(T2,columns=header,show='headings',height=15)
tree.pack(pady=10)

style = ttk.Style()
style.configure("Treeview.Heading", font=(None,15))

for h,w in zip(header,width):
	tree.column(h,width=w)

for i in header:
	tree.heading(i,text=i)


#Deleting item in treeview
def delete(event=None):
	try:
		dummy = tree.selection()[0]
		check = messagebox.askyesno('Confirm','Do you want to delete data?')
		if(check==True):
			#Get ID of that one
			select = tree.selection()[0]
			data = tree.item(select)
			data=data['values']
			data=data[0]
			ID=str(data)
			
			#Delete from treeeview
			tree.delete(select)

			f=open('expense.csv','r',encoding='utf-8',newline='')
			reader=csv.reader(f)
			reader=list(reader)

			#Find the list that will be deleted, and delete it
			for read in reader:
				if (ID in read[0]):
					reader.remove(read)
					break
			f.close()

			#Then write new list that do not have the deleted one in csv file
			f=open('expense.csv','w',encoding='utf-8',newline='')
			writer=csv.writer(f)
			for read in reader:
				writer.writerow(read)
			f.close()
	except:
		print('You must select item')


tree.bind('<BackSpace>',delete)



B2 = ttk.Button(T2,text='Delete',command=delete)
B2.pack(ipadx=1,ipady=5,pady=15)



#Showing the old menu in the csv file
def update_table():
	try:
		data=tree.get_children()
		for d in data:
			tree.delete(d)

		f=open('expense.csv','r',encoding='utf-8',newline='')
		reader=csv.reader(f)
		for row in reader:
			tree.insert(parent='',index='end',value=(row))
		f.close()
	except:
		print('There is no any data')

update_table()


v_menu_popup=StringVar()
v_cost_popup=StringVar()
v_amount_popup=StringVar()

def save_edit(event=None):
	#Get data
	menu=v_menu_popup.get()
	cost=v_cost_popup.get()
	amount=v_amount_popup.get()

	if(len(menu) == 0):
		E1_popup.focus()
		print('Please insert correct/all data')
		messagebox.showwarning('ERROR','Please insert correct/all data')
	else:
		try:
			cost=float(cost)
			amount=int(amount)
			total=cost*amount
			cost=f'{cost:,.2f}'
			amount=f'{amount:,}'
			total=f'{total:,.2f}'

			select = tree.selection()[0]
			data = tree.item(select)
			data=data['values']
			data=data[0]
			ID=str(data)

			#Read all item in csv for modifying
			f=open('expense.csv','r',encoding='utf-8',newline='')
			reader=csv.reader(f)
			reader=list(reader)

			#Find the list that will be modified, and modify it
			for read in reader:
				if (ID in read[0]):
					read[2]=menu
					read[3]=cost
					read[4]=amount
					read[5]=total
					break
			f.close()

			#Update in csv
			f=open('expense.csv','w',encoding='utf-8',newline='')
			writer=csv.writer(f)
			for read in reader:
				writer.writerow(read)
			f.close()

			#Update in treeview
			update_table()

			#Close pop up
			popup.destroy()
		except:
			print('Please insert correct/all data')
			messagebox.showwarning('ERROR','Please insert correct/all data')
			E1_popup.focus()



#Editing item in treeview
def edit(event=None):
	try:
		a=350
		b=300
		da = x-(a/2)
		db = y
		dummy = tree.selection()[0]
		global popup
		popup = Toplevel()
		popup.geometry(f'{a}x{b}+{da:.0f}+{db:.0f}')
		popup.title('Edit record')

		L1_popup=ttk.Label(popup,text='Menu',font=font1)
		L1_popup.pack()
		global E1_popup
		E1_popup=ttk.Entry(popup,textvariable=v_menu_popup,font=font1)
		E1_popup.pack()

		L2_popup=ttk.Label(popup,text='Cost(Baht)',font=font1)
		L2_popup.pack()
		global E2_popup
		E2_popup=ttk.Entry(popup,textvariable=v_cost_popup,font=font1)
		E2_popup.pack()

		L3_popup=ttk.Label(popup,text='Amount',font=font1)
		L3_popup.pack()
		global E3_popup
		E3_popup=ttk.Entry(popup,textvariable=v_amount_popup,font=font1)
		E3_popup.pack()

		B1_popup=ttk.Button(popup,text='Save',command=save_edit)
		B1_popup.pack(ipadx=10,ipady=5,padx=10,pady=12)

		select = tree.selection()[0]
		data = tree.item(select)
		data=data['values']

		v_menu_popup.set(data[2])
		v_cost_popup.set(data[3])
		v_amount_popup.set(data[4])

		popup.bind('<Return>',save_edit)
		E1_popup.focus()

		popup.mainloop()
	except:
		print('You must select item')


B3 = ttk.Button(T2,text='Edit',command=edit)
B3.pack(ipadx=1,ipady=5,pady=10)

############################################################
#Right click menu in treeview
right_click = Menu(root,tearoff=False)
right_click.add_command(label='Delete',command=delete)
right_click.add_command(label='Edit',command=edit)


def menu_popup(event):
	try:
		dummy = tree.selection()[0]
		right_click.post(event.x_root,event.y_root)
	except:
		print('You must select item')

def detach(event=None):
	print('left click')
	tree.selection_remove(tree.focus())

tree.bind('<Button-3>',menu_popup)
T2.bind('<Button-1>',detach)



root.mainloop()