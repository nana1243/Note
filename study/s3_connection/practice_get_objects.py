import boto3

client = boto3.client("s3")


def get_presigned_url(bucket_name: str, key: str):
    """
    Retrieves objects from Amazon S3. To use GET ,
     you must have READ access to the object.
    If you grant READ access to the anonymous user,
     you can return the object without using an authorization header.
    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.get_object
    """
    client = boto3.client()
    presigned_url = client.generate_presigned_url(
        "get_object", Params={"Bucket": bucket_name, "Key": key}
    )
    return presigned_url
