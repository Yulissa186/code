import javax.swing.*;
import javax.swing.table.DefaultTableModel;

public class FibonacciSwing {
    public static void main(String[] args) {
        // Crear la ventana principal
        JFrame frame = new JFrame("Serie de Fibonacci");
        frame.setSize(600, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(null);

        // Crear una tabla para mostrar la serie de Fibonacci
        String[] columnas = {"Iteración", "Suma", "Resultado"};
        DefaultTableModel modelo = new DefaultTableModel(columnas, 0);
        JTable tabla = new JTable(modelo);
        
        
        JScrollPane scrollPane = new JScrollPane(tabla);
        scrollPane.setBounds(10, 10, 560, 300);
        frame.add(scrollPane);

        
        JButton generar = new JButton("Generar Serie");
        generar.setBounds(220, 320, 150, 30);
        frame.add(generar);

        
        generar.addActionListener(e -> {
            modelo.setRowCount(0); // Limpiar la tabla
            int n1 = 0, n2 = 1, n3;
            modelo.addRow(new Object[]{1, "0 + 1", 1});

            for (int i = 2; i <= 15; i++) {
                n3 = n1 + n2;
                modelo.addRow(new Object[]{i, n1 + " + " + n2, n3});
                n1 = n2;
                n2 = n3;
            }
        });

        frame.setVisible(true);
    }
}
