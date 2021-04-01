import matplotlib.pyplot as plt 
#%% Write your data
time = [0, 1, 2, 3] # days
temperature = [28.05, 29.00, 28.65, 27.04] # dC
agitation = [400, 397, 402, 430] # rpm
DO = [71, 5, 5.5, 2] # %
pH = [5.5, 5.2, 4.9, 4.75] # pH
gas_flow = [1, 1.02, 1.01, 1.05]  #vvm

#%% Set up the plot 

fig, host = plt.subplots(figsize=(8,5)) # (width, height) in inches

# Define the number of secondary axis here    
par1 = host.twinx()
par2 = host.twinx()
par3 = host.twinx()
par4 = host.twinx()

# Define the limits of each axis plot here
host.set_xlim(0, 3)      # Time
host.set_ylim(0, 30)     # Temperature
par1.set_ylim(300, 500)  # Agitation
par2.set_ylim(0, 100)    # DO
par3.set_ylim(0, 7)      # pH
par4.set_ylim(0.9, 1.1)  # gas_flow

# Set the label of the different  axis here
host.set_xlabel("Time")
host.set_ylabel("Temperature")
par1.set_ylabel("Agitation")
par2.set_ylabel("DO")
par3.set_ylabel("pH")
par4.set_ylabel("gas_flow")


# Set the colormaps
color1 = plt.cm.plasma(0)
color2 = plt.cm.plasma(0.25)
color3 = plt.cm.plasma(0.5)
color4 = plt.cm.plasma(0.75)
color5 = plt.cm.plasma(0.9)

# Plot the data
p1, = host.plot(time, temperature,    color=color1, label="Temperature")
p2, = par1.plot(time, agitation,    color=color2, label="Agitation")
p3, = par2.plot(time, DO, color=color3, label="DO")
p4, = par3.plot(time, pH, color=color4, label="pH")
p5, = par4.plot(time, gas_flow, color=color5, label="Gas_flow")


lns = [p1, p2, p3, p4, p5]
host.legend(handles=lns, loc='best')

# right, left, top, bottom
par2.spines['right'].set_position(('outward', 60))
par3.spines['right'].set_position(('outward', 120))
par4.spines['right'].set_position(('outward', 180))

# no x-ticks                 
par2.xaxis.set_ticks([])
par3.xaxis.set_ticks([])
par4.xaxis.set_ticks([])

host.yaxis.label.set_color(p1.get_color())
par1.yaxis.label.set_color(p2.get_color())
par2.yaxis.label.set_color(p3.get_color())
par3.yaxis.label.set_color(p4.get_color())
par4.yaxis.label.set_color(p5.get_color())

# Adjust spacings w.r.t. figsize
fig.tight_layout()


#%% Save the figure
plt.savefig("fermentation_profile.pdf")
