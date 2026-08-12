import os
from tkinter import *
from Planets import planets
from Query import QueryInfo as query

root = Tk()
root.title("The Solar System")
root.state("zoomed")  # maximize window so background image fills the screen

first_page_list = []
name_of_planet_list = []
mass_of_planet_list = []
distance_of_planet_list = []
moons_of_planet_list = []

script_dir = os.path.dirname(os.path.abspath(__file__))





try:#https://www.geeksforgeeks.org/python/how-to-use-images-as-backgrounds-in-tkinter/
    image_path = os.path.join(script_dir, "SolarSystem.png")
    background_image = PhotoImage(file=image_path)
    image_label = Label(root, image = background_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)  # fill whole window
except:
    print("No bg image at planned path")


label = Label(root, text="Background Image Credit: NASA/JPL!", bg="black", fg="white")
label.place(relx=0.5, rely=0.05, anchor="n")  # sits on top, near the top


#https://www.geeksforgeeks.org/python/python-creating-a-button-in-tkinter/

#https://www.geeksforgeeks.org/python/how-to-place-a-button-at-any-position-in-tkinter/
def create_menu_buttons():
    name_of_planet_button = Button(root, text="Name of Planets.", font=("Arial", 12), relief="solid", borderwidth=1, command = click_name_of_planet_button)
    name_of_planet_button.place(relx=0.089, rely=0.098, relwidth=0.825, relheight=0.103)
    first_page_list.append(name_of_planet_button)

    button2 = Button(root, text="Mass of Planets.", font=("Arial", 12), relief="solid", borderwidth=1, command = click_mass_of_planet_button)
    button2.place(relx=0.089, rely=0.251, relwidth=0.825, relheight=0.103)
    first_page_list.append(button2)

    button3 = Button(root, text="Distance from the Sun.", font=("Arial", 12), relief="solid", borderwidth=1, command = click_distance_of_planet_button)
    button3.place(relx=0.089, rely=0.404, relwidth=0.825, relheight=0.103)
    first_page_list.append(button3)

    button4 = Button(root, text=" A list of the planet's moons.", font=("Arial", 12), relief="solid", borderwidth=1, command = click_moons_of_planet_button)
    button4.place(relx=0.089, rely=0.557, relwidth=0.825, relheight=0.103)
    first_page_list.append(button4)

def create_planet_name_menu_buttons():

    for i in range(len(planets)):
        planet = planets[i]
        label = Label(root, text=f"{planet.name}", font=("Arial", 12), relief="solid", borderwidth=1)
        label.place(relx=0.089, rely=0.098 + (i*0.075), relwidth=0.825, relheight=0.06)
        name_of_planet_list.append(label)

    back_button = Button(root, text="<-", font=("Arial", 12), relief="solid", borderwidth=1, command = click_back_in_NOP)
    back_button.place(relx=0.01, rely=0.01, relwidth=0.05, relheight=0.06)
    name_of_planet_list.append(back_button)


def create_planet_mass_menu_buttons():
    for i in range(len(planets)):
        planet = planets[i]
        label = Label(root, text=f"{planet.name}'s Mass is {planet.mass}kg", font=("Arial", 12), relief="solid", borderwidth=1)
        label.place(relx=0.089, rely=0.098 + (i*0.075), relwidth=0.825, relheight=0.06)
        mass_of_planet_list.append(label)
   
    back_button = Button(root, text="<-", font=("Arial", 12), relief="solid", borderwidth=1, command = click_back_in_MOP)
    back_button.place(relx=0.01, rely=0.01, relwidth=0.05, relheight=0.06)
    mass_of_planet_list.append(back_button)

def create_planet_distance_menu_buttons():

    for i in range(len(planets)):
        planet = planets[i]
        label = Label(root, text=f"The distance of {planet.name} to the Sun is {planet.distance}", font=("Arial", 12), relief="solid", borderwidth=1)
        label.place(relx=0.089, rely=0.098 + (i*0.075), relwidth=0.825, relheight=0.06)
        distance_of_planet_list.append(label)

    back_button = Button(root, text="<-", font=("Arial", 12), relief="solid", borderwidth=1, command = click_back_in_DOP)
    back_button.place(relx=0.01, rely=0.01, relwidth=0.05, relheight=0.06)
    distance_of_planet_list.append(back_button)

