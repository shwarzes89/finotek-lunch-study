package Perceptron;

import java.util.ArrayList;

public class Learner {
	
	
	public static void main(String args[]){
		double alpha  =0.01;
		ArrayList<TrainingEntity> list = new ArrayList<TrainingEntity>();
	
		list.add(new TrainingEntity(29,56,1.0));
		list.add(new TrainingEntity(64,89,1.0));
		list.add(new TrainingEntity(33,17,-1.0));
		list.add(new TrainingEntity(45,94,1.0));
		list.add(new TrainingEntity(24,26,-1.0));
		list.add(new TrainingEntity(55,24,-1.0));
		list.add(new TrainingEntity(35,52,1.0));
		list.add(new TrainingEntity(57,65,1.0));
		list.add(new TrainingEntity(45,32,-1.0));
		list.add(new TrainingEntity(52,75,1.0));
		list.add(new TrainingEntity(62,31,-1.0));
		
		double w[] = {0.0,0.0,0.0};
		
		while(true){
			//System.out.println("--> "+w[0]+","+ w[1]);
			boolean isPass = true;
			for(TrainingEntity te:list){
				double di = getDi(w,te);
				if(di*te.y > 0 || di*te.y == 0){
					continue;
				}
				else{
					isPass = false;
					w[0] = w[0] + alpha*te.y*te.x1;
					w[1] = w[1] + alpha*te.y*te.x2;
					w[2] = w[2] + alpha*te.y*1;
					System.out.println("Adjusted");
				}
				//System.out.println(w[0]+","+ w[1]);
			}
			if(isPass)
				break;
			
		}
		
		System.out.println(w[0]+","+ w[1]+","+ w[2]);
		
		System.out.println(Validation.valid(list, w));
			
	}
	
	private static double getDi(double[] w, TrainingEntity e){
		double v = w[0]*e.x1 + w[1]*e.x2 + w[2]*1;
		if(v < 0)
			return -1.0;
		else
			return 1.0;
	}
	

}
