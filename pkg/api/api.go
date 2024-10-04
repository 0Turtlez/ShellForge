package api

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"path/filepath"
	"strconv"
	// "encoding/json"
	// "io"
	// "os"
	// "path/filepath"
)

const (
	apiKey  = "$2a$10$LUzqSIJ0rMjnskXfHlMBUuquDmnr0RHAiiOrDequpxip3T36f3Y2S"
	dataDir = "data/"
	url     = "https://api.curseforge.com/v1/mods/search" // The API URL
)

var headers = map[string]string{
	"Accept":    "application/json",
	"x-api-key": apiKey,
}

func RunSort() {
	for page := 0; page < 50; page++ {
		params := map[string]string{
			"gameId":    "432",
			"classId":   "6",
			"sortOrder": "desc",
			"sortField": "6",
			"index":     strconv.Itoa(page * 50),
		}

		fileName := "page" + strconv.Itoa(page) + ".json"

		sendRequestAndSave(url, params, filepath.Join(dataDir+fileName))
	}
}

func sendRequestAndSave(url string, params map[string]string, filename string) error {
	// Build the http request
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return fmt.Errorf("error creating request: %w", err)
	}

	// Add headers to request
	for key, value := range headers {
		req.Header.Add(key, value)
	}

	// Adds query params
	query := req.URL.Query()
	for key, value := range params {
		query.Add(key, value)
	}
	req.URL.RawQuery = query.Encode()

	// Makes http request
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return fmt.Errorf("error sending request: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		print("HTTP Request failed with status code: %d", resp.StatusCode)
	}

	// Reads the response body
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return fmt.Errorf("error reading response body: %w", err)
	}

	// Makes body into interface so go can read it
	var result interface{}
	if err := json.Unmarshal(body, &result); err != nil {
		return fmt.Errorf("error unmarshalling JSON: %w", err)
	}

	// Pretty-Print JSON
	prettyJSON, err := json.MarshalIndent(result, "", "    ")
	if err != nil {
		return fmt.Errorf("error formatting JSON: %w", err)
	}

	// Create file
	file, err := os.Create(filename)
	if err != nil {
		return fmt.Errorf("error creating file %s: %w", filename, err)
	}
	defer file.Close()

	// Save JSON to file
	if _, err := file.Write(prettyJSON); err != nil {
		return fmt.Errorf("error writing to file %s: %w", filename, err)
	}

	return nil
}
