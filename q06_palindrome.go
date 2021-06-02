package main

import "fmt"

func palindrome(s string) bool {
	for i := 0; i < len(s); i++ {
		if s[i] != s[len(s)-1-i] {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(palindrome("racecar"))
	fmt.Println(palindrome("saas"))
	fmt.Println(palindrome("arthur c fitzgerald"))
}
