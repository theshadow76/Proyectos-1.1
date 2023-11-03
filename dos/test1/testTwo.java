import javax.swing.JPanel;
import javax.swing.JWindow;
import javax.swing.*;

public class testTwo {
    public static void main(String[] args){ //muy tonto
        JFrame frame = new JFrame("This is really good ui!");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300,300);
        
        JButton btn_one = new JButton("Press me");
        btn_one.setSize(1,3);
        btn_one.contains(12, 30);
        frame.getContentPane().add(btn_one);

        frame.setVisible(true);
    }
    public void v1(){
        System.out.println("hola");
    }
}
