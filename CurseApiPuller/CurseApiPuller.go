package curseapipuller

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"path/filepath"
)

// Define constants
const (
	apiKey  = "$2a$10$LUzqSIJ0rMjnskXfHlMBUuquDmnr0RHAiiOrDequpxip3T36f3Y2S" // Replace with your actual API key
	dataDir = "data"                                                         // Directory to store the JSON files
	url     = "https://api.curseforge.com/v1/mods/search"                    // The API URL
)

// Define the request headers
var headers = map[string]string{
	"Accept":    "application/json",
	"x-api-key": apiKey,
}

func RunSort() {
	// Ensure the data directory exists
	if _, err := os.Stat(dataDir); os.IsNotExist(err) {
		if err := os.Mkdir(dataDir, 0755); err != nil {
			fmt.Println("Error creating data directory:", err)
			return
		}
	}

	// First request and save to test_dump.json
	params1 := map[string]string{
		"gameId":    "432",
		"classId":   "6",
		"sortOrder": "desc",
		"sortField": "6",
	}
	err := sendRequestAndSave(url, params1, filepath.Join(dataDir, "test_dump.json"))
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
}

// sendRequestAndSave sends an HTTP GET request and saves the JSON response to a file
func sendRequestAndSave(url string, params map[string]string, filename string) error {
	// Build the HTTP request
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return fmt.Errorf("error creating request: %w", err)
	}

	// Add headers to the request
	for key, value := range headers {
		req.Header.Add(key, value)
	}

	// Add query parameters
	query := req.URL.Query()
	for key, value := range params {
		query.Add(key, value)
	}
	req.URL.RawQuery = query.Encode()

	// Make the HTTP request
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return fmt.Errorf("error sending request: %w", err)
	}
	defer resp.Body.Close()

	// Check for 403 Forbidden status
	if resp.StatusCode == http.StatusForbidden {
		return fmt.Errorf("HTTP Request failed with status code: %d", resp.StatusCode)
	}

	// Read the response body
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return fmt.Errorf("error reading response body: %w", err)
	}

	// Unmarshal the body into an interface to check for JSON errors
	var result interface{}
	if err := json.Unmarshal(body, &result); err != nil {
		return fmt.Errorf("error unmarshalling JSON: %w", err)
	}

	// Save the response body to a file
	file, err := os.Create(filename)
	if err != nil {
		return fmt.Errorf("error creating file %s: %w", filename, err)
	}
	defer file.Close()

	if _, err := file.Write(body); err != nil {
		return fmt.Errorf("error writing to file %s: %w", filename, err)
	}

	fmt.Printf("Successfully dumped to %s\n", filename)
	return nil
}
