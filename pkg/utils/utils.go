package utils

import "fmt"

// Clear screen function for a cleaner UI
func ClearScreen() {
	fmt.Print("\033[H\033[2J")
}
