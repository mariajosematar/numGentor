# NumGen
This program is utilized to create thousands of validated phone numbers in a matter of seconds. As of now NumGen only generates numbers with a +1 country code, and all states/provinces inside the country.

Make sure to run the command 'pip install -r requirements.txt' to install all the modules needed for NumGen to run, brefore using NumGen. 

## How NumGen is Used:
NumGen uses parameters, which are passed as you launch the python file via terminal.

Example: python NumGen.py -a 1000

Example: python NumGen.py --reference

### Parameters:
-a AMOUNT, --amount AMOUNT   -> Using this parameter sets the amount of numbers to generate.

-b, --reference   -> Using this Paramter runs 5, 10 seconds references of NumGen to see how many numbers your system is capable of generating every 10 seconds.