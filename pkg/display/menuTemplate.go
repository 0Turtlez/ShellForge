package display

import (
	"ShellForge/pkg/utils"
	"bufio"
	"fmt"
	"os"
	"strings"
)

// Define a menu structure
type Menu struct {
	Title   string
	Options []string
	Handler func(string)
}

// Global menu registry
var menus = map[string]Menu{}

// Register menus on initialization
func init() {
	menus["mainMenu"] = Menu{
		Title:   "ShellForge CLI Menu",
		Options: []string{"🏠 My Modpacks", "🛠️ Create Modpack", "🔎 Browse Modpacks", "❌ Exit"},
		Handler: MainMenuHandler,
	}
	menus["browseMenu"] = Menu{
		Title:   "Browse Modpacks",
		Options: []string{"Modpack 1", "Modpack 2", "Back"},
		Handler: BrowseMenuHandler,
	}
}

// Generalized RunMenu function that uses menu names
func RunMenu(menuName string) {
	if menu, exists := menus[menuName]; exists {
		scanner := bufio.NewScanner(os.Stdin)
		for {
			utils.ClearScreen()
			printHeader(menu.Title)
			displayOptions(menu.Options)
			fmt.Print("\nEnter your choice: ")

			scanner.Scan()
			choice := strings.TrimSpace(scanner.Text())
			menu.Handler(choice)

			fmt.Println("\nPress Enter to continue...")
			scanner.Scan()
		}
	} else {
		fmt.Printf("⚠️ Menu %s not found!\n", menuName)
	}
}

// Print the header with a dynamic title
func printHeader(title string) {
	fmt.Println("=========================")
	fmt.Printf("🐢 %s 🐢\n", title)
	fmt.Println("=========================")
}

// Dynamically display menu options
func displayOptions(options []string) {
	for i, option := range options {
		fmt.Printf("%d. %s\n", i, option)
	}
}

// Main menu handler function
func MainMenuHandler(selection string) {
	switch selection {
	case "0":
		fmt.Println("❌ Exiting...")
		os.Exit(0)
	case "1":
		fmt.Println("🏠 Viewing My Modpacks...")
	case "2":
		fmt.Println("🛠️  Creating a New Modpack...")
	case "3":
		fmt.Println("🔎  Browsing Modpacks...")
		utils.ClearScreen()
		RunMenu("browseMenu")
	default:
		fmt.Println("⚠️ Invalid selection, please try again!")
	}
}

// Browse menu handler function
func BrowseMenuHandler(selection string) {
	switch selection {
	case "0":
		fmt.Println("❌ Going back...")
		RunMenu("mainMenu")
	case "1":
		fmt.Println("Viewing Modpack 1...")
	case "2":
		fmt.Println("Viewing Modpack 2...")
	default:
		fmt.Println("⚠️ Invalid selection, please try again!")
	}
}
