output "instance_id" {
    description = "The EC2 server we need to connect to"
    value = var.instance_id
}

output "sns_topic_name" {
    description = "Messaging for when we need an alert"
    value = aws_sns_topic.web_alerts.arn
}