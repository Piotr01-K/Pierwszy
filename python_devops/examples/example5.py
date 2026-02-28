import boto3


def list_ec2_instances():
    """
    Wyświetla wszystkie instancje EC2.
    """

    print("📡 Łączenie z AWS EC2...")

    # połączenie z EC2
    ec2 = boto3.resource("ec2")

    print("📋 Lista instancji:\n")

    # iteracja po instancjach
    for instance in ec2.instances.all():
        print(f"🆔 ID: {instance.id}")
        print(f"⚙️ Typ: {instance.instance_type}")
        print(f"📊 Stan: {instance.state['Name']}")
        print(f"🌐 Public IP: {instance.public_ip_address}")
        print("-" * 40)


if __name__ == "__main__":
    list_ec2_instances()