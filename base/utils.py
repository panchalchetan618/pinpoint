import hashlib
import boto3
from botocore.exceptions import ClientError
from decouple import config

region = config("AWS_REGION_NAME")
originationNumber = config("SENDER_NUMBER")
appId = config("PINPOINT_APP_ID")


def generate_ref_id(destinationNumber, brandName, source):
    refId = brandName + source + destinationNumber
    return hashlib.md5(refId.encode()).hexdigest()


def send_otp(destinationNumber):
    client = boto3.client("pinpoint", region_name=region)
    try:
        response = client.send_otp_message(
            ApplicationId=appId,
            SendOTPMessageRequestParameters={
                "Channel": "SMS",
                "BrandName": "SellerSetu",
                "CodeLength": 6,
                "ValidityPeriod": 10,
                "AllowedAttempts": 3,
                "Language": "en-US",
                "OriginationIdentity": originationNumber,
                "DestinationIdentity": destinationNumber,
                "ReferenceId": generate_ref_id(
                    destinationNumber, "SellerSetu", "Authentication"
                ),
            },
        )

        return response

    except ClientError as e:
        return str(e)


def verify_otp(destinationNumber, otp):
    client = boto3.client("pinpoint", region_name=region)
    try:
        response = client.verify_otp_message(
            ApplicationId=appId,
            VerifyOTPMessageRequestParameters={
                "DestinationIdentity": destinationNumber,
                "ReferenceId": generate_ref_id(
                    destinationNumber, "SellerSetu", "Authentication"
                ),
                "Otp": otp,
            },
        )
        
        return response

    except ClientError as e:
        return str(e)
