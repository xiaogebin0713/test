package main

import (
	"fmt"
	"io/ioutil"
)

//func Test() {
//	fmt.Println("Test")
//}

// ShowContentFromFile
func ShowContentFromFile(fileName string) {

	content, err := ioutil.ReadFile(fileName)
	if err != nil {

		fmt.Printf("read file failed, error:%v", err)
		return
	}
	fmt.Println(string(content))
}
