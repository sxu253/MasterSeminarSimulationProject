package application;

import java.net.URL;
import java.util.Random; 
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.ResourceBundle;
import java.util.concurrent.TimeUnit;
import java.util.stream.IntStream;

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
    
    static int[] array = null;
    int hodnota;
    int i;
    int sortingType = 0;
    int curr_size = 1;  
    int left_start = 0;
    int top = -1;
    int h = 0;
    int l = 0;
    
    @FXML  
    private BarChart barChart; 
    
    @FXML 
    private ComboBox<String> sortingDropDown; 

    @FXML
    private void handleButtonAction(ActionEvent ev) 
    { 
    	array = new int[100]; 
    	h = array.length -1;
    	Random rand = new Random();
    	final CategoryAxis osaX = new CategoryAxis();          
        final NumberAxis osaY = new NumberAxis();
        ObservableList<XYChart.Series<String, Number>> barChartData = FXCollections.observableArrayList();
        final BarChart.Series<String, Number> series1 = new BarChart.Series<>();
            
        for (int i = 0; i < 100; i++) {                
    		array[i] = rand.nextInt(1000); 
    		series1.getData().add(new XYChart.Data<>(Integer.toString(i), array[i]));
        }
        barChartData.add(series1);       
        barChart.setData(barChartData);

//        Node node = barChart.lookup(".data0.chart-bar");
//        node.setStyle("-fx-bar-fill: red");       
        i = 0;
        int r = array.length-1;
        int n = array.length;
        
        
        comparisonSortTimeline = new Timeline(new KeyFrame(Duration.seconds(.25), (event) -> 
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
        
       
        
        mergeSortTimeline = new Timeline(new KeyFrame(Duration.seconds(.25), (event) -> 
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
        	
        	if (this.isSorted(array))
        	{
        		mergeSortTimeline.stop();
        	}
        }));
        
        
        int[] stack = new int[h - l + 1]; 
        top = -1; 
        stack[++top] = l; 
        stack[++top] = h;         
        quickSortTimeline = new Timeline(new KeyFrame(Duration.seconds(.25), (event) -> 
        {             	            	              	              	                  
        	System.out.println(i + ": " + Arrays.toString(array));  
        	if (top >= 0)
        	{
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
        	}
        	
        	if (this.isSorted(array))
        	{
        		quickSortTimeline.stop();
        	}
        }));
        
        quickSortTimeline.setCycleCount(Timeline.INDEFINITE);
        mergeSortTimeline.setCycleCount(Timeline.INDEFINITE);
        comparisonSortTimeline.setCycleCount(array.length);
    }    

    @FXML 
    private void bubbleButton(ActionEvent ev) 
    {  	
    	try 
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
    	catch (Exception e) {} 	       	
    }    
    
    public boolean isSorted(int[] array)
    {
    	return IntStream.range(0, array.length - 1).noneMatch(i -> array[i] > array[i + 1]);
    }

    @Override
    public void initialize(URL url, ResourceBundle rb) {
    	sortingDropDown.getItems().setAll("Bubble", "Insertion", "Merge", "Quick", "Selection");
    }
}