struct drivers{
    speed = int			## vehicle speed
    joined_date = Date	## time joined to suber
    busy_time = Time	## time to get free for next comuniters
}

N = number_of_commuter
M = number_of_drivers
answers = []
for i in range(number_of_commuter):
    # Update drivers.busy_time O(m)

    # filter drivers according to busy_time and save the drivers which busy_time is zero O(m)
    
	# max heap drivers with first key speed and second key is joined date O(mlogm)

	# assign first driver to the comuuter and driver.busy_time to a specific time O(1)
	# and assign index driver to answers[i] O(1)
 

# over all O(mnlogm)