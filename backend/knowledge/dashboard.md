# CloudDash Dashboard Configuration Guide

## Overview
Dashboards are the primary way to visualize and interact with your data in CloudDash. This guide covers how to create, configure, and troubleshoot dashboards.

## Dashboard Types

### Standard Dashboards
- Pre-configured visualizations
- Easy to set up
- Limited customization
- Best for getting started quickly

### Custom Dashboards
- Full customization of visualizations
- Can include data from multiple sources
- Requires Analyst permission or higher
- Best for advanced analytics needs

### Shared Dashboards
- Viewable by multiple users
- Can be embedded in external applications
- Maintains live connection to data
- Best for team collaboration

## Widget Configuration

### Data Widgets
- **Line Charts**: Time-series data visualization
- **Bar Charts**: Comparison between categories
- **Pie Charts**: Showing proportions of a whole
- **Tables**: Detailed data in tabular format
- **KPI Cards**: Single metric with comparison to previous period

### Configuration Steps
1. Click "Add Widget" on any dashboard
2. Select the widget type
3. Choose the data source
4. Configure display options (title, axes, colors)
5. Set refresh rate (minimum 5 minutes for enterprise accounts)
6. Apply any filters
7. Save widget

## Time Zone Settings
- All dashboards have time zone settings
- Time zone affects data grouping and time-based calculations
- Default is set to organization time zone
- Can be overridden per dashboard
- Time zone changes affect all visualizations on the dashboard

## Permissions and Sharing

### Permission Levels
- **Viewer**: Can only view dashboards assigned to them
- **Analyst**: Can create and modify their own dashboards
- **Manager**: Can share and collaborate on team dashboards
- **Admin**: Full system access including user management

### Sharing a Dashboard
1. Open the dashboard
2. Click "Share" in the top right
3. Enter user emails or select groups
4. Choose permission level for each recipient
5. Enable/disable export capabilities
6. Click "Send" to share

### Embedding Dashboards
1. Open the dashboard
2. Click "Embed" in the top right
3. Configure iframe settings
4. Copy the embed code
5. Paste into your application or website

## Common Issues and Solutions

### "Widget Failed to Load"
- **Cause**: Data source unavailable or permissions issue
- **Solution**:
  1. Check your permissions for the data source
  2. Verify the data source is still available
  3. Try refreshing the dashboard

### "Dashboard Performance Issues"
- **Cause**: Too many widgets or complex calculations
- **Solution**:
  1. Reduce the number of widgets
  2. Increase the refresh interval
  3. Use pre-aggregated data sources
  4. Apply filters to reduce data size

### "Time Zone Discrepancies"
- **Cause**: Dashboard time zone doesn't match expected time zone
- **Solution**:
  1. Check dashboard time zone settings
  2. Verify user account time zone settings
  3. Adjust as needed in dashboard settings

## Best Practices

1. Limit dashboards to 10-15 widgets for optimal performance
2. Group related visualizations on the same dashboard
3. Use clear titles and descriptions
4. Set appropriate refresh rates based on data update frequency
5. Use filters to focus on relevant data
6. Consider user permissions when designing shared dashboards