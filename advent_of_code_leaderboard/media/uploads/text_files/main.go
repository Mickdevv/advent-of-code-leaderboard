package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	// file, err := os.Open("input.txt")
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(file)
	safe_reports := 0

	for scanner.Scan() {
		line:=strings.Split(scanner.Text(), " ")
		fmt.Println(line)

		//Descending
		safe := true
		if string_to_int(line[0]) > string_to_int(line[1]) {
			for i := 0; i < len(line)-1; i++ {
				if string_to_int(line[i]) - string_to_int(line[i+1]) > 3 || string_to_int(line[i]) - string_to_int(line[i+1]) < 1 {
					safe = false
					fmt.Println(string_to_int(line[i]), string_to_int(line[i+1]), "increasing")
					break
				}
			}

		//Ascending
		} else {
			for i := 0; i < len(line)-1; i++ {
				if string_to_int(line[i+1]) - string_to_int(line[i]) > 3 || string_to_int(line[i+1]) - string_to_int(line[i]) < 1 {
					fmt.Println(string_to_int(line[i]), string_to_int(line[i+1]), "decreasing")
					safe = false
					break
				}
			}
		}
		if safe == true {
			
			safe_reports++
		}

	}
	fmt.Println(safe_reports)
}

func string_to_int(str string) float64 {
	i, err := strconv.Atoi(str)
	if err != nil {
		log.Fatal(err)
	}
	return float64(i)
}