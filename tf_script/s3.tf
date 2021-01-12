resource "aws_s3_bucket" "bucket-test" {
  bucket = "my-test-bucket"
  acl    = "private"

  tags = {
    Name        = "My bucket"
    Environment = "Test"
  }
}