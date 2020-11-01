# DuelLinks-Interface

This project uses Flask and PyAutoGUI to control the Duel Links App via a Smartphone, enabling the player to use the Smartphone as a Duel Disk with a brand new interface. The Flask server allows the display of the controls and it's endpoints control the game's behavious via PyAutoGUI.
 

# Dependencies

Just create a **virtual environment**

    mkvirtualenv DuelDisk
    workon DuelDisk

And install the **requirements.txt**

    pip install requirements.txt
    
# Run and access from smartphone

Simply run from the project folder by 

    flask run --host=0.0.0.0
    
Now that the server is running type this you computer's IP address in your smartphone's browser followed by the 5000 port

    your_computers_ip:5000
    
In example:

    192.168.0.12:5000
    
At this point simply open the Duel Links app from Steam and once you are in a Duel you'll be able to use your smartphone as an interface