def create_planet_moons_menu_buttons():
    label1 = Label(root, text="Mercury has 0 moons", font=("Arial", 12), relief="solid", borderwidth=1)
    label1.place(relx=0.089, rely=0.098, relwidth=0.825, relheight=0.06)
    moons_of_planet_list.append(label1)

    label2 = Label(root, text="Venus has 0 moons", font=("Arial", 12), relief="solid", borderwidth=1)
    label2.place(relx=0.089, rely=0.173, relwidth=0.825, relheight=0.06)
    moons_of_planet_list.append(label2)

    for i in range(2, len(planets)):
        planet = planets[i]
        label = Label(root, text=f"The Moons of {planet.name} is/are " + " , ".join(planet.moons), font=("Arial", 12), relief="solid", borderwidth=1)
        label.place(relx=0.089, rely=0.098 + (i*0.075), relwidth=0.825, relheight=0.06)
        moons_of_planet_list.append(label)

    back_button = Button(root, text="<-", font=("Arial", 12), relief="solid", borderwidth=1, command = click_back_in_MOONS)
    back_button.place(relx=0.01, rely=0.01, relwidth=0.05, relheight=0.06)
    moons_of_planet_list.append(back_button)

def destroy_name_of_planet():
    for widget in name_of_planet_list:
        widget.destroy()
    name_of_planet_list.clear()

def destroy_first_page():
    for widget in first_page_list:
        widget.destroy()
    first_page_list.clear()

def destroy_mass_of_planet():
    for widget in mass_of_planet_list:
        widget.destroy()
    mass_of_planet_list.clear()

def destroy_distance_of_planet():
    for widget in distance_of_planet_list:
        widget.destroy()
    distance_of_planet_list.clear()

def destroy_moons_of_planet():
    for widget in moons_of_planet_list:
        widget.destroy()
    moons_of_planet_list.clear()


def click_name_of_planet_button():
    create_planet_name_menu_buttons()
    destroy_first_page()

def click_back_in_NOP():
    destroy_name_of_planet()
    create_menu_buttons()

def click_mass_of_planet_button():
    create_planet_mass_menu_buttons()
    destroy_first_page()

def click_back_in_MOP():
    destroy_mass_of_planet()
    create_menu_buttons()

def click_distance_of_planet_button():
    create_planet_distance_menu_buttons()
    destroy_first_page()

def click_back_in_DOP():
    destroy_distance_of_planet()
    create_menu_buttons()

def click_moons_of_planet_button():
    create_planet_moons_menu_buttons()
    destroy_first_page()

def click_back_in_MOONS():
    destroy_moons_of_planet()
    create_menu_buttons()

def click_enter():
    question = entry_field.get()
    entry_field.delete(0, END)
    answer = query(question).get_answer()
    output_label.config(text=answer)


#START
create_menu_buttons()


input_label = Label(root, text="Query information about the Solar System Here", font=("Arial", 12))
input_label.place(relx=0.089, rely=0.70, relwidth=0.647, relheight=0.05) 
# input field
entry_field = Entry(root, font=("Arial", 12))
entry_field.place(relx=0.089, rely=0.765, relwidth=0.647, relheight=0.073)

# enter button, beside the input field
enter_button = Button(root, text="enter", font=("Arial", 12), relief="solid", borderwidth=1, command=click_enter)
enter_button.place(relx=0.796, rely=0.765, relwidth=0.1175, relheight=0.073)

# output label, spans full width below input/enter
output_label = Label(root, text="", font=("Arial", 12), bg="white", fg="black", relief="solid", borderwidth=1)
output_label.place(relx=0.089, rely=0.876, relwidth=0.825, relheight=0.074)


root.mainloop()