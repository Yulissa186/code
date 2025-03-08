package basedatos01;

import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;

public class Formulario extends JFrame {
    private static final long serialVersionUID = 1L;
    private final JLabel lblDescripcinDelArticulo;
    private JTextField tf3;  // Campo para ingresar código
    private JTextField tf1;  // Campo para descripción del artículo
    private final JLabel lblIngreseCdigoDe;
    private JTextField tf2;  // Campo para precio
    private final JButton btnConsultaporCdigo;
    private JLabel labelResultado_1;  // Etiqueta para mostrar el resultado de la operación

    // Método principal que lanza la aplicación
    public static void main(String[] args) {
        EventQueue.invokeLater(() -> {
            try {
                Formulario frame = new Formulario();
                frame.setVisible(true);
            } catch (Exception e) {
            }
        });
    }

    // Constructor del formulario
    @SuppressWarnings("ConvertToTryWithResources")
    public Formulario() {
        // Configuración de la ventana
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setBounds(100, 100, 613, 492);
        JPanel contentPane = new JPanel();
        contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
        setContentPane(contentPane);
        contentPane.setLayout(null);

        // Etiqueta para la descripción del artículo
        lblDescripcinDelArticulo = new JLabel("Descripcion del Articulo");
        lblDescripcinDelArticulo.setBounds(58, 55, 141, 14);
        contentPane.add(lblDescripcinDelArticulo);

        // Campo de texto para la descripción
        tf1 = new JTextField();
        tf1.setBounds(290, 52, 187, 20);
        contentPane.add(tf1);
        tf1.setColumns(10);

        // Etiqueta para el precio
        JLabel lblPrecio = new JLabel("precio");
        lblPrecio.setBounds(107, 113, 49, 14);
        contentPane.add(lblPrecio);

        // Campo de texto para el precio
        tf2 = new JTextField();
        tf2.setBounds(290, 107, 96, 20);
        contentPane.add(tf2);
        tf2.setColumns(10);

        // Botón "ALTA" para registrar un artículo
        JButton btnAlta = new JButton("ALTA");
        btnAlta.addActionListener((ActionEvent e) -> {
            labelResultado_1.setText("");  // Limpiar el resultado anterior
            try {
                try ( // Conexión a la base de datos
                        Connection conexion = DriverManager.getConnection("jdbc:mysql://localhost:3306/base1", "root", "")) {
                    String query = "INSERT INTO articulos(descripcion, precio) VALUES (?, ?)";  // Consulta SQL
                    PreparedStatement comando = conexion.prepareStatement(query);
                    comando.setString(1, tf1.getText());  // Asignar el valor de la descripción
                    comando.setDouble(2, Double.parseDouble(tf2.getText()));  // Asignar el valor del precio
                    comando.executeUpdate(); // Ejecutar la consulta
                    // Cerrar la conexión
                } // Consulta SQL
                labelResultado_1.setText("Se registraron los datos");
                tf1.setText("");  // Limpiar los campos de texto
                tf2.setText("");
            } catch (SQLException ex) {
                labelResultado_1.setText("Error: " + ex.getMessage());  // Mostrar el error si ocurre
            }
        });
        btnAlta.setBounds(213, 178, 89, 23);
        contentPane.add(btnAlta);

        // Etiqueta para mostrar los resultados
        labelResultado_1 = new JLabel("Resultado");
        labelResultado_1.setBounds(342, 182, 141, 14);
        contentPane.add(labelResultado_1);

        // Etiqueta para el campo de búsqueda por código
        lblIngreseCdigoDe = new JLabel("Ingrese el codigo de Articulo A consultar");
        lblIngreseCdigoDe.setBounds(58, 250, 277, 14);
        contentPane.add(lblIngreseCdigoDe);

        // Campo de texto para ingresar el código de artículo
        tf3 = new JTextField();
        tf3.setBounds(290, 247, 96, 20);
        contentPane.add(tf3);
        tf3.setColumns(10);

        // Botón para consultar por código
        btnConsultaporCdigo = new JButton("consultar por codigo");
        btnConsultaporCdigo.addActionListener((ActionEvent e) -> {
            labelResultado_1.setText("");  // Limpiar el resultado anterior
            tf1.setText("");  // Limpiar los campos de texto
            tf2.setText("");
            try {
                // Conexión a la base de datos
                Connection conexion = DriverManager.getConnection("jdbc:mysql://localhost:3306/base1", "root", "");
                String query = "SELECT * FROM articulos WHERE codigo=?";  // Consulta SQL para buscar el artículo por código
                PreparedStatement comando = conexion.prepareStatement(query);
                comando.setInt(1, Integer.parseInt(tf3.getText()));  // Asignar el valor del código
                ResultSet registro = comando.executeQuery();  // Ejecutar la consulta
                if (registro.next()) {
                    tf1.setText(registro.getString("descripcion"));  // Mostrar la descripción
                    tf2.setText(registro.getString("precio"));  // Mostrar el precio
                } else {
                    labelResultado_1.setText("No Existe Articulo");  // Si no se encuentra, mostrar mensaje
                }
                conexion.close();  // Cerrar la conexión
            } catch (SQLException ex) {
                labelResultado_1.setText("Error: " + ex.getMessage());  // Mostrar error si ocurre
            }
        });
        btnConsultaporCdigo.setBounds(146, 309, 171, 23);
        contentPane.add(btnConsultaporCdigo);
    }
}
