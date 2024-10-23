#Establishing the main python file to run the modular code.
#to run streamlit run the command from the root:
#py -m streamlit run main.py

from utils.Views.Home import mainDisplay

if __name__ == "__main__":
    mainDisplay()