# CloudDash Permissions System

## Overview
CloudDash uses a role-based access control (RBAC) system to manage permissions. This guide explains the different permission levels, how inheritance works, and common troubleshooting steps.

## Permission Levels

### User Roles

| Role | Description | Capabilities |
|------|-------------|--------------|
| **Viewer** | Basic access role | • View assigned dashboards<br>• Export data from viewable dashboards<br>• Save personal dashboard layouts |
| **Analyst** | Data analysis role | • All Viewer capabilities<br>• Create personal dashboards<br>• Create and modify widgets<br>• Access to raw data exports |
| **Manager** | Team leadership role | • All Analyst capabilities<br>• Create and share team dashboards<br>• Manage team members' access<br>• Configure alerts and schedules |
| **Admin** | System administration | • All Manager capabilities<br>• User management<br>• System configuration<br>• Security settings<br>• Billing management |

### Workspace-Level Permissions
- Permissions can be applied at the workspace level
- Users can have different roles in different workspaces
- Workspace admins can only manage their specific workspace

### Resource-Level Permissions
- Dashboards, data sources, and reports can have specific permissions
- Resource owners can share with specific users or groups
- Can override workspace-level permissions (both grant and restrict)

## Permission Inheritance

### Inheritance Rules
- Permissions flow from organization → workspace → resource
- More specific permissions override more general ones
- Explicit denials always override grants
- Group permissions apply to all group members

### Important Exception
- Permission inheritance does not apply across workspace boundaries
- A Manager in Workspace A has no special access in Workspace B unless explicitly granted

## Common Issues and Solutions

### "Access Denied" Errors
- **Cause**: User lacks necessary permissions for the resource
- **Solution**:
  1. Check user's role in the current workspace
  2. Verify if resource has restricted permissions
  3. Request access from resource owner or admin

### "Missing Dashboards"
- **Cause**: Dashboards are not shared with the user
- **Solution**:
  1. Verify dashboard exists (admin can check)
  2. Check if dashboard is in a different workspace
  3. Request sharing permissions from dashboard owner

### "Cannot Edit Widget"
- **Cause**: User has Viewer permissions on a dashboard
- **Solution**:
  1. Request edit permissions from dashboard owner
  2. Create a personal copy of the dashboard (if allowed)
  3. Check if dashboard is locked for editing

## Managing Permissions (Admin Guide)

### Adding Users
1. Navigate to Admin → User Management
2. Click "Add User"
3. Enter email address and select initial role
4. Choose workspaces to grant access to
5. Send invitation

### Creating Groups
1. Navigate to Admin → Group Management
2. Click "Create Group"
3. Name the group and add description
4. Add members by email or from existing users
5. Set group permissions
6. Save group

### Auditing Permissions
1. Navigate to Admin → Security
2. Select "Permission Audit"
3. Search for user or resource
4. Review effective permissions
5. Make adjustments as needed

## Best Practices

1. Follow the principle of least privilege
2. Use groups for easier permission management
3. Regularly audit permissions, especially for sensitive data
4. Document permission assignments for critical resources
5. Train users on permission requests and sharing procedures
6. Create workspace boundaries that align with organizational structure