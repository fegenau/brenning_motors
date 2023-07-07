<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/Exception.php';
require 'PHPMailer/src/SMTP.php';

$destinatarios = array(
    'ma.laborie@yopmail.com',
    'fr.egenau@yopmail.com',
);

$nombre = $_POST['nombre'];
$email = $_POST['email'];
$mensaje = $_POST['mensaje'];
$tipo_motocicleta = $_POST['opcion1'];
$modelo_motocicleta = $_POST['opcion2'];

$asunto = 'Nuevo mensaje de contacto de Breninng Motors';
$contenido = "Nombre: $nombre\n";
$contenido .= "Email: $email\n";
$contenido .= "Mensaje: $mensaje\n";
$contenido .= "Tipo de motocicleta: $tipo_motocicleta\n";
$contenido .= "Modelo de motocicleta: $modelo_motocicleta\n";

$mail = new PHPMailer(true);

try {
    $mail->isSMTP();
    $mail->Host = 'smtp.office365.com';
    $mail->Port = 587;
    $mail->SMTPSecure = 'tls';
    $mail->SMTPAuth = true;
    $mail->Username = 'brenningmotors@outlook.com'; // Reemplaza con tu dirección de correo de Outlook
    $mail->Password = 'Brenning.Motors2023'; // Reemplaza con tu contraseña de Outlook

    $mail->setFrom($email, $nombre);
    foreach ($destinatarios as $destinatario) {
        $mail->addAddress($destinatario);
    }

    $mail->Subject = $asunto;
    $mail->Body = $contenido;

    $mail->send();
    header("Location: confirmacion.html"); // Redirige al usuario a una página de confirmación
    exit;
} catch (Exception $e) {
    echo 'Error al enviar el correo: ' . $mail->ErrorInfo;
}
