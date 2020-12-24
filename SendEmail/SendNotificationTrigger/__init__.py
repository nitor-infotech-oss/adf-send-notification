import logging
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import azure.functions as func
from datetime import datetime, timezone


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    req_body = req.get_json()
    print(req_body)

    try:
        JsonValue = req_body["Key"][""]
        #JsonValue = "Hello Test Mail"
        to_emails = req_body["to_email"]
        from_emails = req_body["from_email"]
        #print(JsonValue)
        today = datetime.now(timezone.utc)
        runDate = today.strftime("%m/%d/%Y %H:%M:%S") + ' GMT'
        instanceId = req_body["instanceId"]
        gcTenantId = req_body["gcTenantId"]
		Subject = req_body["subject"]
		SendClientKey = req_body["sendgridclient"]

        #Subject = 'Data Ingestion Summary :: InstanceID:' + instanceId + ' | TenantId:' + gcTenantId + ' | Date: ' + runDate
        #Subject = 'Data Ingestion Summary :: InstanceID:' + str(to_emails) + str(from_emails) + str(instanceId) + str(gcTenantId)

        message = Mail(
        from_email =from_emails,
        to_emails =to_emails,
        subject = Subject,
        html_content = JsonValue)

        sg = SendGridAPIClient(SendClientKey)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        raise Exception(str(e) + ' -> Error Reported')

    #return func.HttpResponse(f"Email sent successfully")
    return func.HttpResponse(f"{req_body}")
