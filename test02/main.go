package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

// webServer
func webServer() {
	r := gin.Default()
	v2 := r.Group("v2")
	v2.GET("/home", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "Home",
		})
	})

	// /login
	v2.POST("/login", func(c *gin.Context) {
		username := c.PostForm("username")
		password := c.PostForm("password")
		if username == "xiaogebin" && password == "123456" {
			c.JSON(http.StatusOK, gin.H{
				"message": "登录成功",
			})
		}
		c.JSON(http.StatusUnauthorized, gin.H{
			"message": "参数错误",
		})
	})

	// /home
	v2.POST("/home", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "OK",
		})
	})

	// /list
	v2.POST("list", func(c *gin.Context) {
		c.String(http.StatusOK, "list")
	})

	// /logout
	v2.POST("/logout", func(c *gin.Context) {
		// login
		c.String(http.StatusOK, "logout")
	})

	// 监听8888端口
	r.Run(":8888")
}

func main() {
	l := NewLogger("INFO", "test.log")
	l.Info("TEST")
	l.Error("ERROR TEST")
}
