import javax.swing.*;

public class Promedio {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Calcular Promedio");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(null);

        JLabel label1 = new JLabel("Calificación 1:");
        label1.setBounds(10, 10, 100, 20);
        frame.add(label1);

        JTextField cal1 = new JTextField();
        cal1.setBounds(120, 10, 100, 20);
        frame.add(cal1);

        JLabel label2 = new JLabel("Calificación 2:");
        label2.setBounds(10, 40, 100, 20);
        frame.add(label2);

        JTextField cal2 = new JTextField();
        cal2.setBounds(120, 40, 100, 20);
        frame.add(cal2);

        JLabel label3 = new JLabel("Calificación 3:");
        label3.setBounds(10, 70, 100, 20);
        frame.add(label3);

        JTextField cal3 = new JTextField();
        cal3.setBounds(120, 70, 100, 20);
        frame.add(cal3);

        JButton calcular = new JButton("Calcular");
        calcular.setBounds(10, 100, 210, 30);
        frame.add(calcular);

        calcular.addActionListener(e -> {
            try {
                double c1 = Double.parseDouble(cal1.getText());
                double c2 = Double.parseDouble(cal2.getText());
                double c3 = Double.parseDouble(cal3.getText());

                double promedio = (c1 + c2 + c3) / 3;
                String mensaje;
                if (promedio >= 8) {
                    mensaje = "Excelente";
                } else if (promedio >= 6) {
                    mensaje = "Regular";
                } else {
                    mensaje = "Reprobado";
                }
                JOptionPane.showMessageDialog(frame, "Promedio: " + promedio + "\nEstado: " + mensaje);
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(frame, "Por favor, ingresa números válidos.");
            }
        });

        frame.setVisible(true);
    }
}
