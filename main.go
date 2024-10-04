package main

import (
	api "ShellForge/pkg/api"
)

func main() {
	// startTime := time.Now()

	go api.RunSort()
	main.RunMenu("mainMenu")
	// elsapsedTime := time.Since(startTime)

	// display.RunMenu(elsapsedTime)
}

/*
TODO:
	Add Sorting options
	wireshark ftb, and curse

*/
