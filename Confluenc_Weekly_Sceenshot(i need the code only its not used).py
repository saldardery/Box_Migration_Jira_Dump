# Create a new SMTP client object
$smtp = New-Object System.Net.Mail.SmtpClient

# Set the SMTP server address, port, and credentials
$smtp.Host = "smtp.vmware.com"
$smtp.Port = 25
$smtp.Credentials = New-Object System.Net.NetworkCredential("svc.bot.svc_wwcc_ga", "wGJLjMe-_hcNSZm61zY")
$date= Get-Date -Format “dd/MM/yyyy”
# Create a new mail message object
$mail = New-Object System.Net.Mail.MailMessage
$att = New-Object System.Net.Mail.Attachment “C:\Users\powerbi\Desktop\Confluence\screenshot.png”
# Set the sender, recipient, subject, and body of the message
$mail.From = "automation@wwccga.com"
$mail.To.Add("saldardery@vmware.com")
$mail.To.Add("fahda@vmware.com")  
$mail.Subject = "Confluence Weekly Screenshot"
$mail.Body ="This is a screenshot of Great Atlantic's confluence page as of date $date"
$mail.Attachments.Add($att)
# Send the message using the SMTP client
$smtp.Send($mail)
