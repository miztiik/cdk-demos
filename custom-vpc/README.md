# Use AWS Cloud Deployment Kit (CDK) to create your VPC

  We will use AWS CDK(Python) to create a custom VPC with as minimal coding as possible. Lets get started.

1. # Install CDK & Bootstrap CDK

    ```sh
    npm install -g aws-cdk
    # Check cdk version
    cdk --version

    # Boostrap CDK
    # Creates a CFn, S3 Bucket to host your templates etc
    cdk bootstrap
    ```

1. # Initialize new project

    Create a directory to hold our project files and set the language to `python`
  
    ```sh
    mkdir custom-vpc && cd custom-vpc
    cdk init --language python
    # Activate the virtual environment
    source .env/bin/activate
    # Install python modules in virtual env
    # The init command created the requirements.txt file. 
    # CDK is modular, so you will not get everything you need from the core part. 
    # Lets install ec2 package for building a vpc.
    echo "aws-cdk.aws_ec2" >> requirements.txt
    pip install -r requirements.txt
    ```

1. Create a custom VPC in CDK
  
    Lets create a sample VPC with 6 subnets spread across 2 AZ's along the required routing table, IGW etc

    ```sh
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
    ```
1. # Verify & Synthesize Template

    ```sh
    cdk synth
    # To Deploy
    cdk deploy
    ```

1. # Cleanup

    To remove all the resources created by CDK,

    ```sh
    cdk destroy
    ```
