FROM cloudposse/terraform-root-modules:0.5.2 as terraform-root-modules

FROM nikiai/geodesic:latest
ENV BANNER="root" \
    DOCKER_IMAGE="nikiai/root.niki.ai" \
    DOCKER_TAG="latest" \
#############
# AWS Region
#############
    AWS_REGION="ap-south-1" \
    AWS_DEFAULT_REGION="ap-south-1" \
#############
# AWS Profile
##############
    AWS_DEFAULT_PROFILE="root-admin" \
    TF_VAR_aws_assume_role_arn='arn:aws:iam::639127283868:role/root-admin' \
# Terraform State Bucket
    TF_BUCKET="niki-root-terraform-state" \
    TF_BUCKET_REGION="ap-south-1" \
    TF_DYNAMODB_TABLE="niki-root-terraform-state-lock" \
    AWS_ROLE_ARN='arn:aws:iam::639127283868:role/root-admin' \
# Terraform vars
    TF_VAR_account_id="639127283868" \
    TF_VAR_region="ap-south-1" \
    TF_VAR_namespace="niki" \
    TF_VAR_stage="root" \
    TF_VAR_parent_domain_name="niki.ai" \
    TF_VAR_root_domain_name="root.niki.ai" \
# PROD ACCOUNT
    TF_VAR_prod_account_name="niki-prod" \
    TF_VAR_prod_account_id="158181842387" \
    TF_VAR_prod_account_email="aws.prod@niki.ai" \
    TF_VAR_prod_name_servers='["ns-1588.awsdns-06.co.uk.", "ns-1421.awsdns-49.org", "ns-593.awsdns-10.net", "ns-129.awsdns-16.com"]' \
# SDKPROD ACCOUNT
    TF_VAR_sdkprod_account_name="niki-sdkprod" \
    TF_VAR_sdkprod_account_id="890392325335" \
    TF_VAR_sdkprod_account_email="keshav@niki.ai" \
    TF_VAR_sdkprod_name_servers='["ns-1588.awsdns-06.co.uk.", "ns-1421.awsdns-49.org", "ns-593.awsdns-10.net", "ns-129.awsdns-16.com"]' \
#STAGE
    TF_VAR_staging_account_name="niki-stage" \
    TF_VAR_staging_account_id="240764613923" \
    TF_VAR_staging_account_email="awsstage@niki.ai" \
    TF_VAR_staging_name_servers='["ns-1588.awsdns-06.co.uk.", "ns-1421.awsdns-49.org", "ns-593.awsdns-10.net", "ns-129.awsdns-16.com"]' \
#AUDIT
    TF_VAR_audit_account_name="niki-audit" \
    TF_VAR_audit_account_email="rohit.verma@niki.ai" \
    TF_VAR_audit_account_id="614927918057" \
    TF_VAR_audit_name_servers='["ns-1588.awsdns-06.co.uk.", "ns-1421.awsdns-49.org", "ns-593.awsdns-10.net", "ns-129.awsdns-16.com"]' \
# DEV
    TF_VAR_dev_account_name="niki-dev" \
    TF_VAR_dev_account_id="517923651487" \
    TF_VAR_dev_account_email="awsdev@niki.ai" \
    TF_VAR_dev_name_servers='["ns-1588.awsdns-06.co.uk.", "ns-1421.awsdns-49.org", "ns-593.awsdns-10.net", "ns-129.awsdns-16.com"]' \
# Cloudtrail
    TF_VAR_s3_bucket_name=""
# Copy root modules
COPY --from=terraform-root-modules /aws/tfstate-backend/ /conf/tfstate-backend/
COPY --from=terraform-root-modules /aws/organization/ /conf/organization/
COPY --from=terraform-root-modules /aws/cloudtrail/ /conf/cloudtrail/

COPY /aws/ /conf/


# Filesystem entry for tfstate
RUN s3 fstab '${TF_BUCKET}' '/' '/secrets/tf'

WORKDIR /conf/
