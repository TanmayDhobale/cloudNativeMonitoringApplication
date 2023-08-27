import boto3
ecr_client = boto3.client('ecr')

repository_name = "tanmay-repo"
reponse = ecr_client.create_repository(repositoryName=repository_name)

repository_Uri= reponse["repository"]['repositoryUri']
print(repository_Uri)

