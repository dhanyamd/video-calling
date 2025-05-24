# CloudDash Demo Application

A simple analytics dashboard application designed to showcase the LiveKit AI Video Agent's capabilities for technical support scenarios.

## Purpose

This is a minimal web application that simulates common issues users might encounter with a SaaS analytics platform. The AI agent can view your screen while you navigate this application and provide contextual help based on what it sees.

## Demo Scenarios

### 1. Export Size Exceeded Error
- **Navigate to**: Data Export page
- **Action**: Try to export "User Analytics (25,000 rows)" in CSV format (default selection)
- **Issue**: Export fails with "Export Failed: Size Exceeded" error message
- **Expected Agent Response**: 
  1. Agent identifies the error on screen
  2. Explains that CSV format has a 10,000 row limit
  3. Guides user to switch to XLSX format
  4. Walks through clicking the XLSX radio button
  5. Confirms the export should work with XLSX format

**Demo Flow**:
1. Navigate to "Data Export" 
2. Leave defaults selected and click "Generate Export"
3. Error appears - ask agent for help
4. Follow agent guidance to select XLSX format
5. Export succeeds

### 2. Widget Configuration Issue
- **Navigate to**: Dashboard page 
- **Issue**: "Performance Metrics" widget shows "No Data" error with refresh rate too low
- **Expected Agent Response**:
  1. Agent identifies the widget error on screen
  2. Explains that 1-hour refresh rate is too low for real-time data
  3. Guides user to click the gear icon (⚙️) on the widget
  4. Walks through changing refresh rate to 5 or 15 minutes
  5. Confirms widget should display data after update

**Demo Flow**:
1. Look at Dashboard page - notice "Performance Metrics" widget error
2. Ask agent for help with the broken widget
3. Follow agent guidance to click gear icon and change refresh rate
4. Widget displays data successfully

## How to Use for Demos

### Setup
1. Open `index.html` in a web browser
2. Start your LiveKit video session and share your screen showing CloudDash
3. Have the agent ready to respond to questions

### Demo Flow

#### Widget Configuration Demo
1. **Show the Dashboard page** - agent should see the broken "Performance Metrics" widget with red error
2. **Ask naturally**: "Can you help me fix this widget that's not working?"
3. **Follow agent guidance**: Agent will guide you to click the gear icon (⚙️) and change refresh rate
4. **Confirm each step**: "I clicked the gear icon" / "I changed it to 5 minutes"
5. **Success**: Widget shows data and confirmation message

#### Export Error Demo  
1. **Navigate to Data Export page** - defaults are already set to trigger the error
2. **Click "Generate Export"** - red error message appears
3. **Ask for help**: "I'm getting an export error, can you help?"
4. **Follow agent guidance**: Agent will guide you to select XLSX format instead
5. **Success**: Export succeeds with success message

### Demo Tips
- **Speak clearly** and wait for agent responses
- **Describe what you see** if agent needs clarification
- **Confirm actions** to show the interactive troubleshooting process
- **Use natural language** - no need to be technical

### Resetting Between Demos
- **Refresh the page** (F5 or Ctrl+R) to reset both scenarios to initial state
- **Export error** will be cleared
- **Widget will be broken again** - ready for the next demo
- Both scenarios reset instantly and can be repeated multiple times

## Features

- **Minimal Design**: Clean, focused interface for demo purposes
- **Two Core Pages**: Dashboard and Data Export only
- **Two Demo Issues**: Widget configuration and export format problems
- **Interactive Fixes**: Real solutions that users can perform
- **Step-by-step Guidance**: Clear resolution paths for the AI agent

## Technical Details

- Pure HTML, CSS, and JavaScript (no dependencies)
- Responsive grid layout
- CSS animations and hover effects
- Simulated error states and loading conditions
- Local file that can be opened directly in any browser

This application aligns with the knowledge base content in the video agent to provide accurate, contextual responses during technical support scenarios.