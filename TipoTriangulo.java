import javax.swing.*;

public class TipoTriangulo {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Tipo de Triángulo");
        frame.setSize(300, 250);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(null);

        JLabel label1 = new JLabel("Lado 1:");
        label1.setBounds(10, 10, 100, 20);
        frame.add(label1);

        JTextField lado1 = new JTextField();
        lado1.setBounds(120, 10, 100, 20);
        frame.add(lado1);

        JLabel label2 = new JLabel("Lado 2:");
        label2.setBounds(10, 40, 100, 20);
        frame.add(label2);

        JTextField lado2 = new JTextField();
        lado2.setBounds(120, 40, 100, 20);
        frame.add(lado2);

        JLabel label3 = new JLabel("Lado 3:");
        label3.setBounds(10, 70, 100, 20);
        frame.add(label3);

        JTextField lado3 = new JTextField();
        lado3.setBounds(120, 70, 100, 20);
        frame.add(lado3);

        JButton determinar = new JButton("Determinar");
        determinar.setBounds(10, 110, 210, 30);
        frame.add(determinar);

        determinar.addActionListener(e -> {
            try {
                double l1 = Double.parseDouble(lado1.getText());
                double l2 = Double.parseDouble(lado2.getText());
                double l3 = Double.parseDouble(lado3.getText());

                String tipo;
                if (l1 == l2 && l2 == l3) {
                    tipo = "Equilátero";
                } else if (l1 == l2 || l1 == l3 || l2 == l3) {
                    tipo = "Isósceles";
                } else {
                    tipo = "Escaleno";
                }
                JOptionPane.showMessageDialog(frame, "El triángulo es: " + tipo);
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(frame, "Por favor, ingresa valores numéricos válidos.");
            }
        });

        frame.setVisible(true);
    }
}
