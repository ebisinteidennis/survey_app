"""A customer preferences survey written in Python with Tkinter"""
"""The software is aimed at gathering information about shalom-tech innovation product and services
  Software is allowed to collect demographic information, personal information, etc"""

import tkinter as tk

from tkinter import ttk

# Create the root window
root = tk.Tk()

# set the title
root.title('Shalom-tech innovation survey')

# set the root window size
root.wm_iconbitmap ("icon.ico")
root.geometry('640x480+300+300')
root.resizable(False, False)



###########
# Widgets #
###########

# Use a Label to show the title
# 'font' lets us set a font
title = tk.Label(
  root,
  text='SHALOM-TECH INNOVATION SURVEY',
  font=('Arial 16 bold'),
  bg='brown',
  fg='#FF0'
)


# Use string vars for strings
name_var = tk.StringVar(root)
name_label = tk.Label(root, text='What is your name?')
name_inp = tk.Entry(root, textvariable=name_var)

# Use boolean var for True/False
user_var = tk.BooleanVar()
user_inp = tk.Checkbutton(
  root, variable=user_var, text='Check this box if you use shalom-tech innovation services/product'
)

# Use int var for whole numbers
# Value can set a default
num_var = tk.IntVar(value=2)
num_label = tk.Label(text='How many times do you use shalom-tech innovation service?')
# note that even with an intvar, the key is still 'textvariable'
num_inp = tk.Spinbox(
  root,
  textvariable=num_var,
  from_=1.0,
  to = 50.0,
  increment=+1,
)

# Listboxes don't work well with variables,
# However OptionMenu works great!
color_var = tk.StringVar(value='All of them')
color_label = tk.Label(root, text='What service or product have you being most satisfied with?')
color_choices = (
  'Any', 'Web development', 'Graphics Design', 'Video Editing', 'Photography', 'jamb', "DStv installation", "Computer Appreciation",
  "Computer Engineering","Musical Sound and Audio Production","Seminars and Workshop","Mobile App Development","Home Automation",
  "Jamb Registration", "NIMC Registration/National ID cards","Sales of ICT Equipment", "CCTV/intercom(PABX) installation","Typesetting/Photocopy",
  "Binding/Lamination", "Graphics Design/Banners/Printing", "PassPort/Photo printing/DI printing", "Research/Business Plan","Repair All types of computers"
  ,"Event planning/Photography","Video Coverage","NGO, company Business name Registration", "Uninterrupted Power Supply"
)
color_inp = tk.OptionMenu(
    root, color_var, *color_choices
)

recommend_label = tk.Label(root, text='Will you recommend shalom-tech innovation to people?')
# Use a Frame to keep widgets together
recommend_frame = tk.Frame(root)

# We can use any kind of var with Radiobuttons,
# as long as each button's 'value' property is the
# correct type
recommend_var = tk.BooleanVar()
# The radio buttons are connected by using the same variable
# The value of the var will be set to the button's 'value' property value
recommend_yes_inp = tk.Radiobutton(
    recommend_frame,
    text='Yes',
    value=True,
    variable=recommend_var
)
recommend_no_inp = tk.Radiobutton(
    recommend_frame,
    text='no!',
    value=False,
    variable=recommend_var
)

# The Text widget doesn't support variables, sadly
# There is no analogous widget that does
about_sti_label = tk.Label(root, text='Write a little about Shalom-tech innovation')
hint = tk.Label(root,text="HINT: Services, products and customer service")
about_sti_inp = tk.Text(root, height=3)

# Buttons are used to trigger actions

submit_btn = tk.Button(root, text='Submit Survey')

# Labels can use a StringVar for their contents
output_var = tk.StringVar(value='')
output_line = tk.Label(
  root,
  textvariable=output_var,
  anchor='w',
  justify='left'
)

#######################
# Geometry Management #
#######################
# Using Grid instead of pack
# Put our widgets on the root window
#title.grid()
# columnspan allows the widget to span multiple columns
title.grid(columnspan=2)

# add name label and input
# Column defaults to 0
name_label.grid(row=1, column=0)

# The grid automatically expands
# when we add a widget to the next row or column
name_inp.grid(row=1, column=1)

# 'sticky' attaches the widget to the named sides,
# so it will expand with the grid
user_inp.grid(row=2, columnspan=2, sticky='we')
# tk constants can be used instead of strings
num_label.grid(row=3, sticky=tk.W)
num_inp.grid(row=3, column=1, sticky=(tk.W + tk.E))

#padx and pady can still be used to add horizontal or vertical padding
color_label.grid(row=4, columnspan=2, sticky=tk.W, pady=10)
color_inp.grid(row=5, columnspan=2, sticky=tk.W + tk.E, padx=25)

# We can still use pack on the plantain frame.
# pack and grid can be mixed in a layout as long as we don't
# use them in the same frame
recommend_yes_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
recommend_no_inp.pack(side='left', fill='x', ipadx=10, ipady=5)
recommend_label.grid(row=6, columnspan=2, sticky=tk.W)
recommend_frame.grid(row=7, columnspan=2, stick=tk.W)

# Sticky on all sides will allow the widget to fill vertical and horizontal
about_sti_label.grid(row=8, sticky=tk.W)
hint.grid(row=9,sticky=tk.W)
about_sti_inp.grid(row=10, columnspan=2, sticky='NSEW')

# Add the button and output
submit_btn.grid(row=99)
output_line.grid(row=100, columnspan=2, sticky='NSEW')

# columnconfigure can be used to set options on the columns of the grid
# 'weight' means that column will be preferred for expansion
root.columnconfigure(1, weight=1)

# rowconfigure works for rows
root.rowconfigure(99, weight=2)
root.rowconfigure(100, weight=1)

#####################
# Add some behavior #
#####################

def on_submit():
  """To be run when the user submits the form"""
  # cars all use 'get()' to retreive their variables
  name = name_var.get()
  # Because we used an IntVar, .get() will try to convert
  # the contents of num_var to int.
  try:
    number = num_var.get()
  except tk.TclError:
    number = 10000

  # With the variable, OptionMenu makes things simple
  color = color_var.get()

  # Checkbutton and Radiobutton values are now simple
  Shalom_tech_user = user_var.get()
  Shalom_tech_user_all = recommend_var.get()

  # Text widgets require a range
  haiku = about_sti_inp.get('1.0', tk.END)

  # Update the text in our output
  message = f'Thanks for taking the survey, {name}.\n'

  if not Shalom_tech_user:
    message += "Sorry you didn't like shalom-tech innovation services and product!\n"

  else:
    message += f'Enjoy your {number} {color} day!\n'

  if Shalom_tech_user_all:
    message += 'Enjoy the service!'
  else:
    message += 'We will do better next time!'

  if haiku.strip():
    message += f'\n\nYour Feedback:\n{haiku}'

  # Set the value of a variable using .set()
  # DON'T DO THIS:  output_var = 'my string'
  output_var.set(message)


# configure the button to trigger submission
submit_btn.configure(command=on_submit)

###############
# Execute App #
###############

root.mainloop()
