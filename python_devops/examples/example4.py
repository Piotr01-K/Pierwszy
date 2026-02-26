# AWS regioons 

import boto3


def list_ec2_regions():
    """
    Wyświetla wszystkie regiony AWS dla EC2.
    """

    print("🌍 Pobieram regiony AWS...")

    try:
        ec2 = boto3.client("ec2")
        response = ec2.describe_regions()

        print("\n✅ Dostępne regiony:\n")

        for region in response["Regions"]:
            name = region["RegionName"]
            endpoint = region["Endpoint"]
            print(f"• {name} → {endpoint}")

    except Exception as e:
        print(f"❌ Błąd: {e}")


if __name__ == "__main__":
    list_ec2_regions()