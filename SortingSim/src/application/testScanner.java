package application;

import javafx.application.Application;

import java.io.IOException; 
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class testScanner {

	public static void main(String[] args) throws IOException {

		File file1 = new File("movieratings.txt");

		Scanner scanner = new Scanner(file1);

		int [] arr = new int[100]; 
		int h = arr.length -1;

		for (int i = 0; i < 100; i++) {                
			arr[i] = scanner.nextInt();
		}

		System.out.print(Arrays.toString(arr));



	}

}
