import psspy
import redirect

redirect.psse2py()
psspy.psseinit(20000)

# Load case (user to modify)
psspy.case("network.sav")
psspy.dyre_new([1,1,1,1], "network.dyr", "", "", "")

# Channel setup
psspy.delete_all_plot_channels()
psspy.chsb(0, 1, [-1, -1, -1, 1, 13, 0])  # Rotor angle
psspy.chsb(0, 1, [-1, -1, -1, 1, 7, 0])   # Bus voltage

# Start simulation
psspy.strt(0, "output.out")

# Apply fault
psspy.dist_bus_fault(7, 3, 0.0, [0.0, 0.0])

# Clear fault
psspy.run(0, 0.2, 1, 1, 0)
psspy.dist_clear_fault(1)

# Run post-fault
psspy.run(0, 5.0, 1, 1, 0)