package main

import (
	"sync"
)

var wg sync.WaitGroup

func main() {
	wg.Add(1)
	go func() {
		defer wg.Done()
		WebServer()
	}()
	wg.Wait()
}
