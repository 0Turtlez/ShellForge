package main

import (
	apihandling "ShellForge/APIHandling"
	visualcontrol "ShellForge/VisualControl"
)

func main() {

	go apihandling.RunSort()
	visualcontrol.RunMenu()
}

/*
TODO:
# find a way to run the api while or after the menu is populated
# and also ways to cache data, or more efficent ways to run app
#
------- Current Startup time: 156.131542ms -------

# Add Sorting options
# Multiple pagination
#
*/
