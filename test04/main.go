package main

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

// WebServer
func WebServer() {
	r := gin.Default()
	r.GET("/", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "OK",
		})
	})
	r.Run(":8888")
}

// main
func main() {
	fmt.Println("test")
	fmt.Println("test")
}
