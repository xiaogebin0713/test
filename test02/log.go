package main

import (
	"fmt"
	"os"
)

type Logger struct {
	FileName    string
	ErrFileName string
	FileObj     *os.File
	ErrFileObj  *os.File
	Level       LOGLEVEL
}

type LOGLEVEL uint16

const (
	UNKNOWN LOGLEVEL = iota
	INFO
	ERROR
	WARNING
)

// enable
func (l *Logger) enable(level LOGLEVEL) bool {
	return l.Level <= level
}

// log
func (l *Logger) log(level LOGLEVEL, msg string) {
	if l.enable(level) {
		// 写东西
		_, err := l.FileObj.WriteString(msg + "\n")
		if err != nil {
			fmt.Printf("write to file failed, error:%v", err)
			return
		}
		if level >= ERROR {
			_, err := l.ErrFileObj.WriteString(msg + "\n")
			if err != nil {
				fmt.Printf("write to file failed, error:%v", err)
				return
			}
		}
	}
}

// parseLevel
func (l *Logger) parseLevel(level string) LOGLEVEL {
	switch level {
	case "INFO":
		return INFO
	case "ERROR":
		return ERROR
	case "WARNING":
		return WARNING
	default:
		return UNKNOWN
	}
}

// lnfo
func (l *Logger) Info(msg string) {
	l.log(INFO, msg)
}

// Error
func (l *Logger) Error(msg string) {
	l.log(ERROR, msg)
}

// Init 初始化
func (l *Logger) Init() {
	fileObj, err := os.OpenFile(l.FileName, os.O_APPEND|os.O_CREATE|os.O_RDWR, 0644)
	if err != nil {
		fmt.Printf("open file failed, error:%v", err)
		return
	}

	errFileObj, err := os.OpenFile(l.ErrFileName, os.O_APPEND|os.O_CREATE|os.O_RDWR, 0644)
	if err != nil {
		fmt.Printf("open file failed, error:%v", err)
		return
	}
	l.FileObj = fileObj
	l.ErrFileObj = errFileObj
}

// NewLogger
func NewLogger(level string, fileName string) *Logger {
	l := Logger{
		FileName:    fileName,
		ErrFileName: "err_" + fileName,
	}
	Level := l.parseLevel(level)
	if Level == UNKNOWN {
		panic("parseLevel failed, error")
	}
	l.Level = Level
	l.Init()
	return &l
}
