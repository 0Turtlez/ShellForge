package main

import (
	api "ShellForge/pkg/api"
	"ShellForge/pkg/display"
)

func main() {
	// startTime := time.Now()

	go api.RunSort()
	display.RunMenu("mainMenu")
	// elsapsedTime := time.Since(startTime)

	// display.RunMenu(elsapsedTime)
}

/*
TODO:
	Add Sorting options
	wireshark ftb, and curse

*/
