package visualcontrol

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// Clear screen function for a cleaner UI
func clearScreen() {
	fmt.Print("\033[H\033[2J")
}

// Print a stylized header
func printHeader() {
	fmt.Println("=========================")
	fmt.Println("🐢 ShellForge CLI Menu 🐢")
	fmt.Println("=========================")
	//fmt.Println("Not every shell is for hiding. Some are built to withstand")
}

// Display menu options with icons
func displayMenu() {
	fmt.Println("\nChoose an option:")
	fmt.Println("1. 🏠 My Modpacks")
	fmt.Println("2. 🛠️  Create Modpack")
	fmt.Println("3. 🔎 Browse Modpacks")
	fmt.Println("0. ❌ Exit")
}

// Handle user selection
func handleSelection(selection string) {
	switch selection {
	case "1":
		fmt.Println("🏠 Viewing My Modpacks...")
	case "2":
		fmt.Println("🛠️  Creating a New Modpack...")
	case "3":
		fmt.Println("🔎  Browsing Modpacks...")
		clearScreen()
		displayBrowseMenu()
	case "0":
		fmt.Println("❌ Exiting...")
		os.Exit(0)
	default:
		fmt.Println("⚠️  Invalid selection, please try again!")
	}
}

func RunMenu() {
	scanner := bufio.NewScanner(os.Stdin)
	for {
		clearScreen()
		printHeader()
		displayMenu()
		fmt.Print("\nEnter your choice: ")

		scanner.Scan()
		choice := strings.TrimSpace(scanner.Text())
		handleSelection(choice)

		fmt.Println("\nPress Enter to continue...")
		scanner.Scan()
	}
}
