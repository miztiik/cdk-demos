from aws_cdk import (
    aws_ec2 as ec2,
    core
)


class CustomVpcStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
         # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_ec2/Vpc.html
        vpc = ec2.Vpc(
                self, "MyVpc",
                cidr="10.13.0.0/21",
                max_azs=2,
                nat_gateways=0,
                subnet_configuration=[
                    ec2.SubnetConfiguration(name="public", cidr_mask=24, subnet_type=ec2.SubnetType.PUBLIC),
                    # ec2.SubnetConfiguration(name="private", cidr_mask=24, subnet_type=ec2.SubnetType.PRIVATE)
                    ec2.SubnetConfiguration(name="private", cidr_mask=24, subnet_type=ec2.SubnetType.ISOLATED)
                ]
            )
        
        # Tag all VPC Resources
        core.Tag.add(vpc,key="Owner",value="KonStone",include_resource_types=[])
