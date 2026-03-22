variable "instance_id" {
    description = "EC2 ID. What we need to restart when things get slow"
    type = string
    default = "i-12345"
}

variable "sns_topic_name" {
    description = "Name for SNS topic"
    type = string
    default = "web-alerts"
}

variable "region" {
    description = "Region we are deploying to. Going with us-east-1"
    type = string
    default = "us-east-1"
}