import boto3
import os


def download_file(bucket_name, key, local_filename):
    s3 = boto3.client(
        "s3",
        region_name="insert_region",
        aws_access_key_id="insert_id",
        aws_secret_access_key="insert_secret",
    )
    s3.download_file(bucket_name, key, local_filename)


def upload_file(bucket_name, key, local_filename):
    s3 = boto3.client(
        "s3",
        region_name="insert_region",
        aws_access_key_id="insert_id",
        aws_secret_access_key="insert_secret",
    )
    s3.upload_file(local_filename, bucket_name, key)


def edit_file(local_filename):
    os.system(f'notepad "{local_filename}"')


def main():
    bucket_name = "insert_bucket_name"
    key = "insert_file_name.txt"
    local_filename = "temp_file.txt"

    # Download the file from S3.
    download_file(bucket_name, key, local_filename)

    # Allow the user to edit the file.
    edit_file(local_filename)

    # Upload the modified file back to S3.
    upload_file(bucket_name, key, local_filename)

    # Clean up the temporary file.
    os.remove(local_filename)

    print("File has been updated and uploaded to S3.")


if __name__ == "__main__":
    main()
