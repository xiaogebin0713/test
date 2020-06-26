package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

// WebServer
func WebServer() {
	r := gin.Default()
	r.LoadHTMLGlob("templates/*")
	r.GET("/", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "OK",
		})
	})
	r.GET("/index", func(c *gin.Context) {
		c.HTML(http.StatusOK, "index.html", gin.H{
			"title": "test",
		})
	})
	r.Run(":8888")
}

// main
func main() {
	// fmt.Println("test")
	// fmt.Println("test")
	WebServer()
}
