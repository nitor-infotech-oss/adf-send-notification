# adf-send-notification
<h3>Using this code, we can send email notification from data factory using sendgrid email SMTP relay and azure function</h3>
<b>Please follow below steps to send email notification from data factory</b> <br/>
<ol>
<li> Create send grid account and register sender email </li>
<li> Use the comitted code to create azure function in python langauge </li>
<li> deploy the azure function to azure portal </li>
<li> Create data factory and add web activity to trigger the azure function </li>
<li> Use the deployed function URL and configure it in Data Factory web activity. </li>
<li> Parameters can be passed to azure function from web activity using post or get method. </li>
</ol>
