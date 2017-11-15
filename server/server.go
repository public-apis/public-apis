package main

import (
	"encoding/json"
	"io/ioutil"
	"strconv"
	"strings"

	"github.com/gin-gonic/gin"
)

type Request struct {
	Title       string `form:"title" json:"title"`
	Description string `form:"description" json:"description"`
	Auth        string `form:"auth" json:"auth"`
	HTTPS       string `form:"https" json:"https"`
	Category    string `form:"category" json:"category"`
}

type Entry struct {
	API         string `json:"API"`
	Description string `json:"Description"`
	Auth        string `json:"Auth"`
	HTTPS       bool   `json:"HTTPS"`
	Link        string `json:"Link"`
	Category    string `json:"Category"`
}

type ProjectData struct {
	Count   int     `json:"count"`
	Entries []Entry `json:"entries"`
}

func checkEntryMatches(entry Entry, request Request) bool {
	if strings.Contains(strings.ToLower(entry.API), strings.ToLower(request.Title)) &&
		strings.Contains(strings.ToLower(entry.Description), strings.ToLower(request.Description)) &&
		strings.Contains(strings.ToLower(entry.Auth), strings.ToLower(request.Auth)) &&
		strings.Contains(strings.ToLower(entry.Category), strings.ToLower(request.Category)) {
		if request.HTTPS == "" {
			return true
		} else {
			if value, err := strconv.ParseBool(request.HTTPS); err == nil {
				if entry.HTTPS == value {
					return true
				}
			}
		}
	}
	return false
}

func main() {
	r := gin.Default()

	r.GET("/api", func(c *gin.Context) {
		var req Request
		if c.Bind(&req) != nil {
			c.JSON(500, gin.H{
				"message": "server failed to parse request",
			})
			return
		}
		raw, err := ioutil.ReadFile("../json/entries.min.json")
		if err != nil {
			panic(err)
		}
		var data ProjectData
		json.Unmarshal(raw, &data)
		var resp []Entry
		for _, e := range data.Entries {
			if checkEntryMatches(e, req) {
				resp = append(resp, e)
			}
		}
		c.JSON(200, gin.H{
			"count": len(resp),
			"data":  resp,
		})
	})

	r.Run() // listen on port 8080
}
