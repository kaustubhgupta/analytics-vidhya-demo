from pywebio.input import *
from pywebio.output import put_text
from pywebio.exceptions import SessionClosedException


def demo():

    inputs = input_group("All Input Types", [
        input("Integer Input", type=NUMBER, name="integer_in"),
        textarea("This is a text area", type=TEXT, name='text_area'),
        select("This is a selection", options=[
               ('Software Engineer', 1), ('Data Analyst', 2), ('Artist', 3)], name='selection'),
        checkbox("This is a checkbox", options=[
                 ('Software Engineer', 1), ('Data Analyst', 2), ('Artist', 3)], name='check_box'),
        radio("This is a radio selection", options=[
              ('Software Engineer', 1), ('Data Analyst', 2), ('Artist', 3)], name='radio_selection')
    ])
    put_text("Integer: {}\nTextArea: {}\nSelection: {}\nCheckBox: {}\nRadioButton: {}".format(
        inputs['integer_in'], inputs['text_area'], inputs['selection'], inputs['check_box'], inputs['radio_selection']))


if __name__ == "__main__":
    try:
        demo()
    except SessionClosedException:
        print("The session was closed unexpectedly")
