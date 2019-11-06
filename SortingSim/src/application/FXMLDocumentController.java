package application;

import java.net.URL;
import java.util.Random; 
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.ResourceBundle;
import java.util.concurrent.TimeUnit;

import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Node;
import javafx.scene.chart.BarChart;
import javafx.scene.chart.CategoryAxis;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.XYChart;
import javafx.scene.chart.XYChart.Data;
import javafx.scene.control.ComboBox;
import javafx.util.Duration;

public class FXMLDocumentController implements Initializable {

    Timeline comparisonSortTimeline;
    Timeline mergeSortTimeline;
    Timeline quickSortTimeline;
    
    static int[] array = new int[20];
    int hodnota;
    int i;
    int sortingType = 0;
    int curr_size = 1;  
    int left_start = 0;
    int top = -1;
    int h = array.length -1;
    int l = 0;
    
    @FXML  
    private BarChart barChart; 
    
    @FXML 
    private ComboBox<String> sortingDropDown; 

    @FXML
    private void handleButtonAction(ActionEvent ev) 
    { 

    	Random rand = new Random();
    	for (int i = 0; i < 20; i++) {                
    		array[i] = rand.nextInt(1000); 
        }
    	
    	final CategoryAxis osaX = new CategoryAxis();          
        final NumberAxis osaY = new NumberAxis();
        ObservableList<XYChart.Series<String, Number>> barChartData = FXCollections.observableArrayList();
        final BarChart.Series<String, Number> series1 = new BarChart.Series<>();
        series1.getData().add(new XYChart.Data<>("1", array[0]));        
        series1.getData().add(new XYChart.Data<>("2", array[1]));
        series1.getData().add(new XYChart.Data<>("3", array[2]));
        series1.getData().add(new XYChart.Data<>("4", array[3]));
        series1.getData().add(new XYChart.Data<>("5", array[4]));
        series1.getData().add(new XYChart.Data<>("6", array[5]));
        series1.getData().add(new XYChart.Data<>("7", array[6]));
        series1.getData().add(new XYChart.Data<>("8", array[7]));
        series1.getData().add(new XYChart.Data<>("9", array[8]));
        series1.getData().add(new XYChart.Data<>("10", array[9]));
        series1.getData().add(new XYChart.Data<>("11", array[10]));        
        series1.getData().add(new XYChart.Data<>("12", array[11]));
        series1.getData().add(new XYChart.Data<>("13", array[12]));
        series1.getData().add(new XYChart.Data<>("14", array[13]));
        series1.getData().add(new XYChart.Data<>("15", array[14]));
        series1.getData().add(new XYChart.Data<>("16", array[15]));
        series1.getData().add(new XYChart.Data<>("17", array[16]));
        series1.getData().add(new XYChart.Data<>("18", array[17]));
        series1.getData().add(new XYChart.Data<>("19", array[18]));
        series1.getData().add(new XYChart.Data<>("20", array[19]));
        barChartData.add(series1);
        
        barChart.setData(barChartData);

        Node node = barChart.lookup(".data0.chart-bar");
        node.setStyle("-fx-bar-fill: red");       
        i = 0;
        int r = array.length-1;
        int n = array.length;
        
        
        comparisonSortTimeline = new Timeline(new KeyFrame(Duration.seconds(1), (event) -> 
        {
            System.out.println(i + ": " + Arrays.toString(array));         
            String selectedSort = sortingDropDown.getValue();
            switch(selectedSort)
            {
               case "Bubble" :
            	   array = SortingFunctions.BubbleSort(array, i);
                  break;              
               case "Insertion" :
            	   array = SortingFunctions.InsertionSort(array, i);
                  break;               
               default : 
            	   array = SortingFunctions.SelectionSort(array, i);                 
            }
           
            List<XYChart.Data<String, Number>> tempData = new ArrayList<Data<String, Number>>();
            for(int i = 0; i < array.length; i++)
            {
                tempData.add(new Data<String, Number>(Integer.toString(i), array[i]));
            }            
            barChartData.get(0).getData().setAll(tempData);

            i++;
        }));
        
       
        
        mergeSortTimeline = new Timeline(new KeyFrame(Duration.seconds(1), (event) -> 
        {             	            	              	              	                  
        	System.out.println(i + ": " + Arrays.toString(array));         

	        int mid = Math.min(left_start + curr_size - 1, n-1);             
	        int right_end = Math.min(left_start + 2*curr_size - 1, n-1); 
	        SortingFunctions.merge(array, left_start, mid, right_end); 
	        List<XYChart.Data<String, Number>> tempData = new ArrayList<Data<String, Number>>();
	        for(int i = 0; i < array.length; i++)
	        {
	              tempData.add(new Data<String, Number>(Integer.toString(i), array[i]));
	        }            
	        barChartData.get(0).getData().setAll(tempData);                    
	             
        	left_start += 2*curr_size;
        	
        	if (left_start >= n-1)
        	{
        		curr_size = 2*curr_size;
        		left_start = 0;
        	}
	                      
        	i++;
        }));
        
        
             
    	int[] stack = new int[h - l + 1];     
        stack[++top] = l;
        stack[++top] = h;          
        quickSortTimeline = new Timeline(new KeyFrame(Duration.seconds(1), (event) -> 
        {             	            	              	              	                  
        	System.out.println(i + ": " + Arrays.toString(array));          
	        h = stack[top--]; 
	        l = stack[top--]; 
	        
	        int p = SortingFunctions.partition(array, l, h); 
	        if (p - 1 > l) 
	        { 
	           stack[++top] = l; 
	           stack[++top] = p - 1; 
	        } 
	            
	        if (p + 1 < h) 
	        { 
	           stack[++top] = p + 1; 
	           stack[++top] = h; 
	        } 
	        
	       	        
	        List<XYChart.Data<String, Number>> tempData = new ArrayList<Data<String, Number>>();
	        for(int i = 0; i < array.length; i++)
	        {
	              tempData.add(new Data<String, Number>(Integer.toString(i), array[i]));
	        }            
	        barChartData.get(0).getData().setAll(tempData);                    	           
	                      
        	i++;
        }));
        
        quickSortTimeline.setCycleCount(30);
        mergeSortTimeline.setCycleCount(30);
        comparisonSortTimeline.setCycleCount(array.length);
    }    

    @FXML 
    private void bubbleButton(ActionEvent ev) 
    { 
    	
    	String selectedSort = sortingDropDown.getValue();
        switch(selectedSort)
        {
           case "Bubble" :
           case "Selection" :
           case "Insertion" :
        	   comparisonSortTimeline.play();
              break; 
           case "Merge" :
        	   mergeSortTimeline.play();
           case "Quick" :
        	   quickSortTimeline.play();
           default : 
        	   array = SortingFunctions.SelectionSort(array, i);                 
        }
    	
    }       

    @Override
    public void initialize(URL url, ResourceBundle rb) {
    	sortingDropDown.getItems().setAll("Bubble", "Insertion", "Merge", "Quick", "Selection");
    }
}