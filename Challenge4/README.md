# Challenge 4: Lmfitting

This Challenge simulates a rudimentary method for fitting data.  I have generated sample data (with some random noise added) for an AlCl transition at a particular temperature.  Your job, is to read in the data from the data file and frequency file and use lmfit to fit the same doppler broadened gaussian function from Challenge 3.  Your script should print to the terminal window the transition line (f0) and the temperature of the sample (T).

## Simulated Procedure for Data

1. Set laser to frequency and save frequency setpoint to "freq_file.txt"
2. Record absorption at that frequency and save to "data_file.txt"


## Challenge Tasks

1. Read in freq_file.txt and data_file.txt (I recommend using the np.genfromtxt() function)
2. Perform a lmfit using the doppler broadened gaussian function
3. Print out the extracted transition frequency and temperature (or have the values displayed on the following plot)
4. Using matplotlib.pyplot, make a scatter plot of the data with a plot of the gaussian fit overlaid.