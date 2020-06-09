package main

import (
	"fmt"
	"io/ioutil"
)

// ShowFileContent 打印文件内容
func ShowFileContent(filename string) {
	content, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Printf("read file failed, error:%v", err)
		return
	}
	fmt.Println(string(content))
}
