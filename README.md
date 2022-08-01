# DISC_Impedance_Testing
Automate IDE impedance data analysis process. Avoid copy &amp; paste!

## Follow these steps for Accelerated Aging Testing!
### Impedance Measurement
Step 1: Turn on Autolab and connect to the lab Dell PC. <br /><br />
Step 2: Setup the IDE in the Ferrari Cage. <br />

For old IDEs (12, 16, 20):<br />
1) Open the cap.<br /> 
2) Put PBS inside the cap.<br /> 
3) Put wire inside PBS. Make sure the wire is not touching the intricate device.<br /> 
4) Connect CE (Counting Electrode) to mutual / shunt wire.<br /> 
5) Connect WE (Working Electrode) to 2/4/8/16 wire.<br /> 

For new IDEs (22+):<br />
1) Remove the tape on the cap. <br /> 
2) Insert water into the tube with needle.<br /> 
3) Put wire inside the tube through the hole on the cap.<br /> 
4) Tilt the tube to see if there's any air bubble. If yes, insert more water to make sure the tube is filled. <br /> 
5) Connect WE (Working Electrode) to 2/4/8/16 wire.<br /> 

Step 3: Open Nova2.1.4 software with the procedure **"FRA MUX 1ch 50mV 10k-10Hz - automated"**. <br /><br />
Step 4: Change the export file-name to corresponding IDE. <br /> E.g: <br />12-8-m means IDE 12, 8µm, mutual. <br /> 16-16-s means IDE 16, 16µm, shunt <br /><br />
Step 5: Click on the run button and wait for the test result.<br /><br />
Step 6: Nova2.1.4 will auto-generate a csv file for each IDE in the ASCI format. File location:Desktop/IDE-data. <br /><br />
Step 7: Edit the **"date.csv"** file to keep track of the experiment dates. <br /><br />
Step 8: Clean the IDE and put it back to the Lab Armor. <br />

For all IDEs:<br />
1) Make sure the tube is filled full with solution.<br />
2) If new IDE: Add new tape on the hole of the cap to prevent water evaporation.
3) Wrap the device with sealing. Stretch the sealing to ensure close contact. 
4) Spray oil on the tube and the incubator to prevent device getting stuck. 
5) Add covers on the incubator to ensure heat preservation.


### Data Analysis 
Step 1: Open the jupyter notebook on terminal. <br /><br />
Step 2: Open the file **"[20220609]TBBL-Impedance Data Analysis"**.  <br /><br />
Step 3: Run Jupyter Notebook and get your awesome data graphs!
