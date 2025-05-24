# CloudDash Data Export Guide

## Overview
CloudDash offers multiple ways to export your data for analysis, reporting, and integration with other systems. This guide covers the available export formats, their limitations, and common troubleshooting steps.

## Export Formats

### CSV Format
- **Best for**: Simple tabular data and spreadsheet imports
- **Limitations**: Maximum 10,000 rows
- **Use case**: Monthly reports, simple metrics tracking
- **Common error**: "Export size exceeded" - This occurs when trying to export more than 10,000 rows in CSV format

### XLSX Format
- **Best for**: Larger datasets, preserving formatting
- **Limitations**: Maximum 100,000 rows
- **Use case**: Quarterly reports, financial analysis
- **Required for**: Any dataset exceeding 10,000 rows

### JSON Format
- **Best for**: Preserving data hierarchies and structure
- **Limitations**: More complex to work with in spreadsheet applications
- **Use case**: System integrations, API connections
- **Special note**: Includes full metadata unlike other formats

## Export Process

1. Navigate to **Admin Panel**
2. Select **Data Management**
3. Click on **Exports** tab
4. Choose the dashboard or dataset to export
5. Select your desired format
6. Configure any filters or date ranges
7. Click "Generate Export"
8. You'll receive a notification when the export is ready to download

## Permissions Required

| Export Type | Required Permission |
|-------------|---------------------|
| Dashboard | Viewer access or higher |
| Raw data | Analyst access or higher |
| User data | Admin access only |
| System logs | Admin access only |

## Common Issues and Solutions

### "Export Failed: Size Exceeded"
- **Cause**: Trying to export too many rows in a format with row limitations
- **Solution**: 
  1. Switch to XLSX format for datasets between 10,000 and 100,000 rows
  2. Apply filters to reduce the dataset size
  3. Break the export into multiple smaller exports

### "Export Failed: Permission Denied"
- **Cause**: User doesn't have sufficient permissions for the requested data
- **Solution**:
  1. Request elevated permissions from your administrator
  2. Export only the datasets you have permission to access

### "Export Timed Out"
- **Cause**: The export request took too long to process
- **Solution**:
  1. Apply filters to reduce the dataset size
  2. Schedule the export for off-peak hours
  3. Break the export into multiple smaller requests

## Best Practices

1. Schedule large exports during off-peak hours
2. Use filters to export only the data you need
3. Use XLSX for larger datasets
4. Use JSON when integrating with other systems
5. Consider recurring exports for regular reporting needs