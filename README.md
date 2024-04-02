# s3-file-editor
Python script that allows you to download a file from an Amazon S3 bucket, edit it using a local text editor on Windows, and upload the modified file back to the S3 bucket.

Requirements:
    Python 3, Boto3 library (AWS SDK for Python). AWS user with necessary permissions, its credentials (keys) and an S3 bucket created in a specific region.

AWS credentials:
Ensure that you have AWS credentials configured on your system. You can set them up using AWS CLI or by providing them directly in the script.

Modify the script:
Update the bucket_name, key, and local_filename variables in the main() function with your specific S3 bucket details and file information.

Run the script:
Follow the prompts to edit the file locally. Once you're done, save it. The modified file will be automatically uploaded back to the S3 bucket.

Notes:
Ensure that the IAM user associated with the AWS credentials has the necessary permissions to access the specified S3 bucket and perform read/write operations on the objects.
Specify the region where the S3 bucket is.
Make sure to handle sensitive information such as AWS access keys securely.
This script is intended for educational purposes and can be modified to suit specific requirements.

To know more about this script, please visit: https://serpentinebyte.blogspot.com/2024/03/boto3-integrating-python-apps-with-aws.html

Feel free to enhance and contribute to this repository! If you encounter any issues or have suggestions for improvements, please send an email to gianluca.balla.contact@gmail.com.
