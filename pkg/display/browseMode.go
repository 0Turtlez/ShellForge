package display

import (
	"ShellForge/pkg/schema"
	"ShellForge/pkg/utils"
	"bufio"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

const (
	dataFolderPath string = "data/"
)

func displayBrowseMenu() {
	var page int = 0
	scanner := bufio.NewScanner(os.Stdin)

	for {
		utils.ClearScreen()
		fmt.Println("=================")
		fmt.Println("🔎 Browse View 🔎")
		fmt.Println("=================")
		displayModInfo(page)

		scanner.Scan()
		choice := strings.TrimSpace(scanner.Text())

		// TODO: ADD LIMITS TO SCROLL TO SIZE OF TOTAL ITEMS HIGH END AND LOW
		switch choice {
		case "f":
			page++
		case "b":
			page--
		default:
			fmt.Println("invalid option please use + or -")
		}
	}
}

func displayModInfo(page int) {
	jsonPath := dataFolderPath + "page" + strconv.Itoa(page) + ".json"
	println(jsonPath)

	file, err := os.Open(jsonPath)
	if err != nil {
		fmt.Printf("Error opening file %s: %v\n", jsonPath, err)
		return
	}
	defer file.Close()

	// Read all the contents of the file
	contents, err := ioutil.ReadAll(file)
	if err != nil {
		fmt.Printf("Error reading file %s: %v\n", jsonPath, err)
		return
	}

	// Parse the JSON into the Root struct
	var root schema.Root
	if err := json.Unmarshal(contents, &root); err != nil {
		fmt.Printf("Error parsing JSON: %v\n", err)
		return
	}

	// Print out a few fields to confirm the parsing was successful
	fmt.Println("Number of ModData Entries:", len(root.Data))
	if len(root.Data) > 0 {
		for i := 0; i < 50 && i < len(root.Data); i++ {

			modName := root.Data[i].Name
			firstAuthor := root.Data[i].Authors[0].Name
			downloadCount := root.Data[i].DownloadCount
			fmt.Printf("%4d | %-30.30s | %-10.10s | %10d \n", i+1, modName, firstAuthor, downloadCount)
		}
	}
}

// TODO:
// ADD INSTALL COMMAND
// ADD GRAPHICALLY DISPLAY FOR INSTALLED MODS
//
