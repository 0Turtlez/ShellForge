package schema

type Root struct {
	Data []ModData `json:"data"`
}

// PopularityRank 	= sort by popularity
// DownloadCount 	= sort by downloads
// Name 			= sort by name
// ID				= sort by ID
type ModData struct {
	AllowModDistribution bool                 `json:"allowModDistribution"`
	Authors              []Author             `json:"authors"`
	Categories           []Category           `json:"categories"`
	ClassID              int                  `json:"classId"`
	DateCreated          string               `json:"dateCreated"`
	DateModified         string               `json:"dateModified"`
	DateReleased         string               `json:"dateReleased"`
	DownloadCount        int                  `json:"downloadCount"`
	GameID               int                  `json:"gameId"`
	PopularityRank       int                  `json:"gamePopularityRank"`
	ID                   int                  `json:"id"`
	IsAvailable          bool                 `json:"isAvailable"`
	IsFeatured           bool                 `json:"isFeatured"`
	LatestFiles          []LatestFiles        `json:"latestFiles"`
	LatestFilesIndexes   []LatestFilesIndexes `json:"latestFilesIndexes"`
	Links                Links                `json:"links"`
	Logo                 Logo                 `json:"logo"`
	MainFileID           int                  `json:"mainFileId"`
	Name                 string               `json:"name"`
	PrimaryCategoryId    int                  `json:"primaryCategoryId"`
	ScreenShots          []ScreenShots        `json:"screenshots"`
	Slug                 string               `json:"slug"`
	Status               int                  `json:"status"`
	Summary              string               `json:"summary"`
	ThumbsUpCount        int                  `json:"thumbsUpCount"`
}

type Author struct {
	ID   int    `json:"id"`
	Name string `json:"name"`
	URL  string `json:"url"`
}

type Category struct {
	ClassID          int    `json:"classId"`
	DateModified     string `json:"dateModified"`
	GameID           int    `json:"gameId"`
	IconURL          string `json:"iconUrl"`
	ID               int    `json:"id"`
	IsClass          bool   `json:"isClass"`
	Name             string `json:"name"`
	ParentCategoryID int    `json:"parentCategoryId"`
	Slug             string `json:"slug"`
	URL              string `json:"url"`
}

type LatestFiles struct {
	AlternateFileID      int                    `json:"alternateFileId"`
	Dependencies         []Dependencies         `json:"dependencies"`
	DisplayName          string                 `json:"displayName"`
	DownloadCount        int                    `json:"downloadCount"`
	DownloadURL          string                 `json:"downloadUrl"`
	FileDate             string                 `json:"fileDate"`
	FileFingerPrint      int                    `json:"fileFingerprint"`
	FileLength           int                    `json:"fileLength"`
	FileName             string                 `json:"fileName"`
	FileStatus           int                    `json:"fileStatus"`
	GameID               int                    `json:"gameId"`
	GameVersions         []string               `json:"gameVersions"`
	Hashes               []Hashes               `json:"hashes"`
	ID                   int                    `json:"id"`
	IsAvailable          bool                   `json:"isAvailable"`
	IsServerPack         bool                   `json:"isServerPack"`
	ModID                int                    `json:"modId"`
	Modules              []Modules              `json:"modules"`
	ReleaseType          int                    `json:"releaseType"`
	SortableGameVersions []SortableGameVersions `json:"sortableGameVersions"`
}

type Dependencies struct {
	ModId         int `json:"modId"`
	RealationType int `json:"relationType"`
}

type Hashes struct {
	Algo  int    `json:"algo"`
	Value string `json:"value"`
}

type Modules struct {
	FingerPrint int    `json:"value"`
	Name        string `json:"name"`
}

type SortableGameVersions struct {
	GameVersion            string `json:"gameVersion"`
	GameVersionName        string `json:"gameVersionName"`
	GameVersionPadded      string `json:"gameVersionPadded"`
	GameVersionReleaseDate string `json:"gameVersionReleaseDate"`
	GameVersionTypeID      int    `json:"gameVersionTypeId"`
}

type LatestFilesIndexes struct {
	FileID            int    `json:"fileId"`
	FileName          string `json:"filename"`
	GameVersion       string `json:"gameVersion"`
	GameVersionTypeId int    `json:"gameVersionTypeId"`
	ModLoader         int    `json:"modLoader"`
	ReleaseType       int    `json:"releaseType"`
}

type Links struct {
	IssuesURL  string `json:"issuesUrl"`
	SourceURL  string `json:"sourceUrl"`
	WebsiteURL string `json:"websiteUrl"`
	WikiURL    string `json:"wikiUrl"`
}

type Logo struct {
	Description  string `json:"description"`
	ID           int    `json:"id"`
	ModID        int    `json:"modId"`
	ThumbnailURL string `json:"thumbnailUrl"`
	Title        string `json:"title"`
	URL          string `json:"url"`
}

type ScreenShots struct {
	Description  string `json:"description"`
	ID           int    `json:"id"`
	ModID        int    `json:"modId"`
	ThumbnailURL string `json:"thumbnailUrl"`
	Title        string `json:"title"`
	URL          string `json:"url"`
}
