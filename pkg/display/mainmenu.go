package display

import (
	utils "ShellForge/pkg/utils"
	"bufio"
	"fmt"
	"os"
	"strings"
	"time"
)

// Print a stylized header
func printMMHeader() {
	fmt.Println("=========================")
	fmt.Println("🐢 ShellForge CLI Menu 🐢")
	fmt.Println("=========================")
	//fmt.Println("Not every shell is for hiding. Some are built to withstand")
}

// Display menu options with icons
func displayMainMenu() {
	fmt.Println("\nChoose an option:")
	fmt.Println("1. 🏠 My Modpacks")
	fmt.Println("2. 🛠️  Create Modpack")
	fmt.Println("3. 🔎 Browse Modpacks")
	fmt.Println("0. ❌ Exit")
}

// Handle user selection
func handleMainMenuSelections(selection string) {
	switch selection {
	case "1":
		fmt.Println("🏠 Viewing My Modpacks...")
	case "2":
		fmt.Println("🛠️  Creating a New Modpack...")
	case "3":
		fmt.Println("🔎  Browsing Modpacks...")
		utils.ClearScreen()
		displayBrowseMenu()
	case "0":
		fmt.Println("❌ Exiting...")
		os.Exit(0)
	default:
		fmt.Println("⚠️ Invalid selection, please try again!")
	}
}

func RunMainMenu(time time.Duration) {
	scanner := bufio.NewScanner(os.Stdin)
	for {
		utils.ClearScreen()
		fmt.Printf("Time to Start: %s\n", time)
		printMMHeader()
		displayMainMenu()
		fmt.Print("\nEnter your choice: ")

		scanner.Scan()
		choice := strings.TrimSpace(scanner.Text())
		handleMainMenuSelections(choice)

		fmt.Println("\nPress Enter to continue...")
		scanner.Scan()
	}
}
