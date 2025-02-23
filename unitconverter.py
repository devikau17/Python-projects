# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 13:26:37 2024

@author: DEVIKA
"""


import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk



# Fun for closing window frame button
def close_window():
    root.destroy()


# Fun for minimize and maximize window button
def maximize_window():
    if root.state() == "normal":
        root.state("zoomed")  # Maximize the window
        maximize_button.config(text="🗗")  # Change icon to "Restore Down"
    else:
        root.state("normal")  # Restore the window
        maximize_button.config(text="🗖")  # Change icon to "Maximize"


# Main window
root = tk.Tk()
root.geometry('990x450')
root.title("UNIT CONVERTER")
root.configure(bg='lightgreen')




# Hide the default title bar
root.overrideredirect(True)


# Create a custom title bar
title_bar = tk.Frame(root, bg="springgreen4", relief="raised", bd=2)
title_bar.pack(side="top", fill="x")

# Add a label for the title
title_label = tk.Label(
    title_bar,
    text="Unit Converters.Net",
    font=("Arial", 15, "bold"),
    bg="springgreen4",
    fg="white"
)
title_label.pack(side="left", padx=5, pady=5)

# Add a close button
close_button = tk.Button(
    title_bar,
    text="X",
    command=close_window,
    font=("Arial", 10, "bold"),
    bg="red",
    fg="white",
    relief="flat"
)
close_button.pack(side="right", padx=10, pady=5)

# Add a maximize button
maximize_button = tk.Button(
    title_bar,
    text="🗖",  # Unicode character for "Maximize"
    command=maximize_window,
    font=("Arial", 18, "bold"),
    bg="springgreen4",
    fg="white",
    relief="flat"
)
maximize_button.pack(side="right", padx=5, pady=5)

# Tab control color frame
tabcontrol = ttk.Notebook(root)
tab1 = tk.Frame(tabcontrol, bg="floralwhite")
tab2 = tk.Frame(tabcontrol, bg="floralwhite")
tab3 = tk.Frame(tabcontrol, bg="floralwhite")
tab4 = tk.Frame(tabcontrol, bg="floralwhite")
tab5 = tk.Frame(tabcontrol, bg="floralwhite")
tab6 = tk.Frame(tabcontrol, bg="floralwhite")

tabcontrol.pack(expand=1, fill="both")


# Assign to tab names
tabcontrol.add(tab1, text='Length')
tabcontrol.add(tab2, text='Mass')
tabcontrol.add(tab3, text="Temperature")
tabcontrol.add(tab4, text='Area')
tabcontrol.add(tab5, text='Volume')
tabcontrol.add(tab6, text='Time')
tabcontrol.pack(expand=1, fill="both")

# Create a style object for the tabs on the top of window (colour,style,background)

# Bring the other widgets to the front
title_bar.lift()        # Ensure the custom title bar is on top
tabcontrol.lift()       # Ensure the tab control is on top of the background
for tab in [tab1, tab2, tab3, tab4, tab5, tab6]:
    tab.lift()          # Ensure the tabs' content is visible

# Adjust tab1 content layout for centering
tab1.grid_rowconfigure(0, weight=1)  # Add padding at the top
tab1.grid_rowconfigure(30, weight=1)  # Add padding at the bottom
tab1.grid_columnconfigure(0, weight=1)  # Add padding to the left
tab1.grid_columnconfigure(20, weight=1)  # Add padding to the right

# Place the Convert button in the center of the last row

# Adjust tab2 content layout for centering
tab2.grid_rowconfigure(0, weight=1)  # Add padding at the top
tab2.grid_rowconfigure(30, weight=1)  # Add padding at the bottom
tab2.grid_columnconfigure(0, weight=1)  # Add padding to the left
tab2.grid_columnconfigure(20, weight=1)  # Add padding to the right



# Adjust tab3 content layout for centering
tab3.grid_rowconfigure(0, weight=1)  # Add padding at the top
tab3.grid_rowconfigure(30, weight=1)  # Add padding at the bottom
tab3.grid_columnconfigure(0, weight=1)  # Add padding to the left
tab3.grid_columnconfigure(20, weight=1)  # Add padding to the right

# Adjust tab4 content layout for centering
tab4.grid_rowconfigure(0, weight=1)  # Add padding at the top
tab4.grid_rowconfigure(30, weight=1)  # Add padding at the bottom
tab4.grid_columnconfigure(0, weight=1)  # Add padding to the left
tab4.grid_columnconfigure(20, weight=1)  # Add padding to the right

# Adjust tab5 content layout for centering
tab5.grid_rowconfigure(0, weight=1)  # Add padding at the top
tab5.grid_rowconfigure(30, weight=1)  # Add padding at the bottom
tab5.grid_columnconfigure(0, weight=1)  # Add padding to the left
tab5.grid_columnconfigure(20, weight=1)  # Add padding to the right

# Adjust tab6 content layout for centering
tab6.grid_rowconfigure(0, weight=1)  # Add padding at the top
tab6.grid_rowconfigure(30, weight=1)  # Add padding at the bottom
tab6.grid_columnconfigure(0, weight=1)  # Add padding to the left
tab6.grid_columnconfigure(20, weight=1)  # Add padding to the right


#style the dropdown box

root.title("Styled Combobox Example")

# Define a style object
style = ttk.Style()
style.theme_use('vista')  # Change theme to 'clam' for better customization options




# Customizing the Combobox Style
'''style.configure(
    "Custom.TCombobox",
    foreground="white",               # Text color
    background="blue",            # Dropdown button background color
    fieldbackground="lightblue",      # Input field background color
    bordercolor="blue",               # Border color
    arrowcolor="yellow",              # Dropdown arrow color
    padding=5,                        # Inner padding
    font=('Helvetica', 18)            # Font style
)'''

'''# Apply dropdown customization using `style.map()`
style.map("Custom.TCombobox",
          fieldbackground=[("readonly", "lightblue")],  # When readonly, change background color
          arrowcolor=[("readonly", "yellow")])  # Change arrow color for readonly'''


# Customize the Notebook and its Tabs
style.theme_create("CustomTabTheme", parent="alt", settings={
    "TNotebook": {
        "configure": {
            "tabmargins": [2, 5, 2, 0],  # Margins around tabs
            "background": "floralwhite"    # Background color for the entire tab control
        }
    },
    "TNotebook.Tab": {
        "configure": {
            "padding": [15, 10],         # Padding inside the tab
            "background": "springgreen4",  # Default tab background color (inactive tab)
            "foreground": "white",      # Default text color
            "font": ('Arial', 12, 'bold'),  # Font for tab text
            "relief": "solid",           # Border style for the tab
        },
        "map": {
            "background": [("selected", "floralwhite"),  # Background color when tab is selected
                           ("active", "seagreen4")],  # Background color on hover
            "foreground": [("selected", "green"),       # Text color when selected
                           ("active", "white")],       # Text color on hover
        }
    }
})

# Apply the custom theme
style.theme_use("CustomTabTheme")


# Create the functions
#lenght

def convert_length():
    """
    Convert a length measurement from one unit to another and display the result.
    Supported units: Inches, Centimeters, Meters, Feet, Kilometers, Millimeters
    """
    try:
        # Get the input value and units
        value = float(length_input_value.get())  # Convert input to float
        from_unit = length_input_unit.get()  # Source unit
        to_unit = length_output_unit.get()  # Target unit

        # Define conversion factors as a dictionary of tuples
        conversion_factors = {
            # Base conversions involving Inches
            ("Inches", "Centimeters"): 2.54,
            ("Centimeters", "Inches"): 1 / 2.54,
            ("Meters", "Inches"): 39.3701,
            ("Inches", "Meters"): 1 / 39.3701,
            ("Feet", "Inches"): 12,
            ("Inches", "Feet"): 1 / 12,
            ("Kilometers", "Inches"): 39370.1,
            ("Inches", "Kilometers"): 1 / 39370.1,
            ("Millimeters", "Inches"): 1 / 25.4,
            ("Inches", "Millimeters"): 25.4,

            # Base conversions involving Centimeters
            ("Centimeters", "Meters"): 1 / 100,
            ("Meters", "Centimeters"): 100,
            ("Centimeters", "Feet"): 1 / 30.48,
            ("Feet", "Centimeters"): 30.48,
            ("Kilometers", "Centimeters"): 100000,
            ("Centimeters", "Kilometers"): 1 / 100000,
            ("Millimeters", "Centimeters"): 1 / 10,
            ("Centimeters", "Millimeters"): 10,

            # Base conversions involving Meters
            ("Meters", "Feet"): 1 / 0.3048,
            ("Feet", "Meters"): 0.3048,
            ("Kilometers", "Meters"): 1000,
            ("Meters", "Kilometers"): 1 / 1000,
            ("Millimeters", "Meters"): 1 / 1000,
            ("Meters", "Millimeters"): 1000,

            # Base conversions involving Kilometers
            ("Kilometers", "Feet"): 3280.84,
            ("Feet", "Kilometers"): 1 / 3280.84,
            ("Kilometers", "Millimeters"): 1e6,
            ("Millimeters", "Kilometers"): 1 / 1e6,

            # Base conversions involving Millimeters
            ("Millimeters", "Feet"): 1 / 304.8,
            ("Feet", "Millimeters"): 304.8,
        }

        # Perform the conversion
        if from_unit == to_unit:
            result = value  # No conversion needed for identical units
        else:
            # Get the conversion factor for the specified units
            factor = conversion_factors.get((from_unit, to_unit))
            if factor:
                result = value * factor
            else:
                # Raise an error for unsupported conversions
                raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")

        # Display the result in the output field
        length_output_value.config(state='normal')
        length_output_value.delete(0, tk.END)
        length_output_value.insert(0, f"{result:.2f}")
        length_output_value.config(state='readonly')

    except ValueError as ve:
        # Handle invalid numeric input or unsupported unit conversions
        length_output_value.config(state='normal')
        length_output_value.delete(0, tk.END)
        length_output_value.insert(0, str(ve))
        length_output_value.config(state='readonly')

    except Exception as ex:
        # Catch any unexpected errors
        length_output_value.config(state='normal')
        length_output_value.delete(0, tk.END)
        length_output_value.insert(0, "An unexpected error occurred.")
        length_output_value.config(state='readonly')



# Length tab: Creating Dropdown and Convert Button and lab

length_units= ["Inches", "Centimeters", "Meters", "Feet", "Kilometers", "Millimeters"]

length_input_label = tk.Label(tab1, text="Select input unit:", font=('Arial', 16, 'bold'), bg="floralwhite", relief='flat')
length_input_label.grid(row=6, column=2, pady=7, padx=40,sticky="e")

length_input_unit = ttk.Combobox(tab1, values=length_units, state="readonly", font=('Arial', 14), style="Custom.TCombobox")
length_input_unit.grid(row=7, column=2, padx=0)

length_input_value_label = tk.Label(tab1, text="Enter Value:", font=('Arial', 16, 'bold'), bg="floralwhite")
length_input_value_label.grid(row=11, column=2, pady=10,padx=0)

length_input_value = tk.Entry(tab1, font=('Arial', 16), background="white", relief="groove", width=16)
length_input_value.grid(row=12, column=2, padx=30,sticky="e")

length_output_label = tk.Label(tab1, text="Select output Unit:", font=('Arial', 16, 'bold'), bg="floralwhite")
length_output_label.grid(row=6, column=4, pady=5, padx=40)

length_output_unit = ttk.Combobox(tab1, values=length_units, state="readonly", font=('Arial', 14), style="Custom.TCombobox")
length_output_unit.grid(row=7, column=4, padx=20,sticky="w")

length_output_value_label = tk.Label(tab1, text="Converted Value:", font=('Arial', 16, 'bold'), bg="floralwhite")
length_output_value_label.grid(row=11, column=4, pady=7)

length_output_value = tk.Entry(tab1, font=('Arial', 16), background="white", relief="groove", width=16)
length_output_value.grid(row=12, column=4, padx=30)

length_convert_button = tk.Button(tab1, text="Convert", command=convert_length, fg="black", font=('Arial', 16, 'bold'), bg="springgreen4", relief="groove", width=8, height=1)
length_convert_button.grid(row=23, column=3,padx=0, pady=20,sticky="n")

# Center the Convert button in the last row
length_convert_button.grid(row=24, column=3, pady=20, sticky="n")


#image lenght
image = Image.open("E:/PYTHON/PycharmProjects/pythonProject1/scale (5).png")
image = image.resize((155,150))
photo_image = ImageTk.PhotoImage(image)
image_label = tk.Label(tab1, image=photo_image,relief='flat',bg='floralwhite')
image_label.place(x=1500,y=200)

# Place the image on the right side of the existing content in tab1
image_label.grid(row=6, column=5, rowspan=10, padx=100, pady=10, sticky="e")



# Mass function
def convert_kg():
    """
    Convert a weight measurement from one unit to another and display the result.
    Supported units: Kilograms, Pounds, Grams, Milligrams, Tons, Ounces
    """
    try:
        # Get the input value and units
        value = float(kg_input_value.get())  # Convert input to float
        from_unit = kg_input_unit.get()     # Source unit
        to_unit = kg_output_unit.get()      # Target unit

        # Define conversion factors
        conversion_factors = {
            # Base conversions involving Kilograms
            ("Pounds", "Kilograms"): 0.453592,
            ("Kilograms", "Pounds"): 2.20462,
            ("Grams", "Kilograms"): 1 / 1000,
            ("Kilograms", "Grams"): 1000,
            ("Milligrams", "Kilograms"): 1 / 1e6,
            ("Kilograms", "Milligrams"): 1e6,
            ("Tons", "Kilograms"): 1000,
            ("Kilograms", "Tons"): 1 / 1000,
            ("Ounces", "Kilograms"): 0.0283495,
            ("Kilograms", "Ounces"): 1 / 0.0283495,

            # Base conversions involving Pounds
            ("Milligrams", "Pounds"): 1 / 453592.37,
            ("Pounds", "Milligrams"): 453592.37,
            ("Grams", "Pounds"): 1 / 453.592,
            ("Pounds", "Grams"): 453.592,
            ("Ounces", "Pounds"): 1 / 16,
            ("Pounds", "Ounces"): 16,
            ("Tons", "Pounds"): 2000,
            ("Pounds", "Tons"): 1 / 2000,

            # Base conversions involving Grams
            ("Milligrams", "Grams"): 1 / 1000,
            ("Grams", "Milligrams"): 1000,
            ("Grams", "Ounces"): 1 / 28.3495,
            ("Ounces", "Grams"): 28.3495,
            ("Tons", "Grams"): 1e6,
            ("Grams", "Tons"): 1 / 1e6,

            # Base conversions involving Tons
            ("Milligrams", "Tons"): 1 / 1e9,
            ("Tons", "Milligrams"): 1e9,
            ("Ounces", "Tons"): 1 / 32000,
            ("Tons", "Ounces"): 32000,

            # Base conversions involving Ounces
            ("Milligrams", "Ounces"): 1 / 28349.5,
            ("Ounces", "Milligrams"): 28349.5,
        }

        # Perform the conversion
        if from_unit == to_unit:
            result = value  # No conversion needed for identical units
        else:
            # Get the conversion factor for the specified units
            factor = conversion_factors.get((from_unit, to_unit))
            if factor:
                result = value * factor
            else:
                # Raise an error for unsupported conversions
                raise ValueError(f" not supported.")

        # Display the result in the output field
        kg_output_value.config(state='normal')
        kg_output_value.delete(0, tk.END)
        kg_output_value.insert(0, f"{result:.2f}")
        kg_output_value.config(state='readonly')

    except ValueError as ve:
        # Handle invalid numeric input or unsupported unit conversions
        kg_output_value.config(state='normal')
        kg_output_value.delete(0, tk.END)
        kg_output_value.insert(0, str(ve))
        kg_output_value.config(state='readonly')

    except Exception as ex:
        # Catch any unexpected errors
        kg_output_value.config(state='normal')
        kg_output_value.delete(0, tk.END)
        kg_output_value.insert(0, "An unexpected error occurred.")
        kg_output_value.config(state='readonly')



# Mass tab: Creating Dropdown and Convert Button and labels

mass_units = ["Kilograms", "Pounds", "Grams", "Milligrams", "Tons", "Ounces"]

kg_input_label = tk.Label(tab2, text="Select input Unit:", font=('Arial', 16, 'bold'), bg="floralwhite", relief='flat')
kg_input_label.grid(row=6, column=2, pady=7, padx=40,sticky="e")

kg_input_unit = ttk.Combobox(tab2, values=mass_units, state="readonly", font=('Arial', 14), style="Custom.TCombobox")
kg_input_unit.grid(row=7, column=2, padx=0)

kg_input_value_label = tk.Label(tab2, text="Enter Value:", font=('Arial', 16, 'bold'), bg="floralwhite")
kg_input_value_label.grid(row=11, column=2, pady=10,padx=0)

kg_input_value = tk.Entry(tab2, font=('Arial', 16), background="white", relief="groove", width=16)
kg_input_value.grid(row=12, column=2, padx=30,sticky="e")

kg_output_label = tk.Label(tab2, text="Select output Unit:", font=('Arial', 16, 'bold'), bg="floralwhite")
kg_output_label.grid(row=6, column=4, pady=5, padx=40)

kg_output_unit = ttk.Combobox(tab2, values=mass_units, state="readonly", font=('Arial', 14), style="Custom.TCombobox")
kg_output_unit.grid(row=7, column=4, padx=20,sticky="w")

kg_output_value_label = tk.Label(tab2, text="Converted Value:", font=('Arial', 16, 'bold'), bg="floralwhite")
kg_output_value_label.grid(row=11, column=4, pady=7)

kg_output_value = tk.Entry(tab2, font=('Arial', 16), background="white", relief="groove", width=16)
kg_output_value.grid(row=12, column=4, padx=30)

kg_convert_button = tk.Button(tab2, text="Convert", command=convert_kg, fg="black", font=('Arial', 16, 'bold'), bg="springgreen4", relief="groove", width=8, height=1)
kg_convert_button.grid(row=23, column=3,padx=0, pady=20,sticky="n")

# Center the Convert button in the last row
length_convert_button.grid(row=24, column=3, pady=20, sticky="n")

#image mass
image2 = Image.open("E:/PYTHON/PycharmProjects/pythonProject1/law.png")
image2 = image2.resize((130,130))
photo_image2 = ImageTk.PhotoImage(image2)
image_label2 = tk.Label(tab2, image=photo_image2,relief='flat',bg='floralwhite')
image_label2.place(x=1500,y=230)

# Place the image on the right side of the existing content in tab1
image_label2.grid(row=5, column=15, rowspan=10, padx=100, pady=10, sticky="e")


# Temperature Function
def convert_temperature():

    try:
        # Get the input value and units
        value = float(temp_input_value.get())  # Convert input to float
        from_unit = temp_input_unit.get()     # Source unit
        to_unit = temp_output_unit.get()      # Target unit

        # Perform the conversion based on units
        if from_unit == to_unit:
            result = value  # No conversion needed for identical units
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5 / 9
        elif from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9 / 5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (value - 32) * 5 / 9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (value - 273.15) * 9 / 5 + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = value - 273.15
        else:
            # Raise an error for unsupported conversions
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")

        # Display the result in the output field
        temp_output_value.config(state='normal')
        temp_output_value.delete(0, tk.END)
        temp_output_value.insert(0, f"{result:.2f}")
        temp_output_value.config(state='readonly')

    except ValueError as ve:
        # Handle invalid numeric input or unsupported unit conversions
        temp_output_value.config(state='normal')
        temp_output_value.delete(0, tk.END)
        temp_output_value.insert(0, str(ve))
        temp_output_value.config(state='readonly')

    except Exception as ex:
        # Catch any unexpected errors
        temp_output_value.config(state='normal')
        temp_output_value.delete(0, tk.END)
        temp_output_value.insert(0, "An unexpected error occurred.")
        temp_output_value.config(state='readonly')

# Temperature Tab: Widgets

temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]

temp_input_label = tk.Label(tab3, text="Select input Unit:", font=('Arial', 16, 'bold'), bg="floralwhite", relief='flat')
temp_input_label.grid(row=6, column=4, pady=5, padx=40,sticky="e")

temp_input_unit = ttk.Combobox(tab3, values=temperature_units, state="readonly", font=('Arial', 14), style="Custom.TCombobox")
temp_input_unit.grid(row=7, column=2, padx=0)

temp_input_value_label = tk.Label(tab3, text="Enter Value:", font=('Arial', 16, 'bold'), bg="floralwhite")
temp_input_value_label.grid(row=11, column=2, pady=10,padx=0)

temp_input_value = tk.Entry(tab3, font=('Arial', 16), background="white", relief="groove", width=16)
temp_input_value.grid(row=12, column=2, padx=30,sticky="e")

temp_output_label = tk.Label(tab3, text="Select output Unit:", font=('Arial', 16, 'bold'), bg="floralwhite")
temp_output_label.grid(row=6, column=2, pady=7, padx=40)

temp_output_unit = ttk.Combobox(tab3, values=temperature_units, state="readonly", font=('Arial', 14), style="Custom.TCombobox")
temp_output_unit.grid(row=7, column=4, padx=20,sticky="w")

temp_output_value_label = tk.Label(tab3, text="Converted Value:", font=('Arial', 16, 'bold'), bg="floralwhite")
temp_output_value_label.grid(row=11, column=4, pady=7)

temp_output_value = tk.Entry(tab3, font=('Arial', 16), background="white", relief="groove", width=16)
temp_output_value.grid(row=12, column=4, padx=30)

temp_convert_button = tk.Button(tab3, text="Convert", command=convert_temperature, fg="black", font=('Arial', 16, 'bold'), bg="springgreen4", relief="groove", width=8, height=1)
temp_convert_button.grid(row=23, column=3,padx=0, pady=20,sticky="n")

# Center the Convert button in the last row
temp_convert_button.grid(row=24, column=3, pady=20, sticky="n")

#image temp
image3 = Image.open("E:/PYTHON/PycharmProjects/pythonProject1/temperature (1).png")
image3 = image3.resize((140,140))
photo_image3 = ImageTk.PhotoImage(image3)
image_label3 = tk.Label(tab3, image=photo_image3,relief='flat',bg='floralwhite')
image_label3.place(x=1500,y=250)

# Place the image on the right side of the existing content in tab1
image_label3.grid(row=5, column=15, rowspan=10, padx=100, pady=10, sticky="e")



# Area  Function

def convert_area():

    try:
        # Get the input value and units
        value = float(area_input_value.get())  # Convert input to float
        from_unit = area_input_unit.get()     # Source unit
        to_unit = area_output_unit.get()      # Target unit

        # Define conversion factors
        conversion_factors = {
            # Base conversions involving Square Meter
            ("Square Meter", "Square Feet"): 10.7639,
            ("Square Feet", "Square Meter"): 1 / 10.7639,
            ("Square Centimeter", "Square Meter"): 1 / 10000,
            ("Square Meter", "Square Centimeter"): 10000,
            ("Square Millimeter", "Square Meter"): 1 / 1e6,
            ("Square Meter", "Square Millimeter"): 1e6,
            ("Square Kilometer", "Square Meter"): 1e6,
            ("Square Meter", "Square Kilometer"): 1 / 1e6,
            ("Square Mile", "Square Meter"): 2.59e6,
            ("Square Meter", "Square Mile"): 1 / 2.59e6,
            ("Square Yard", "Square Meter"): 0.836127,
            ("Square Meter", "Square Yard"): 1 / 0.836127,

            # Base conversions involving Square Feet
            ("Square Feet", "Square Centimeter"): 929.03,
            ("Square Centimeter", "Square Feet"): 1 / 929.03,
            ("Square Feet", "Square Millimeter"): 92903,
            ("Square Millimeter", "Square Feet"): 1 / 92903,
            ("Square Feet", "Square Kilometer"): 1 / 1.076e7,
            ("Square Kilometer", "Square Feet"): 1.076e7,
            ("Square Feet", "Square Mile"): 1 / 2.788e7,
            ("Square Mile", "Square Feet"): 2.788e7,
            ("Square Feet", "Square Yard"): 1 / 9,
            ("Square Yard", "Square Feet"): 9,

            # Base conversions involving Square Centimeter
            ("Square Centimeter", "Square Millimeter"): 100,
            ("Square Millimeter", "Square Centimeter"): 1 / 100,
            ("Square Kilometer", "Square Centimeter"): 1e10,
            ("Square Centimeter", "Square Kilometer"): 1 / 1e10,
            ("Square Mile", "Square Centimeter"): 2.59e10,
            ("Square Centimeter", "Square Mile"): 1 / 2.59e10,

            # Base conversions involving Square Millimeter
            ("Square Kilometer", "Square Millimeter"): 1e12,
            ("Square Millimeter", "Square Kilometer"): 1 / 1e12,
            ("Square Mile", "Square Millimeter"): 2.59e12,
            ("Square Millimeter", "Square Mile"): 1 / 2.59e12,

            # Base conversions involving Square Kilometer
            ("Square Kilometer", "Square Mile"): 1 / 2.59,
            ("Square Mile", "Square Kilometer"): 2.59,

            # Base conversions involving Square Yard
            ("Square Yard", "Square Mile"): 1 / 3.098e6,
            ("Square Mile", "Square Yard"): 3.098e6,
            ("Square Yard", "Square Kilometer"): 1 / 1.196e6,
            ("Square Kilometer", "Square Yard"): 1.196e6,
        }

        # Perform the conversion
        if from_unit == to_unit:
            result = value  # No conversion needed for identical units
        else:
            # Get the conversion factor for the specified units
            factor = conversion_factors.get((from_unit, to_unit))
            if factor:
                result = value * factor
            else:
                # Raise an error for unsupported conversions
                raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")

        # Display the result in the output field
        area_output_value.config(state='normal')
        area_output_value.delete(0, tk.END)
        area_output_value.insert(0, f"{result:.2f}")
        area_output_value.config(state='readonly')

    except ValueError as ve:
        # Handle invalid numeric input or unsupported unit conversions
        area_output_value.config(state='normal')
        area_output_value.delete(0, tk.END)
        area_output_value.insert(0, str(ve))
        area_output_value.config(state='readonly')

    except Exception as ex:
        # Catch any unexpected errors
        area_output_value.config(state='normal')
        area_output_value.delete(0, tk.END)
        area_output_value.insert(0, "An unexpected error occurred.")
        area_output_value.config(state='readonly')


# Area Tab: Widgets

area_units = ["Square Meter", "Square Feet", "Square Kilometer", "Square Millimeter", "Square Mile", "Square Yard"]

area_input_label = tk.Label(tab4, text="Select input Unit:", font=('Arial', 16, 'bold'), bg="floralwhite", relief='flat')
area_input_label.grid(row=6, column=4, pady=5, padx=40,sticky="e")

area_input_unit = ttk.Combobox(tab4, values=area_units, state="readonly", font=('Arial', 14), style="Custom.TCombobox")
area_input_unit.grid(row=7, column=2, padx=0)

area_input_value_label = tk.Label(tab4, text="Enter Value:", font=('Arial', 16, 'bold'), bg="floralwhite")
area_input_value_label.grid(row=11, column=2, pady=10,padx=0)

area_input_value = tk.Entry(tab4, font=('Arial', 16), background="white", relief="groove", width=16)
area_input_value.grid(row=12, column=2, padx=30,sticky="e")

area_output_label = tk.Label(tab4, text="Select output Unit:", font=('Arial', 16, 'bold'), bg="floralwhite")
area_output_label.grid(row=6, column=2, pady=7, padx=40)

area_output_unit = ttk.Combobox(tab4, values=area_units, state="readonly", font=('Arial', 14), style="Custom.TCombobox")
area_output_unit.grid(row=7, column=4, padx=20,sticky="w")

area_output_value_label = tk.Label(tab4, text="Converted Value:", font=('Arial', 16, 'bold'), bg="floralwhite")
area_output_value_label.grid(row=11, column=4, pady=7)

area_output_value = tk.Entry(tab4, font=('Arial', 16), background="white", relief="groove", width=16)
area_output_value.grid(row=12, column=4, padx=30)

area_convert_button = tk.Button(tab4, text="Convert", command=convert_area, fg="black", font=('Arial', 16, 'bold'), bg="springgreen4", relief="groove", width=8, height=1)
area_convert_button.grid(row=23, column=3,padx=0, pady=20,sticky="n")

# Center the Convert button in the last row
area_convert_button.grid(row=24, column=3, pady=20, sticky="n")

#image area
image4 = Image.open("E:/PYTHON/PycharmProjects/pythonProject1/arrow.png")
image4 = image4.resize((130,130))
photo_image4 = ImageTk.PhotoImage(image4)
image_label4 = tk.Label(tab4, image=photo_image4,relief='flat',bg='floralwhite')
image_label4.place(x=1400,y=20)

# Place the image on the right side of the existing content in tab1
image_label4.grid(row=6, column=13, rowspan=10, padx=100, pady=10, sticky="e")




def convert_volume():
    """
    Convert a volume measurement from one unit to another and display the result.
    Supported units: Cubic Inch, Cubic Feet, Cubic Centimeter, Cubic Millimeter,
                     Cubic Meter, Cubic Yard, Fluid Ounce, Cubic Mile.
    """
    try:
        # Get the input value and units
        value = float(volume_input_value.get())  # Convert input to float
        from_unit = volume_input_unit.get()     # Source unit
        to_unit = volume_output_unit.get()      # Target unit

        # Define conversion factors
        conversion_factors = {
            # Base conversions involving Cubic Meter
            ("Cubic Meter", "Cubic Feet"): 35.3147,
            ("Cubic Feet", "Cubic Meter"): 1 / 35.3147,
            ("Cubic Meter", "Cubic Inch"): 61023.7441,
            ("Cubic Inch", "Cubic Meter"): 1 / 61023.7441,
            ("Cubic Meter", "Cubic Centimeter"): 1e6,
            ("Cubic Centimeter", "Cubic Meter"): 1 / 1e6,
            ("Cubic Meter", "Cubic Millimeter"): 1e9,
            ("Cubic Millimeter", "Cubic Meter"): 1 / 1e9,
            ("Cubic Meter", "Cubic Yard"): 1.30795,
            ("Cubic Yard", "Cubic Meter"): 1 / 1.30795,
            ("Cubic Meter", "Cubic Mile"): 2.399e-10,
            ("Cubic Mile", "Cubic Meter"): 1 / 2.399e-10,
            ("Cubic Meter", "Fluid Ounce"): 33814.0227,
            ("Fluid Ounce", "Cubic Meter"): 1 / 33814.0227,

            # Base conversions involving Cubic Feet
            ("Cubic Feet", "Cubic Inch"): 1728,
            ("Cubic Inch", "Cubic Feet"): 1 / 1728,
            ("Cubic Feet", "Cubic Centimeter"): 28316.8466,
            ("Cubic Centimeter", "Cubic Feet"): 1 / 28316.8466,
            ("Cubic Feet", "Cubic Millimeter"): 2.83168e7,
            ("Cubic Millimeter", "Cubic Feet"): 1 / 2.83168e7,
            ("Cubic Feet", "Cubic Yard"): 1 / 27,
            ("Cubic Yard", "Cubic Feet"): 27,
            ("Cubic Feet", "Cubic Mile"): 3.531e-8,
            ("Cubic Mile", "Cubic Feet"): 1 / 3.531e-8,
            ("Cubic Feet", "Fluid Ounce"): 957.506,
            ("Fluid Ounce", "Cubic Feet"): 1 / 957.506,

            # Base conversions involving Cubic Inch
            ("Cubic Inch", "Cubic Centimeter"): 16.3871,
            ("Cubic Centimeter", "Cubic Inch"): 1 / 16.3871,
            ("Cubic Inch", "Cubic Millimeter"): 16387.064,
            ("Cubic Millimeter", "Cubic Inch"): 1 / 16387.064,
            ("Cubic Inch", "Fluid Ounce"): 0.554113,
            ("Fluid Ounce", "Cubic Inch"): 1 / 0.554113,

            # Base conversions involving Fluid Ounce
            ("Fluid Ounce", "Cubic Centimeter"): 29.5735,
            ("Cubic Centimeter", "Fluid Ounce"): 1 / 29.5735,
            ("Fluid Ounce", "Cubic Millimeter"): 29573.5,
            ("Cubic Millimeter", "Fluid Ounce"): 1 / 29573.5,

            # Base conversions involving Cubic Yard
            ("Cubic Yard", "Cubic Mile"): 2.143e-10,
            ("Cubic Mile", "Cubic Yard"): 1 / 2.143e-10,

            # Base conversions involving Cubic Mile
            ("Cubic Mile", "Cubic Centimeter"): 4.168e15,
            ("Cubic Centimeter", "Cubic Mile"): 1 / 4.168e15,
            ("Cubic Mile", "Cubic Millimeter"): 4.168e18,
            ("Cubic Millimeter", "Cubic Mile"): 1 / 4.168e18,
        }

        # Perform the conversion
        if from_unit == to_unit:
            result = value  # No conversion needed for identical units
        else:
            # Get the conversion factor for the specified units
            factor = conversion_factors.get((from_unit, to_unit))
            if factor:
                result = value * factor
            else:
                # Raise an error for unsupported conversions
                raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")

        # Display the result in the output field
        volume_output_value.config(state='normal')
        volume_output_value.delete(0, tk.END)
        volume_output_value.insert(0, f"{result:.6f}")
        volume_output_value.config(state='readonly')

    except ValueError as ve:
        # Handle invalid numeric input or unsupported unit conversions
        volume_output_value.config(state='normal')
        volume_output_value.delete(0, tk.END)
        volume_output_value.insert(0, str(ve))
        volume_output_value.config(state='readonly')

    except Exception as ex:
        # Catch any unexpected errors
        volume_output_value.config(state='normal')
        volume_output_value.delete(0, tk.END)
        volume_output_value.insert(0, "An unexpected error occurred.")
        volume_output_value.config(state='readonly')


# Volume Tab: Widgets

volume_units = ["Cubic Meter", "Cubic Feet", "Cubic Inch", "Cubic Centimeter", "Cubic Millimeter", "Cubic Yard", "Fluid Ounce", "Cubic Mile"]

volume_input_label = tk.Label(tab5, text="Select input Unit:", font=('Arial', 16, 'bold'), bg="floralwhite", relief='flat')
volume_input_label.grid(row=6, column=4, pady=5, padx=40,sticky="e")

volume_input_unit = ttk.Combobox(tab5, values=volume_units, state="readonly", font=('Arial', 14), style="Custom.TCombobox")
volume_input_unit.grid(row=7, column=2, padx=0)

volume_input_value_label = tk.Label(tab5, text="Enter Value:", font=('Arial', 16, 'bold'), bg="floralwhite")
volume_input_value_label.grid(row=11, column=2, pady=10,padx=0)

volume_input_value = tk.Entry(tab5, font=('Arial', 16), background="white", relief="groove", width=16)
volume_input_value.grid(row=12, column=2, padx=30,sticky="e")

volume_output_label = tk.Label(tab5, text="Select output Unit:", font=('Arial', 16, 'bold'), bg="floralwhite")
volume_output_label.grid(row=6, column=2, pady=7, padx=40)

volume_output_unit = ttk.Combobox(tab5, values=volume_units, state="readonly", font=('Arial', 14), style="Custom.TCombobox")
volume_output_unit.grid(row=7, column=4, padx=20,sticky="w")

volume_output_value_label = tk.Label(tab5, text="Converted Value:", font=('Arial', 16, 'bold'), bg="floralwhite")
volume_output_value_label.grid(row=11, column=4, pady=7)

volume_output_value = tk.Entry(tab5, font=('Arial', 16), background="white", relief="groove", width=16)
volume_output_value.grid(row=12, column=4, padx=30)

volume_convert_button = tk.Button(tab5, text="Convert", command=convert_volume, fg="black", font=('Arial', 16, 'bold'), bg="springgreen4", relief="groove", width=8, height=1)
volume_convert_button.grid(row=23, column=3,padx=0, pady=20,sticky="n")

# Center the Convert button in the last row
length_convert_button.grid(row=24, column=3, pady=20, sticky="n")

#image volume
image5 = Image.open("E:/PYTHON/PycharmProjects/pythonProject1/sound.png")
image5 = image5.resize((115,115))
photo_image5 = ImageTk.PhotoImage(image5)
image_label5 = tk.Label(tab5, image=photo_image5,relief='flat',bg='floralwhite')
image_label5.place(x=1500,y=230)

# Place the image on the right side of the existing content in tab1
image_label5.grid(row=5, column=15, rowspan=10, padx=100, pady=10, sticky="e")

def convert_time():
    """
    Convert a time measurement from one unit to another and display the result.
    Supported units: Second, Millisecond, Microsecond, Nanosecond,
                     Minute, Hour, Day, Week, Year.
    """
    try:
        # Get the input value and units
        value = float(time_input_value.get())  # Convert input to float
        from_unit = time_input_unit.get()     # Source unit
        to_unit = time_output_unit.get()      # Target unit

        # Define conversion factors
        conversion_factors = {
            # Base conversions involving Seconds
            ("Second", "Millisecond"): 1e3,
            ("Millisecond", "Second"): 1 / 1e3,
            ("Second", "Microsecond"): 1e6,
            ("Microsecond", "Second"): 1 / 1e6,
            ("Second", "Nanosecond"): 1e9,
            ("Nanosecond", "Second"): 1 / 1e9,
            ("Second", "Minute"): 1 / 60,
            ("Minute", "Second"): 60,
            ("Second", "Hour"): 1 / 3600,
            ("Hour", "Second"): 3600,
            ("Second", "Day"): 1 / 86400,
            ("Day", "Second"): 86400,
            ("Second", "Week"): 1 / 604800,
            ("Week", "Second"): 604800,
            ("Second", "Year"): 1 / 31536000,
            ("Year", "Second"): 31536000,

            # Base conversions involving Milliseconds
            ("Millisecond", "Microsecond"): 1e3,
            ("Microsecond", "Millisecond"): 1 / 1e3,
            ("Millisecond", "Nanosecond"): 1e6,
            ("Nanosecond", "Millisecond"): 1 / 1e6,
            ("Millisecond", "Minute"): 1 / 60000,
            ("Minute", "Millisecond"): 60000,
            ("Millisecond", "Hour"): 1 / 3.6e6,
            ("Hour", "Millisecond"): 3.6e6,
            ("Millisecond", "Day"): 1 / 8.64e7,
            ("Day", "Millisecond"): 8.64e7,
            ("Millisecond", "Week"): 1 / 6.048e8,
            ("Week", "Millisecond"): 6.048e8,
            ("Millisecond", "Year"): 1 / 3.154e10,
            ("Year", "Millisecond"): 3.154e10,

            # Base conversions involving Microseconds
            ("Microsecond", "Nanosecond"): 1e3,
            ("Nanosecond", "Microsecond"): 1 / 1e3,

            # Base conversions involving Minutes
            ("Minute", "Hour"): 1 / 60,
            ("Hour", "Minute"): 60,
            ("Minute", "Day"): 1 / 1440,
            ("Day", "Minute"): 1440,
            ("Minute", "Week"): 1 / 10080,
            ("Week", "Minute"): 10080,
            ("Minute", "Year"): 1 / 525600,
            ("Year", "Minute"): 525600,

            # Base conversions involving Hours
            ("Hour", "Day"): 1 / 24,
            ("Day", "Hour"): 24,
            ("Hour", "Week"): 1 / 168,
            ("Week", "Hour"): 168,
            ("Hour", "Year"): 1 / 8760,
            ("Year", "Hour"): 8760,

            # Base conversions involving Days
            ("Day", "Week"): 1 / 7,
            ("Week", "Day"): 7,
            ("Day", "Year"): 1 / 365,
            ("Year", "Day"): 365,
        }

        # Perform the conversion
        if from_unit == to_unit:
            result = value  # No conversion needed for identical units
        else:
            # Get the conversion factor for the specified units
            factor = conversion_factors.get((from_unit, to_unit))
            if factor:
                result = value * factor
            else:
                # Raise an error for unsupported conversions
                raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")

        # Display the result in the output field
        time_output_value.config(state='normal')
        time_output_value.delete(0, tk.END)
        time_output_value.insert(0, f"{result:.6f}")
        time_output_value.config(state='readonly')

    except ValueError as ve:
        # Handle invalid numeric input or unsupported unit conversions
        time_output_value.config(state='normal')
        time_output_value.delete(0, tk.END)
        time_output_value.insert(0, str(ve))
        time_output_value.config(state='readonly')

    except Exception as ex:
        # Catch any unexpected errors
        time_output_value.config(state='normal')
        time_output_value.delete(0, tk.END)
        time_output_value.insert(0, "An unexpected error occurred.")
        time_output_value.config(state='readonly')


# Time Tab: Widgets

time_units = ["Second", "Millisecond", "Microsecond", "Nanosecond", "Minute", "Hour", "Day", "Week", "Year"]

time_input_label = tk.Label(tab6, text="Select input Unit:", font=('Arial', 16, 'bold'), bg="floralwhite", relief='flat')
time_input_label.grid(row=6, column=4, pady=5, padx=40,sticky="e")

time_input_unit = ttk.Combobox(tab6, values=time_units, state="readonly", font=('Arial', 14), style="Custom.TCombobox")
time_input_unit.grid(row=7, column=2, padx=0)

time_input_value_label = tk.Label(tab6, text="Enter Value:", font=('Arial', 16, 'bold'), bg="floralwhite")
time_input_value_label.grid(row=11, column=2, pady=10,padx=0)

time_input_value = tk.Entry(tab6, font=('Arial', 16), background="white", relief="groove", width=16)
time_input_value.grid(row=12, column=2, padx=30,sticky="e")

time_output_label = tk.Label(tab6, text="Select output Unit:", font=('Arial', 16, 'bold'), bg="floralwhite")
time_output_label.grid(row=6, column=2, pady=7, padx=40)

time_output_unit = ttk.Combobox(tab6, values=time_units, state="readonly", font=('Arial', 14), style="Custom.TCombobox")
time_output_unit.grid(row=7, column=4, padx=20,sticky="w")

time_output_value_label = tk.Label(tab6, text="Converted Value:", font=('Arial', 16, 'bold'), bg="floralwhite")
time_output_value_label.grid(row=11, column=4, pady=7)

time_output_value = tk.Entry(tab6, font=('Arial', 16), background="white", relief="groove", width=16)
time_output_value.grid(row=12, column=4, padx=30)

time_convert_button = tk.Button(tab6, text="Convert", command=convert_time, fg="black", font=('Arial', 16, 'bold'), bg="springgreen4", relief="groove", width=8, height=1)
time_convert_button.grid(row=23, column=3,padx=0, pady=20,sticky="n")

# Center the Convert button in the last row
length_convert_button.grid(row=24, column=3, pady=20, sticky="n")

#image time
image6 = Image.open("E:/PYTHON/PycharmProjects/pythonProject1/time (1).png")
image6 = image6.resize((150,150))
photo_image6 = ImageTk.PhotoImage(image6)
image_label6 = tk.Label(tab6, image=photo_image6,relief='flat',bg='floralwhite')
image_label6.place(x=1500,y=230)

# Place the image on the right side of the existing content in tab1
image_label6.grid(row=5, column=15, rowspan=10, padx=100, pady=10, sticky="e")



root.mainloop()
