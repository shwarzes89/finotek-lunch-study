package Perceptron;

import java.util.ArrayList;

public class Validation {
	
	public static boolean valid(ArrayList<TrainingEntity> list, double[] w){
		boolean result = false;
		
		for(TrainingEntity te : list){
			double h = te.x1 * w[0] + te.x2 * w[1] + w[2];
			if(h * te.y > 0)
				continue;
			else
				return false;
		}
		result = true;
		
		return result;
	}

}
