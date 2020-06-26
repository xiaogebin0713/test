package main

import (
	"fmt"
	"io/ioutil"
)


// ShowContentFromFile 显示文件内容
func ShowContentFromFile(fileName string) {
	content, err := ioutil.ReadFile(fileName)
	if err != nil {
		fmt.Printf("read file failed, error:%v", err)
		return
	}
	fmt.Println(string(content))
}
