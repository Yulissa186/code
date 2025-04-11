import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Piezas extends JFrame {
    private JPanel contentPane;
    private JTextField txtNumPiezas, txtPeso;
    private JTextArea txtResultado;
    private int piezasRestantes;
    private int entre18y52, masDe52;

    public Piezas() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setBounds(100, 100, 400, 300);
        contentPane = new JPanel();
        //contentPane.setBackground(new Color(0, 128, 255));//
        contentPane.setLayout(null);
        setContentPane(contentPane);

        JLabel lblNumPiezas = new JLabel("Número de piezas:");
        lblNumPiezas.setFont(new Font("Arial ", Font.PLAIN, 11));
        lblNumPiezas.setBounds(10, 20, 147, 25);
        contentPane.add(lblNumPiezas);

        txtNumPiezas = new JTextField();
        txtNumPiezas.setBounds(167, 21, 100, 25);
        contentPane.add(txtNumPiezas);

        JButton btnCapturar = new JButton("Aceptar");
        btnCapturar.setFont(new Font("Arial ", Font.PLAIN, 11));
        btnCapturar.setBounds(167, 93, 100, 25);
        contentPane.add(btnCapturar);

        JLabel lblPeso = new JLabel("Peso de la pieza (Kg):");
        lblPeso.setFont(new Font("Arial ", Font.PLAIN, 11));
        lblPeso.setBounds(10, 56, 147, 25);
        contentPane.add(lblPeso);

        txtPeso = new JTextField();
        txtPeso.setBounds(167, 57, 100, 25);
        contentPane.add(txtPeso);

        txtResultado = new JTextArea();
        txtResultado.setFont(new Font("Arial ", Font.PLAIN, 12));
        txtResultado.setBounds(10, 140, 360, 100);
        txtResultado.setEditable(false);
        contentPane.add(txtResultado);

        btnCapturar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                piezasRestantes = Integer.parseInt(txtNumPiezas.getText());
                entre18y52 = 0;
                masDe52 = 0;
                txtResultado.setText("El precio total es: ");
                txtPeso.setEnabled(true); // Habilitar campo para ingresar peso
                txtNumPiezas.setEnabled(false); // Deshabilitar campo de número de piezas
                btnCapturar.setEnabled(false); // Deshabilitar el botón
            }
        });

        txtPeso.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Capturar el peso de la pieza
                double peso = Double.parseDouble(txtPeso.getText());

                if (peso >= 1.8 && peso <= 5.2) {
                    entre18y52++;
                } else if (peso > 5.2) {
                    masDe52++;
                }

                piezasRestantes--;

                if (piezasRestantes > 0) {
                    txtPeso.setText(""); // Limpiar el campo de peso
                    txtPeso.requestFocus(); // Volver a enfocar en el campo de peso
                } else {
                    txtResultado.setText("Piezas entre 1.8 y 5.2 Kg: " + entre18y52 +
                            "\nPiezas mayores de 5.2 Kg: " + masDe52 +
                            "\nTotal de piezas procesadas: " + (entre18y52 + masDe52));
                    txtPeso.setEnabled(false); // Deshabilitar el campo de peso
                }
            }
        });
    }

    public static void main(String[] args) {
        Piezas frame = new Piezas();
        frame.setVisible(true);
    }
}