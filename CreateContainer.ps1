# Define container properties
$resourceGroupName = ""
$containerInstanceName = ""
$imageName = ""

# Define container registry credentials
$REGISTRY = ""
$USERNAME = ""
$TENANT_ID = ""
$PASSWORD = ""

# Define secure environment variables
$VM_NAME = ""
$RESOURCE_GROUP = ""
$ADMIN_ROLE_ID = 
$TENANT_ID = ""
$CLIENT_ID = ""
$SUBSCRIPTION_ID = ""
$CLIENT_SECRET = ""
$TOKEN = ""

# Login to Azure/ACR
az login --tenant $TENANT_ID
az acr login --name $REGISTRY

# Tag and push image to ACR
docker tag $containerInstanceName $imageName
docker push $imageName

# Create Container
az container create -g $resourceGroupName --name $containerInstanceName --image $imageName --ports 443 --registry-username $USERNAME --registry-password $PASSWORD --secure-environment-variables VM_NAME=$VM_NAME RESOURCE_GROUP=$RESOURCE_GROUP ADMIN_ROLE_ID=$ADMIN_ROLE_ID TENANT_ID=$TENANT_ID CLIENT_ID=$CLIENT_ID SUBSCRIPTION_ID=$SUBSCRIPTION_ID CLIENT_SECRET=$CLIENT_SECRET TOKEN=$TOKEN