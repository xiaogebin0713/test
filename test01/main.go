package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

type Struct1 struct {
	Name string
	ID   int
}

func main() {
	// wg.Add(1)
	// go func() {
	// 	defer wg.Done()
	// 	WebServer()
	// }()
	// wg.Wait()
	fmt.Println("test")
	var t *Struct1
	t = &Struct1{
		"xiaogebin",
		1,
	}
	fmt.Println(t.Name)
	fmt.Println(t.ID)

}
