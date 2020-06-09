package main

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

// WebServer web服务
func WebServer() {
	g := gin.Default()
	fmt.Println("Webserver starting")
	g.GET("/", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "这是首页",
		})
	})

	g.POST("/post", func(c *gin.Context) {
		message := c.PostForm("message")
		c.JSON(http.StatusOK, gin.H{
			"Message": message,
		})
	})

	//
	// 启动服务
	g.Run("0.0.0.0:8080")
}
