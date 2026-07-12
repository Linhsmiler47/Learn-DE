# Phase 24 — Azure Data Engineering

## Learning Objectives

- Map local Data Engineering concepts to Azure-managed equivalents.
- Understand Azure resource groups, identity, storage, and the core DE-relevant services.

## Prerequisites

- Phase 23 — Deployment
- Phase 19 — Modern Lakehouse (to compare against Azure equivalents)

## Reference Materials (`ref roadmap/`, read-only)

- [Azure App Registration used for OneDrive API auth (conceptual only — not an Azure DE service)](../../ref%20roadmap/My%20mentor/BUỔI%202/BÀI%20GIẢNG/TALEND/ETL%20ONEDRIVE%20TO%20DWH/LESSON%202%20-%20AZURE%20-%20MAIN%20-%20Hướng%20dẫn%20đăng%20ký%20Azure%20App%20và%20Authen.docx)

> This is the only Azure-related material in `ref roadmap/`, and it's about API auth for a Talend connector, not Azure's actual data services — treat this phase as fully new content.

## Core Concepts

- Azure architecture fundamentals, resource groups, identity and access (Entra ID)
- Storage accounts, Azure Data Lake Storage
- Azure SQL, Azure Database for PostgreSQL
- Azure Data Factory, Azure Functions, Azure Container Apps, Azure Container Registry
- Azure Key Vault, Azure Monitor, Microsoft Fabric fundamentals

## Exercises

- Map every component of your Phase 20 final project onto an Azure equivalent (table format: local tool -> Azure service).
- Using a free-tier/student Azure account, deploy one small piece (e.g., a storage account + one Data Factory pipeline) as a conceptual proof.
- Document how Key Vault would replace your local `.env`-based secrets (Phase 04).

## Expected Output

- A mapping table: local stack component -> Azure service -> why.

## Validation Checklist

- [ ] You can explain what Microsoft Fabric bundles together relative to the separate services you've mapped.

## Common Mistakes

- Assuming every local tool has an exact 1:1 Azure equivalent — some map to a combination of services.

## Optional Challenges

- Actually provision the free-tier resources with Terraform (Phase 07) instead of the Azure Portal.

## Reflection Questions

- Which local components would you migrate first if this became a real production system?
