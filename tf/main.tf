provider "aws" {
  access_key = var.access_key
  secret_key = var.secret_key
  version = "~> 2.0"
  region = var.region
}

resource "aws_vpc" "main" {
  cidr_block = "172.31.0.0/16"
  enable_dns_support = true
  enable_dns_hostnames = true

}
resource "aws_subnet" "main" {
  vpc_id = aws_vpc.main.id
  cidr_block = "172.31.32.0/20"
  map_public_ip_on_launch = true
  availability_zone = "us-west-2a"
  tags = {
    Name = var.user_name
  }
}

resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.main.id
  tags = {
    Name = var.user_name
  }
}


resource "aws_route_table" "r" {
  vpc_id = aws_vpc.main.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }
}

resource "aws_network_acl" "main" {
  vpc_id = aws_vpc.main.id
  subnet_ids = [aws_subnet.main.id]
  egress{
    protocol = "all"
    rule_no = 100
    action = "allow"
    cidr_block = "0.0.0.0/0"
    from_port = 0
    to_port = 0
  }

  ingress {
    protocol = "all"
    rule_no = 1
    action = "allow"
    cidr_block = "0.0.0.0/0"
    from_port = 0
    to_port = 0
  }

  tags = {
    Name = var.user_name
  }
}

resource "aws_route_table_association" "a" {
  subnet_id = aws_subnet.main.id
  route_table_id = aws_route_table.r.id
}

resource "aws_security_group" "allow_internet_access" {
  name = "allow_internet_access"
  description = "Allow outbound internet communication."
  vpc_id = aws_vpc.main.id

  tags = {
    Name = var.user_name
  }

  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "allow_all_ssh_access" {
  name = "allow_all_ssh_access"
  description = "ALlow ssh access from any ip"
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "var.user_name"
  }

  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
