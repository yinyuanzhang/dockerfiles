FROM cloudposse/terraform-root-modules:0.5.2 as terraform-root-modules

FROM nikiai/geodesic:latest

ENV BANNER="dev" \
    DOCKER_IMAGE="nikiai/dev.niki.ai" \
    DOCKER_TAG="latest" \
# Account
    TF_VAR_zone_id="Z3O7B88IGYG0CN" \
    TF_VAR_account_id="517923651487" \
    TF_VAR_domain_name="dev.niki.ai" \
# Terraform vars \
    TF_VAR_region="${AWS_REGION}" \
    TF_VAR_namespace="niki" \
    TF_VAR_stage="dev" \
    TF_VAR_zone_name="${TF_VAR_domain_name}" \
# Default AWS region \
    AWS_REGION="us-west-2" \
    AWS_DEFAULT_REGION="${AWS_REGION}" \
# Default AWS Profile name \
    AWS_DEFAULT_PROFILE="dev-admin" \
    TF_VAR_aws_assume_role_arn="arn:aws:iam::${TF_VAR_account_id}:role/dev-admin" \
# Terraform State Bucket \
    TF_BUCKET="niki-dev-terraform-state" \
    TF_BUCKET_REGION="${AWS_REGION}" \
    TF_DYNAMODB_TABLE="niki-dev-terraform-state-lock" \
    AWS_ROLE_ARN="arn:aws:iam::${TF_VAR_account_id}:role/${AWS_ROLE_ARN}" \
# chamber KMS config
    CHAMBER_KMS_KEY_ALIAS="alias/${TF_VAR_namespace}-${TF_VAR_stage}-chamber" \
# kops config
    KOPS_BASE_IMAGE="aws-marketplace/CoreOS-stable-1800.5.0-hvm-0d1e0bd0-eaea-4397-9a3a-c56f861d2a14-ami-ab6963d4.4" \
    KOPS_CLUSTER_NAME="${TF_VAR_domain_name}" \
    KOPS_DNS_ZONE=${TF_VAR_zone_name} \
    KOPS_STATE_STORE="s3://${TF_VAR_namespace}-${TF_VAR_stage}-kops-state"
    KOPS_STATE_STORE_REGION="us-west-2" \
    KOPS_AVAILABILITY_ZONES="us-west-2a,us-west-2b,us-west-2c" \
    KOPS_PRIVATE_SUBNETS="10.0.1.0/24,10.0.2.0/24,10.0.3.0/24" \
    KOPS_UTILITY_SUBNETS="10.0.11.0/24" \
    KOPS_BASTION_PUBLIC_NAME="bastion" \
    BASTION_MACHINE_TYPE="t2.medium" \
    MASTER_MACHINE_TYPE="t2.medium" \
    NODE_MACHINE_TYPE="t2.medium" \
    NODE_MAX_SIZE="10" \
    NODE_MIN_SIZE="2" \
# kube config
    KUBECONFIG="/conf/kops-aws-platform/kubeconfig_niki-dev-cluster" \
# backend-services
    TF_VAR_MYSQL_ADMIN_NAME="root" \
    TF_VAR_MYSQL_ADMIN_PASSWORD="testtest12" \
    TF_VAR_MYSQL_DB_NAME="commerce" \
    TF_VAR_key_name="Oregon"

VOLUME "/conf"

# Copy root modules
COPY --from=terraform-root-modules /aws/tfstate-backend/ /conf/tfstate-backend/
COPY --from=terraform-root-modules /aws/account-dns/ /conf/account-dns/
COPY --from=terraform-root-modules /aws/acm/ /conf/acm/
COPY --from=terraform-root-modules /aws/chamber/ /conf/chamber/
COPY --from=terraform-root-modules /aws/cloudtrail/ /conf/cloudtrail/

COPY /aws/iam/ /conf/iam/
COPY /aws/kops/ /conf/kops/
COPY /aws/backing-services/ /conf/backing-services/
COPY /aws/kops-aws-platform/ /conf/kops-aws-platform/
COPY /aws/services/ /conf/services/

# Filesystem entry for tfstate
RUN s3 fstab "${TF_BUCKET}" "/" "/secrets/tf"

WORKDIR /conf/
